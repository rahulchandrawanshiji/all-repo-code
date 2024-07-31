from fastapi import FastAPI
app = FastAPI()

@app.get("/")              # data ko get karega 
async def root ():
    return {"messege ":"hello "}

@app.post("/")
async def post():
    return {"command ":"hello post "}

@app.put("/")
async def put ():
    return {"hello":"hello put"}

############################################### PATH PARAMETERE ##########################################################


@app.get("/item/(item_id)")
def index(item_id):
    return {"product_id":"item_id"}




#############################################3 qury parametere #############################################################3


@app.get("/items/")
def box(q:int,m:Optional[int]=10):
    return{"product is":q,"m":m}