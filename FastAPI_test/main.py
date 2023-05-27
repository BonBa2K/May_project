from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .crud import post_flight_multi,post_trend_price
from .schemas import mult_param,useful_F_data,trend_param,Message
from pydantic.schema import Optional
from starlette.middleware.cors import CORSMiddleware

tags_metadata = [
    {"name": "Flight"},
    {"name": "Trend"},
]
app = FastAPI(openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.post("/flights/",
    tags=["Flight"],
    responses={
        200:{
            "model":list[useful_F_data],
            "description":"搜尋成功"
        },
        404:{
            "model":Message,
            "description":"無查詢結果"
        }
    }
)
def read_flight_multi(param_in: mult_param):
    """
    航班查詢：
    根據輸入的「出發機場」、「目的機場」、「出發日期」來搜尋符合的航班
    - **a_AC**: 出發機場代號
    - **d_AC**: 目的機場代號
    - **d_date**: 出發日期(ex: 2023-05-29)
    """
    Ans = post_flight_multi(
        arrival_AC=param_in.a_AC, departure_AC=param_in.d_AC, dDate=param_in.d_date
    )
    if len(list(Ans)) == 0:
        return JSONResponse(status_code=404, content={"message": "Flight cannot found"})
    else:
        return Ans

    
@app.post("/chartData/",
    responses={
        200:{
            "model":list[Optional[int]],
            "description":"搜尋成功"
        },
        404:{
            "model":Message,
            "description":"無查詢結果"
        }
    }
)
def read_trend_price(param_in: trend_param):
    """    
    趨勢圖資料查詢：
    根據輸入的「查詢月份」、「出發城市」、「目的城市」來取得趨勢圖會用到的價格資料
    - **mon**: 查詢月份
    - **ori**: 出發城市
    - **dest**: 目的城市
    """
    Ans = post_trend_price(
        month=param_in.mon, origin=param_in.ori, destination=param_in.dest
    )
    if len(list(Ans)) == 0:
        return JSONResponse(status_code=404, content={"message": "trend cannot found"})
    else:
        return Ans



# @app.post("/flights_all/", tags=["Flight"], response_model=list[Flight])
# def read_flight_multi_all(param_in: mult_param):
#     Ans = post_flight_multi_all(
#         arrival_AC=param_in.a_AC, departure_AC=param_in.d_AC, dDate=param_in.d_date
#     )
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans

# @app.get(
#     "/flights_sc/{s_code}", tags=["Flight"], response_model=list[Flight]
# )
# def read_flights_from_airline_code(s_code: str):
#     Ans = get_flight_from_airline_code(searchCode=s_code)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans

    
# @app.post("/LogIn/", tags=["LogIn"], response_model=str)
# def LogIn(param_in: LogIn_param):
#     Ans = post_LogIn(UN=param_in.UserName, PW=param_in.Password)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans
    


# @app.post("/flights_ac/", tags=["Flight"], response_model=list[Flight])
# def read_flights_from_airport_code(arrival_code: str, departure_code: str):
#     Ans = get_flight_from_airport_code(
#         arrivalAC=arrival_code, departureAC=departure_code
#     )
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans


# @app.post("/flights_oid/", tags=["Flight"], response_model=Flight)
# def read_flights_from_oid(o_id: str):
#     Ans = get_flight_from_oid(id_in=o_id)
#     print("Ans == ")
#     print(Ans)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans


# @app.post("/FD_oid/", tags=["Flight"], response_model=list[Flight_FD])
# def read_FD_from_oid(o_id: str):
#     Ans = post_FD_from_oid(id_in=o_id)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans


# @app.post("/tran_oid/", tags=["Flight"], response_model=Flight_transfer)
# def read_tran_from_oid(o_id: str):
#     Ans = post_tran_from_oid(id_in=o_id)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans


# @app.post("/seats_oid/", tags=["Flight"], response_model=list[Flight_seats])
# def read_seat_from_oid(o_id: str):
#     Ans = post_seat_from_oid(id_in=o_id)
#     if len(list(Ans)) == 0:
#         raise HTTPException(status_code=404, detail="Flight cannot found")
#     else:
#         return Ans
