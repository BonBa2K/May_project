from . import schemas
from .database import mydb
from bson.objectid import ObjectId

mycol = mydb["Flight"]


def get_flight_from_airline_code(searchCode: str):
    x = mycol.find({"airlineCode": searchCode})
    Ans = []
    for ele in x:
        Ans.append(ele)
    return Ans


def get_flight_from_airport_code(arrivalAC: str,departureAC: str):
    x = mycol.find({"arrivalAirportCode": arrivalAC,"departureAirportCode": departureAC})
    Ans = []
    for ele in x:
        Ans.append(ele)
    return Ans


def get_flight_from_oid(id_in: str):
    ele = mycol.find_one({"_id": ObjectId(id_in)})
    return ele


def post_flight_from_multi(
    arrival_AC: str, departure_AC: str, aDate: str, dDate: str
):
    x = mycol.find(
        {
            "arrivalAirportCode": arrival_AC,
            "departureAirportCode": departure_AC,
            "arrivalDate": aDate,
            "departureDate": dDate,
        }
    )
    Ans = []
    for ele in x:
        Ans.append(ele)
    return Ans


def post_FD_from_oid(id_in: str):
    tar = mycol.find_one({"_id": ObjectId(id_in)})
    FD_parsed = tar["flightDetails"]
    return FD_parsed


def post_seat_from_oid(id_in: str):
    tar = mycol.find_one({"_id": ObjectId(id_in)})
    seats_parsed = tar["seats"]
    return seats_parsed


def post_tran_from_oid(id_in: str):
    tar = mycol.find_one({"_id": ObjectId(id_in)})
    tran_parsed = tar["transit"]
    return tran_parsed
