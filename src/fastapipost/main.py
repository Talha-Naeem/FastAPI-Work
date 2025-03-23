from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import Optional,List


class item(BaseModel):
    name: str
    id: int
    address: Optional[str]=None

app = FastAPI()

@app.post("/items")
def  senddata(user:item):
    return f"Kb aou gy {user.name} id no. {user.id} address {user.address}"

@app.post("/iu/{userid}")
def sendpathdata(userid:int,user:item):
    return f"Kb aou gy {user.name} id no. {user.id} address {user.address}"

@app.get("/it")
def optionlchk(q:Optional[str]=None):
    return {"mrzi hai" :{q}}

@app.get("/que")
def que(f:Optional[str]=Query(None,min_length=3,max_length=5,regex="lopiu")):
    return f

@app.get("/qu")
def que(f:Optional[List[str]]=Query(['dfg','bnm'])):
    return f