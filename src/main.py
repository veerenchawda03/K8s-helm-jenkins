from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from fastapi_health import health
import uvicorn



app = FastAPI()
def get_session():
    return True

def is_app_online(session: bool = Depends(get_session)):
    return session

app = FastAPI()
app.add_api_route("/health", health([is_app_online]))



@app.get("/")
async def get_call():


    return {"message": "This is a GET call, QA check 3.8.2021"}






@app.put("/")
async def put_call():
    return {"message": "This is a PUT call"}

@app.post("/")
async def post_call():
    return {"message": "This is a POST call"}




@app.delete("/")
async def delete_call():
    return {"message": "This is a DELETE call"}







if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=False)










