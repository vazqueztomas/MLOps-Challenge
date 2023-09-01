from pydantic import BaseModel

class FootballPlayer(BaseModel):
	player_id: int
	fname: str
	lname: str
	age: int
	isPlay: bool