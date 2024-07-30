# let start with the basic program to know about api 
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
async def root ():
    return {"command  ":"hello world "}

'''  firstly to create a api we going with step by step
     1 create a folder  and open in vscode 
     2 create a file lile firstapi.py 
     3 create the virtual invoirnment  the command is =   python -m venv venv 
     4 activate the venv .\venv\scrip\activate 
     5 install the fastapi  command is  pip install fastapi uvicorn
     6 run the application  command is   uvicorn firstpr:app --reload 
     '''