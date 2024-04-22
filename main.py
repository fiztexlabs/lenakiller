from typing import Union

from fastapi import FastAPI

import rsp

app = FastAPI()

h2o = rsp.createSubstance("H2O_IF97")

@app.get("/")
async def read_root():
    return {"Hello": rsp.callProperty(h2o,"D","PT",[101325,300])}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    req = rsp.callProperty(h2o,"D","PT",[101325,item_id])
    
    return {"item_id": req, "q": q}
    # return {"item_id": item_id, "q": q}
