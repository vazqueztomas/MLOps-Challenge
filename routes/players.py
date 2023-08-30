from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/player')

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


@router.get("/players")
async def get_players():
    return {"players": players}