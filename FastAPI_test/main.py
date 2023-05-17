from fastapi import Depends, FastAPI, HTTPException

from . import crud, schemas
from .database import mydb,dblst

tags_metadata = [
    {"name": "FlightGet"},
    # {"name": "FlightPost"},
    # {"name": "FlightPut"},
    # {"name": "FlightDelete"},
    # {"name": "UserGet"},
    # {"name": "UserPost"},
    # {"name": "UserPut"},
    # {"name": "UserDelete"},
]
app = FastAPI(openapi_tags=tags_metadata)

@app.get("/flights/{s_code}", tags=["FlightGet"], response_model=list[schemas.Flight])
def read_flights_from_airline_code(s_code:str):
    return crud.get_flight_from_airline_code(searchCode=s_code)


@app.get("/flights/{o_id}", tags=["FlightGet"], response_model=schemas.Flight)
def read_flights_from_oid(o_id:str):
    return crud.get_flight_from_oid(id_in=o_id)

@app.post("/flights/", tags=["FlightGet"], response_model=list[schemas.Flight])
def read_flight_from_multi(a_city:str,d_city:str,a_date:str,dDate:str):
    Ans =crud.post_flight_from_multi(arrivalCity=a_city,departureCity=d_city,aDate=a_date,dDate=dDate)
    if len(list(Ans)) == 0 :
        raise HTTPException(status_code=404, detail="Flight cannot found")
    return Ans

