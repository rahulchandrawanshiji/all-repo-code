'''When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.

A request body is data sent by the client to your API. A response body is the data your API sends to the client.

Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.'''

from fastapi import FastAPI       #FastAPI is a library
from pydantic import BaseModel 
from flask import Flask,jsonify   #BaseModel from the pydantic library is used for data validation and data conversion, 
                                    #helping you define data models and ensure data conforms to the expected format.
class Item(BaseModel):           #This line imports the BaseModel class from the Pydantic library.
                                  # BaseModel is the base class for creating data models that provide data validation and parsing.

    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


#####################################################################################################################################

'''Create your data mode l¶
Then you declare your data model as a class that inherits from BaseModel.

Use standard Python types these file  item are extendert which provie minimum there are derive which  substentent 
import the library thet help cases thet are expand there derive  extenderd for which another way these also include functionlaliy ther are 
substruction unsessary precause devident particle for all the attributes:


'''

from fastapi import FastAPI
from schema import Item


app = FastAPI()


@app.post("/items/")
async def create_item():
    return "hellow world"
