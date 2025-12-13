# Weekly Progress Log
## Task List & Estimated Hours (Technical Evaluation)

## Week of Nov 30 – Dec 6
**Estimated time:**   2 hours
- Setup repository.
- Create a fork on GitHub
- Install Python
- Fix any missing folder issues

### Study the system using the Medium article  
**Estimated time:**   3 hours 
- Read and understand the architecture  
- Understand how LangChain + FastAPI + SQL parsing interact  
- Explore the folder structure  
- Follow the flow of the code

### Set up and run the project locally  
**Estimated time:** 4 hours
- Create virtual environment  
- Install dependencies  
- Resolve library version issues  
- Run the backend and frontend  
- Test locally  

###  Make modifications to the system  
**Estimated time:** 6 hours
- Understand existing logic for SELECT parsing  
- Modify or extend SQL translation logic
- extend functionality to support INSERT statements
- Add handling in executor
- Update SQL validation rules
- Add error handling and safe checks
- Test with your own examples 
- Debug issues  


### Tasks worked on & actual hours spent
- Cloned the ConvertQueryToSQL repository and created a local working copy – 1 hour
- Set up Python on my machine and fixed path issues (reinstalling version, verifying environment) – 2 hours
- Created a virtual environment and installed the required dependencies – 1 hour
- Resolved missing-folder and file-visibility issues in VS Code (understanding why only LICENSE/readme appeared, fixing folder     structure,understanding shallow clone behavior) – 1 hour
- Studied the Medium article and examined the system architecture (LangChain → embeddings → Chroma → FastAPI → SQL executor) – 3 hours
- Ran the server locally, tested endpoints, checked errors with API key and configuration, fixed `.env` formatting and model naming issues –   2 hours
- Explored the code flow: how queries are embedded → retrieved → parsed → executed in SQLite – 2 hours
- Investigated SQL parsing logic, especially SELECT handling – 1 hour
- extend functionality to support INSERT statements (initial exploration and planning where to implement it) - 1 hour
- Documented blockers and open questions – 0.5 hour

###  Blockers / Open Questions
- Would like clarification on how LangChain calls flow into our FastAPI endpoints.
- Need clarification on which parts of the codebase are considered stable/core and which parts are expected to change when extending the system.
- Would appreciate clarification on whether the place where I implemented the initial INSERT functionality is aligned with the intended architecture, and if this is the correct module to extend for this feature.


## Weekly Progress Update – Weekend Work (Dec 7 – Dec 13)

### Summary
Over the weekend, I focused on progressing INSERT support, validating basic end-to-end flow, and gaining a clearer understanding of the system architecture.

---

### Tasks Completed & Time Spent

#### Progress on INSERT statement support (3 hours)
- Implemented an initial version of INSERT support in the SQL translation layer.
- Extended the executor logic to handle INSERT alongside existing SELECT functionality.
- Added a basic separation between read (SELECT) and write (INSERT) operations.

---

#### SQL validation and safety (2 hours)
- Performed an initial update of SQL validation rules to allow INSERT statements.
- Added basic structural checks for valid SQL.
- Improved error messages returned by the API for failed queries.
- Ensured existing SELECT functionality remains unaffected.

---

#### Architecture review and flow understanding (3 hours)
- Traced the full request flow: LangChain → FastAPI → SQL executor.
- Identified core/stable components versus extension points in the codebase.
- Evaluated whether the current INSERT implementation aligns with the overall architecture.

---

#### Documentation and reporting (0.5 hours)
- Updated the weekly progress log.
- Documented current limitations and open questions.

---

### Total Time Spent
** 8.5 hours**

---

### Open Questions / Points for Clarification
1. Which parts of the codebase should be considered stable core components and avoided when adding new SQL features (e.g., INSERT)?
2. Is the current location of the INSERT implementation aligned with the long-term architecture of the system?
3. Are there additional safety, validation, or permission requirements expected for write operations?
4. Based on the Medium article, the RAG-related work (LangChain setup, embeddings, retrieval, validation) is a broader effort that may span multiple weeks and require significant cumulative time, rather than being completed within a single weekend of ~10 hours. I would appreciate clarification on the expected scope and depth at this stage.

I would also appreciate clearer, more concrete task definitions or milestones to help better guide my work and ensure alignment with expectations. 

---








