import uvicorn
from fastapi import FastAPI
from routes import players


app = FastAPI()

app.include_router(players.router)
#app get
@app.get('/')
async def root():
    return {"Challenge": "MLOps - API // Challenge"}

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
