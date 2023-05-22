from fastapi import Depends, FastAPI, HTTPException, Request
from starlette.middleware.cors import CORSMiddleware
from . import crud, schemas
from .database import mydb, dblst
from pydantic.schema import Optional

tags_metadata = [
    {"name": "Flight"},
    {"name": "Trend"},
    {"name": "LogIn"},
]
app = FastAPI(openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/LogIn/", tags=["LogIn"], response_model=str)
def LogIn(param_in: schemas.LogIn_param):
    Ans = crud.post_LogIn(UN=param_in.UserName, PW=param_in.Password)
    if len(list(Ans)) == 0:
        raise HTTPException(status_code=404, detail="Flight cannot found")
    else:
        return Ans
    
@app.get(
    "/flights_sc/{s_code}", tags=["Flight"], response_model=list[schemas.Flight]
)
def read_flights_from_airline_code(s_code: str):
    Ans = crud.get_flight_from_airline_code(searchCode=s_code)
    if len(list(Ans)) == 0:
        raise HTTPException(status_code=404, detail="Flight cannot found")
    else:
        return Ans

@app.post("/flights/", tags=["Flight"], response_model=list[schemas.useful_F_data])
def read_flight_multi(param_in: schemas.mult_param):
    Ans = crud.post_flight_multi(
        arrival_AC=param_in.a_AC, departure_AC=param_in.d_AC, dDate=param_in.d_date
    )
    if len(list(Ans)) == 0:
        raise HTTPException(status_code=404, detail="Flight cannot found")
    else:
        return Ans

@app.post("/flights_all/", tags=["Flight"], response_model=list[schemas.Flight])
def read_flight_multi_all(param_in: schemas.mult_param):
    Ans = crud.post_flight_multi_all(
        arrival_AC=param_in.a_AC, departure_AC=param_in.d_AC, dDate=param_in.d_date
    )
    if len(list(Ans)) == 0:
        raise HTTPException(status_code=404, detail="Flight cannot found")
    else:
        return Ans
    
@app.post("/chartData/", tags=["Trend"], response_model=list[Optional[int]])
def read_trend_price(param_in: schemas.trend_param):
    Ans = crud.post_trend_price(
        month=param_in.mon, origin=param_in.ori, destination=param_in.dest
    )
    if len(list(Ans)) == 0:
        raise HTTPException(status_code=404, detail="Flight cannot found")
    else:
        return Ans
    


# @app.post("/flights_ac/", tags=["Flight"], response_model=list[schemas.Flight])
# def read_flights_from_airport_code(arrival_code: str, departure_code: str):
#     Ans = crud.get_flight_from_airport_code(
#         arrivalAC=arrival_code, departureAC=departure_code
#     )
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans


# @app.post("/flights_oid/", tags=["Flight"], response_model=schemas.Flight)
# def read_flights_from_oid(o_id: str):
#     Ans = crud.get_flight_from_oid(id_in=o_id)
#     print("Ans == ")
#     print(Ans)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans


# @app.post("/FD_oid/", tags=["Flight"], response_model=list[schemas.Flight_FD])
# def read_FD_from_oid(o_id: str):
#     Ans = crud.post_FD_from_oid(id_in=o_id)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans


# @app.post("/tran_oid/", tags=["Flight"], response_model=schemas.Flight_transfer)
# def read_tran_from_oid(o_id: str):
#     Ans = crud.post_tran_from_oid(id_in=o_id)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans


# @app.post("/seats_oid/", tags=["Flight"], response_model=list[schemas.Flight_seats])
# def read_seat_from_oid(o_id: str):
#     Ans = crud.post_seat_from_oid(id_in=o_id)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans
