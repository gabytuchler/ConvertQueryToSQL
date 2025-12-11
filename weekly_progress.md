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
-Cloned the ConvertQueryToSQL repository and created a local working copy – 1 hour
-Set up Python on my machine and fixed path issues (reinstalling version, verifying environment) – 2 hours
-Created a virtual environment and installed the required dependencies – 1 hour
-Resolved missing-folder and file-visibility issues in VS Code (understanding why only LICENSE/readme appeared, fixing folder structure,understanding shallow clone behavior) – 1 hour
-Studied the Medium article and examined the system architecture (LangChain → embeddings → Chroma → FastAPI → SQL executor) – 3 hours
-Ran the server locally, tested endpoints, checked errors with API key and configuration, fixed `.env` formatting and model naming issues – 2 hours
-Explored the code flow: how queries are embedded → retrieved → parsed → executed in SQLite – 2 hours
-Investigated SQL parsing logic, especially SELECT handling – 1 hour
-extend functionality to support INSERT statements (initial exploration and planning where to implement it) - 1 hour
- Documented blockers and open questions – 0.5 hour








