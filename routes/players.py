from fastapi import APIRouter, HTTPException
from models.player import FootballPlayer

router = APIRouter(prefix='/players')

players = [
   FootballPlayer(player_id=1,fname="Juan Roman", lname="Riquelme", age=42, isPlay=False), 
   FootballPlayer(player_id=2,fname="Martin", lname="Palermo", age=40, isPlay=False), 
   FootballPlayer(player_id=3,fname="Guillermo", lname="Barros Schelotto", age=40, isPlay=False), 
   FootballPlayer(player_id=4,fname="Sebastián", lname="Battaglia", age=41, isPlay=False), 
   FootballPlayer(player_id=5,fname="Exequiel", lname="Zeballos", age=20, isPlay=True)
]


@router.get("/")
async def get_players():
    return {"players": players}


@router.get("/{player_id}")
async def get_player_by_id(player_id: int):
    return search_player(player_id)


@router.post("/", response_model=FootballPlayer)
async def charge_player(player: FootballPlayer):
    try:
        players.append(player)
        return player
    except Exception as err:
        raise HTTPException(status_code=500, detail="Server error") from err
    
    
@router.put("/", response_model=FootballPlayer)
async def update_player(player: FootballPlayer):
    found = False

    for index, saved_player in enumerate(players):
        if saved_player.player_id == player.player_id:
            players[index] = player
            found = True
            return player
    
    if not found:
        raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{player_id}")
async def delete_player(player_id: int):
    for index, player in enumerate(players):
        if player.player_id == player_id:
            del players[index]
            return {"Player eliminated"}
    
    raise HTTPException(status_code=404, detail="User not exists")
            

def search_player(player_id: int):
    playerFound = filter(lambda p: p.player_id == player_id, players)
    try:
        return list(playerFound)[0]
    except Exception as err:
        raise HTTPException(status_code=404, detail="Player not found") from err