# RAG-based SQL Query Generator

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline that uses Google Gemini (via langchain_google_genai) to generate and execute validated SQL queries on a SQLite database through a FastAPI backend.

It supports natural language questions like

##### “Show total revenue from completed orders”

and safely converts them into valid SQL SELECT statements.

# 🚀 Features

#### ✅ Natural Language → SQL generation using Google Gemini
#### ✅ RAG pipeline — uses document context to improve accuracy
#### ✅ SQL validation layer (prevents DDL/DML like DROP, DELETE, UPDATE)
#### ✅ Asynchronous FastAPI backend
#### ✅ SQLite database integration
#### ✅ Error handling for malformed or unsafe SQL
#### ✅ Extensible design — easily switch models or databases

# Tech Stack

1. LangChain for RAG pipeline orchestration
2. Google Gemini (via langchain_google_genai) for LLM-based SQL generation
3. HuggingFace for Embedding model
4. FastAPI for API serving
5. SQLite for local relational database
6. SQLGlot for SQL parsing and validation
7. Pydantic / AsyncIO for typed async state handling

# Setup

### 1. Install required dependencies
pip install -r requirements.txt

### 2. Create sample sqlite DB
python sample_db/create_sample_db.py

### 3. Create vector db
python ingestion/index_sqlite.py

### 4. Run Fast API server
uvicorn server.app:app --reload --port 8000

### 5. Run Streamlit app
streamlit run client/app.py


# 🔍 Example Query Flow

### Input:

{
  "question": "What is the total revenue from completed orders?"
}


### LLM-generated SQL:

SELECT SUM(total_amount) FROM orders WHERE status = 'completed'


### Output:

{
  "SUM(total_amount)": 8927.87
}

# 🧰 Validation Rules

### The SQL validator ensures:

1. Only SELECT statements are executed.

2. No DDL/DML keywords (INSERT, UPDATE, DELETE, DROP, etc.).

3. Only allowed tables (like orders, customers) are referenced.


# Architecture Overview

### Flow:

User Question → Retrieve Context → LLM Generates SQL → SQL Validation → DB Execution → JSON Response


### Key Node:
. sql_generator_node cleans and filters the SQL response from the model:

. Removes markdown (```)

. Keeps only SELECT statements

. Strips extra characters

. Stores the result in state["generated_sql"]

# 🛡️ Safety

✔️ Prevents harmful SQL commands

✔️ Validates structure using sqlglot

✔️ Sanitizes model outputs before execution



