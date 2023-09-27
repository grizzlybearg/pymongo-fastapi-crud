"""
Note: We'll be using shell commands to create files and directories, and navigate through them. 
If you prefer, you can use a graphical file explorer instead.

Let's start by implementing a simple root / endpoint that returns a welcome message. 
Open the main.py file in your favorite code editor and add the following:

pymongo-fastapi-crud/main.py

Save the file and run the application using the uvicorn package, 
which was installed together with the fastapi package.

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}'''


We will use the python-dotenv package to load environment variables 
ATLAS_URI and DB_NAME from the .env file. Then, we'll use the pymongo package to 
connect to the Atlas cluster when the application starts. We'll add another event handler to close 
the connection when the application stops. Open the main.py file again and replace 
its contents with the following:
"""

from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

'''
Register the /book endpoints
Finally, we need to register the /book endpoints. 
Open the main.py file, import the routes module, 
and register the book router. 
Your final version of the main.py file should look like this:
'''
app.include_router(book_router, tags=["books"], prefix="/book")