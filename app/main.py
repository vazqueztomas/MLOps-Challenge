import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class FootballPlayer(BaseModel):
	id: int
	fname: str
	lname: str
	age: int
	isPlay: bool

players = {
   0: FootballPlayer(id=1,fname="Juan Roman", lname="Riquelme", age=42, isPlay=False), 
   1: FootballPlayer(id=2,fname="Martin", lname="Palermo", age=40, isPlay=False), 
   2: FootballPlayer(id=3,fname="Guillermo", lname="Barros Schelotto", age=40, isPlay=False), 
   3: FootballPlayer(id=4,fname="Sebastián", lname="Battaglia", age=41, isPlay=False), 
   4: FootballPlayer(id=5,fname="Exequiel", lname="Zeballos", age=20, isPlay=True)
}

app = FastAPI()
#app get
@app.get('/')
async def root() -> dict[str, dict[int, FootballPlayer]]:
    return {"players": players}

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
