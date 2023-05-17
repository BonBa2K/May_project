# from sqlalchemy.orm import Session

# from . import models, schemas
from . import schemas
from .database import mydb,dblst
from bson.objectid import ObjectId

def post_flight_from_multi(arrivalCity:str,departureCity:str,aDate:str,dDate:str):
    mycol = mydb["Flight"]
    x = mycol.find({"arrivalCityCode": arrivalCity,"departureCityCode": departureCity,"arrivalDate": aDate,"departureDate": dDate})
    Ans=[]
    for ele in x:
        Ans.append(schemas.Flight(
            airlineCode=ele["airlineCode"],
            airlineFlitername=ele["airlineFlitername"],
            airlineName=ele["airlineName"],
            arrivalAirportCode=ele["arrivalAirportCode"],
            arrivalAirportName=ele["arrivalAirportName"],
            arrivalCityCode=ele["arrivalCityCode"],
            arrivalCityName=ele["arrivalCityName"],
            arrivalDate=ele["arrivalDate"],
            arrivalTime=ele["arrivalTime"],
            crossDays=ele["crossDays"],
            departureAirportCode=ele["departureAirportCode"],
            departureAirportName=ele["departureAirportName"],
            departureCityCode=ele["departureCityCode"],
            departureCityName=ele["departureCityName"],
            departureDate=ele["departureDate"],
            departureTerminal=ele["departureTerminal"],
            departureTime=ele["departureTime"],
            flightKey=ele["flightKey"],
            stopType=ele["stopType"],
            stuTicketGrp=ele["stuTicketGrp"],
            validatingAirlineCode=ele["validatingAirlineCode"],
        ))
    return Ans

def get_flight_from_airline_code(searchCode:str):
    mycol = mydb["Flight"]
    x = mycol.find({"airlineCode": searchCode})
    Ans=[]
    for ele in x:
        Ans.append(schemas.Flight(
            airlineCode=ele["airlineCode"],
            airlineFlitername=ele["airlineFlitername"],
            airlineName=ele["airlineName"],
            arrivalAirportCode=ele["arrivalAirportCode"],
            arrivalAirportName=ele["arrivalAirportName"],
            arrivalCityCode=ele["arrivalCityCode"],
            arrivalCityName=ele["arrivalCityName"],
            arrivalDate=ele["arrivalDate"],
            arrivalTime=ele["arrivalTime"],
            crossDays=ele["crossDays"],
            departureAirportCode=ele["departureAirportCode"],
            departureAirportName=ele["departureAirportName"],
            departureCityCode=ele["departureCityCode"],
            departureCityName=ele["departureCityName"],
            departureDate=ele["departureDate"],
            departureTerminal=ele["departureTerminal"],
            departureTime=ele["departureTime"],
            flightKey=ele["flightKey"],
            stopType=ele["stopType"],
            stuTicketGrp=ele["stuTicketGrp"],
            validatingAirlineCode=ele["validatingAirlineCode"],
        ))
    return Ans

def get_flight_from_oid(id_in:str):
    mycol = mydb["Flight"]
    ele = mycol.find_one({"_id": ObjectId(id_in)})
    return schemas.Flight(
            airlineCode=ele["airlineCode"],
            airlineFlitername=ele["airlineFlitername"],
            airlineName=ele["airlineName"],
            arrivalAirportCode=ele["arrivalAirportCode"],
            arrivalAirportName=ele["arrivalAirportName"],
            arrivalCityCode=ele["arrivalCityCode"],
            arrivalCityName=ele["arrivalCityName"],
            arrivalDate=ele["arrivalDate"],
            arrivalTime=ele["arrivalTime"],
            crossDays=ele["crossDays"],
            departureAirportCode=ele["departureAirportCode"],
            departureAirportName=ele["departureAirportName"],
            departureCityCode=ele["departureCityCode"],
            departureCityName=ele["departureCityName"],
            departureDate=ele["departureDate"],
            departureTerminal=ele["departureTerminal"],
            departureTime=ele["departureTime"],
            flightKey=ele["flightKey"],
            stopType=ele["stopType"],
            stuTicketGrp=ele["stuTicketGrp"],
            validatingAirlineCode=ele["validatingAirlineCode"],
        )

# # get part
# def get_flights(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Flight).offset(skip).limit(limit).all()


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# # post part
# def post_flight(db: Session, flight: schemas.FlightCreate):
#     db_flight = models.Flight(
#         flightKey=flight.flightKey,
#         departureDate=flight.departureDate,
#         departureTime=flight.departureTime,
#         arrivalDate=flight.arrivalDate,
#         arrivalTime=flight.arrivalTime,
#         crossDays=flight.crossDays,
#         departureCityCode=flight.departureCityCode,
#         arrivalCityCode=flight.arrivalCityCode,
#         departureCityName=flight.departureCityName,
#         arrivalCityName=flight.arrivalCityName,
#         departureAirportCode=flight.departureAirportCode,
#         departureAirportName=flight.departureAirportName,
#         arrivalAirportCode=flight.arrivalAirportCode,
#         arrivalAirportName=flight.arrivalAirportName,
#         departureTerminal=flight.departureTerminal,
#         arrivalTerminal=flight.arrivalTerminal,
#         stopType=flight.stopType,
#         transit=flight.transit,
#         airlineName=flight.airlineName,
#         airlineFlitername=flight.airlineFlitername,
#         airlineCode=flight.airlineCode,
#         validatingAirlineCode=flight.validatingAirlineCode,
#         seats=flight.seats,
#         flightDetails=flight.flightDetails,
#         stuTicketGrp=flight.stuTicketGrp,
#     )
#     db.add(db_flight)
#     db.commit()
#     db.refresh(db_flight)
#     return db_flight


# def post_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def put_user(db: Session, user_id: int, user_email: str, user_active: bool):
#     if db.query(models.User).filter(models.User.id == user_id).first() == None:
#         return None
#     else:
#         p = db.query(models.User).filter(models.User.id == user_id).first()
#         p.email = user_email
#         # p.is_active = user_active
#         db.commit()
#         return {"message": "user update successfully"}


# def delete_user(db: Session, user_id: int):
#     if db.query(models.User).filter(models.User.id == user_id).first() == None:
#         return None
#     else:
#         db.query(models.User).filter(models.User.id == user_id).delete()
#         db.commit()
#         return {"message": "user deleted successfully"}


# # def get_items(db: Session, skip: int = 0, limit: int = 100):
# #     return db.query(models.Item).offset(skip).limit(limit).all()

# # def post_item(db: Session, item: schemas.ItemCreate, user_id: int):
# #     db_item = models.Item(**item.dict(), owner_id=user_id)
# #     db.add(db_item)
# #     db.commit()
# #     db.refresh(db_item)
# #     return db_item


# # def put_item(db: Session, item_id: int, item_title: str, item_description: str):
# #     if db.query(models.Item).filter(models.Item.id == item_id).first() == None:
# #         return None
# #     else:
# #         p = db.query(models.Item).filter(models.Item.id == item_id).first()
# #         p.title = item_title
# #         p.description = item_description
# #         db.commit()
# #         return p


# # def delete_item(db: Session, item_id: int):
# #     if db.query(models.Item).filter(models.Item.id == item_id).first() == None:
# #         return None
# #     else:
# #         db.query(models.Item).filter(models.Item.id == item_id).delete()
# #         db.commit()
# #         return {"message": "Item deleted successfully"}
