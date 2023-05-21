from . import schemas
from .database import mydb
from bson.objectid import ObjectId

mycol = mydb["Flight"]

def post_LogIn(UN:str, PW:str):
    UserCol=mydb["UserTest"]
    x = UserCol.find({"username": UN,"password": PW})
    Ans = []
    for ele in x:
        Ans.append(ele)
    return "good"



def get_flight_from_airline_code(searchCode: str):
    x = mycol.find({"airlineCode": searchCode})
    Ans = []
    for ele in x:
        Ans.append(ele)
    return Ans


def get_flight_from_airport_code(arrivalAC: str, departureAC: str):
    x = mycol.find(
        {"arrivalAirportCode": arrivalAC, "departureAirportCode": departureAC}
    )
    Ans = []
    for ele in x:
        Ans.append(ele)
    return Ans


def get_flight_from_oid(id_in: str):
    ele = mycol.find_one({"_id": ObjectId(id_in)})
    return ele


def post_flight_multi(arrival_AC: str, departure_AC: str, dDate: str):
    x = mycol.find(
        {
            "arrivalAirportCode": arrival_AC,
            "departureAirportCode": departure_AC,
        }
    )
    Ans = []
    for ele in x:
        if ele["flightDetails"][0]["goDate"]==dDate:
            flightNo_tmp_1 = []
            flightNo_tmp_2 = []
            price_tmp = []
            arriveD=""
            
            for seatIn in ele["seats"]:
                price_tmp.append(seatIn["price"])

            for el in ele["flightDetails"]:
                arriveD=el["toDate"]

            for FD in ele["flightDetails"]:
                flightNo_tmp_2.append(FD["flightNo"])

            flightNo_tmp_1.append(flightNo_tmp_2)

            Ans.append(
                schemas.useful_F_data(
                    id_in=str(ele["_id"]),
                    airlineName=ele["airlineName"],
                    arrivalAirportCode=ele["arrivalAirportCode"],
                    arrivalAirportName=ele["arrivalAirportName"],
                    arrivalCityName=ele["arrivalCityName"],
                    arrivalDate=arriveD,
                    arrivalTime=ele["arrivalTime"],
                    departureAirportCode=ele["departureAirportCode"],
                    departureAirportName=ele["departureAirportName"],
                    departureCityName=ele["departureCityName"],
                    departureDate=dDate,
                    departureTime=ele["departureTime"],
                    flightNo=flightNo_tmp_1,
                    price=price_tmp,
                )
            )
    return Ans


def post_trend_price(month: str,origin: str,destination: str):
    TrendCol=mydb["TrendData"]
    DestDict = TrendCol.find_one({"destination": destination})
    Ans = []
    for ele in DestDict["TD"]:
        if("-"+month+"-" in ele["outboundDate"]):
            Ans.append(ele["price"])
        
    return Ans
    
def post_flight_multi_all(arrival_AC: str, departure_AC: str, dDate: str):
    x = mycol.find(
        {
            "arrivalAirportCode": arrival_AC,
            "departureAirportCode": departure_AC,
            "departureDate": dDate,
        }
    )
    Ans = []
    for ele in x:
        Ans.append(ele)
    return Ans


# def post_FD_from_oid(id_in: str):
#     tar = mycol.find_one({"_id": ObjectId(id_in)})
#     FD_parsed = tar["flightDetails"]
#     return FD_parsed


# def post_seat_from_oid(id_in: str):
#     tar = mycol.find_one({"_id": ObjectId(id_in)})
#     seats_parsed = tar["seats"]
#     return seats_parsed


# def post_tran_from_oid(id_in: str):
#     tar = mycol.find_one({"_id": ObjectId(id_in)})
#     tran_parsed = tar["transit"]
#     return tran_parsed
