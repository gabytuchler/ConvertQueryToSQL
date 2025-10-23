from typing import TypedDict, List
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# state type
class RAGState(TypedDict, total=False):
    question: str
    retrieved_docs: List[str]
    generated_sql: str
    validated_sql: str
    sql_result: List[dict]
    messages: List[dict]


# init vectorstore & models
CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_persist")
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
TOP_K = int(os.getenv("TOP_K", "8"))

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
vectordb = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings, collection_name="sqlite_docs")
retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

sql_prompt = PromptTemplate.from_template("""
        You are a SQL generator. Based on the following context, generate a SINGLE READ-ONLY SQLite SELECT query (no semicolons, no multiple statements).
        Context:
        {context}
        
        Question:
        {question}
        
        Return only the SQL SELECT statement.
        """)


async def retriever_node(state: RAGState) -> RAGState:
    docs = await retriever.ainvoke(state["question"])
    state["retrieved_docs"] = [d.page_content for d in docs]
    return state



import re
from typing import Any

async def sql_generator_node(state: RAGState) -> RAGState:
    """
    Generate SQL from the retrieved documents and user question.
    Cleans LLM output, removes markdown/code fences, and ensures only SELECT statements remain.
    """
    # 1. Combine retrieved documents
    context = "\n\n".join(state.get("retrieved_docs", []))

    # 2. Format the prompt
    prompt_text = sql_prompt.format(context=context, question=state["question"])

    # 3. Call the LLM asynchronously
    out = await llm.ainvoke(prompt_text)

    # 4. Extract text content if output is an AIMessage or ChatResult
    if hasattr(out, "content"):
        out = out.content
    out = str(out).strip()

    # 5. Remove code fences ``` or ```sql and any leading/trailing whitespace
    out = re.sub(r"```(?:sql)?\n?", "", out, flags=re.IGNORECASE).replace("```", "").strip()

    # 6. Ensure the SQL starts with SELECT (case-insensitive)
    match = re.search(r"(select\b.*)", out, flags=re.IGNORECASE | re.DOTALL)
    if match:
        out = match.group(1).strip()
    else:
        # fallback if no SELECT found
        out = ""

    # 7. Optional: remove trailing semicolon if present
    out = out.rstrip(";").strip()

    # 8. Save cleaned SQL back to state
    state["generated_sql"] = out
    return state
