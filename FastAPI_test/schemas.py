# 因為 SQLAlchemy 跟 Pydantic 對model的定義不一樣，所以 Pydantic 的 model 一律以 schemas 來對待
from pydantic import BaseModel
from pydantic.schema import Optional
from bson.objectid import ObjectId
from .F_seats_sub_schema import Flight_seats_FP

class mult_param(BaseModel):
    a_AC: str
    d_AC: str
    d_date: str

class trend_param(BaseModel):
    mon: str
    ori: str
    dest: str
    
class Message(BaseModel):
    message: str

# class LogIn_param(BaseModel):
#     UserName: str
#     Password: str

# 座位資訊
class Flight_seats(BaseModel):
    seatCount:Optional[int]
    seatType:Optional[str]
    feeConfirm:Optional[bool]
    currencyCode:Optional[str]
    price:Optional[int]
    averagePrice:Optional[int]
    averagePriceNoTax:Optional[int]
    priceWithoutTax:Optional[int]
    priceWithTax:Optional[int]
    adultPrice:Optional[int]
    adultCnt:Optional[int]
    adultTax:Optional[int]
    childPrice:Optional[int]
    childTax:Optional[int]
    childCnt:Optional[int]
    infantPrice:Optional[int]
    infantTax:Optional[int]
    infantCnt:Optional[int]
    selectedFlightParas:Optional[str]
    selectedFlightInfo:Optional[str]
    displayCategory:Optional[int]
    classType:Optional[str]
    allClassType:Optional[str]
    engineType:Optional[str]
    remarkId:Optional[str]
    fareInfo:Optional[str]
    planCategory:Optional[str]
    resourceName:Optional[str]
    resourceDesc:Optional[str]
    freeBaggage:Optional[int]
    productDesc:Optional[str]
    ticketingDesc:Optional[str]
    ticketingCode:Optional[int]
    ageRestriction:Optional[str]
    passportTag:Optional[str]
    companionFare:Optional[str]
    combineTag:Optional[str]
    FarePenaltiesFlag:Optional[int]
    FarePenalties:Optional[Flight_seats_FP]
    easeTag:Optional[str]
    ticketType:Optional[str]
    license:Optional[str]

# 轉機資訊
class Flight_transfer(BaseModel):
    isCrossday: Optional[bool]
    isChangeAirport: Optional[bool]
    isChangeTerminal: Optional[bool]
    TransitType: Optional[int]
    TransferCity: Optional[str]
    TransferSpan: Optional[str]

# Flight_FD代表航班細節

class Flight_FD_craft(BaseModel):
    craftType : Optional[str]
    enName : Optional[str]
    widthLevel : Optional[str]
    minSeats : Optional[int]
    maxSeats : Optional[int]
    craftName : Optional[str]

class Flight_FD(BaseModel):
    departureFullDate : Optional[str]
    departureDate : Optional[str]
    arrivalDate : Optional[str]
    goDate : Optional[str]
    departureTime : Optional[str]
    toDate : Optional[str]
    arrivalTime : Optional[str]
    isRedEye : Optional[bool]
    durationMinutes : Optional[int]
    transferStayMinutes : Optional[int]
    departureCity : Optional[str]
    departureCityCode : Optional[str]
    departureCityName : Optional[str]
    arrivalCity : Optional[str]
    arrivalCityCode : Optional[str]
    arrivalCityName : Optional[str]
    airlineCode : Optional[str]
    airline : Optional[str]
    flightNo : Optional[str]
    operatingAirlineCode : Optional[str]
    operatingAirline : Optional[str]
    operatingFlightNo : Optional[str]
    craft: Optional[Flight_FD_craft]
    transitType : Optional[int]
    departureAirportCode : Optional[str]
    departureAirportName : Optional[str]
    departureTerminal : Optional[str]
    arrivalAirportCode : Optional[str]
    arrivalAirportName : Optional[str]
    arrivalTerminal : Optional[str]
    cabinType : Optional[str]
    cabinDesc : Optional[str]
    bookingClass : Optional[str]
    crossDays : Optional[int]
    stopList : Optional[list]
    transfer : Optional[Flight_transfer]
    seqNo : Optional[int]
    segmentNo : Optional[int]
    sequenceNo : Optional[int]
    baggageStraight : Optional[int]
    dterminal : Optional[str]
    aterminal : Optional[str]
    dport : Optional[str]
    aport : Optional[str]

# 航班資料
class Flight(BaseModel):
    _id:Optional[ObjectId]
    airlineCode:Optional[str]
    airlineFlitername:Optional[str]
    airlineName:Optional[str]
    arrivalAirportCode:Optional[str]
    arrivalAirportName:Optional[str]
    arrivalCityCode:Optional[str]
    arrivalCityName:Optional[str]
    arrivalDate:Optional[str]
    arrivalTerminal:Optional[str]
    arrivalTime:Optional[str]
    crossDays:Optional[int]
    departureAirportCode:Optional[str]
    departureAirportName:Optional[str]
    departureCityCode:Optional[str]
    departureCityName:Optional[str]
    departureDate:Optional[str]
    departureTerminal:Optional[str]
    departureTime:Optional[str]
    flightDetails:Optional[list[Flight_FD]]
    flightKey:Optional[str]
    seats:Optional[list[Flight_seats]]
    stopType:Optional[int]
    stuTicketGrp:Optional[bool]
    transit:Optional[Flight_transfer]
    validatingAirlineCode:Optional[str]
    class Config:
        orm_mode = True

class useful_F_data(BaseModel):
    airlineName:Optional[str]
    arrivalAirportCode:Optional[str]
    arrivalAirportName:Optional[str]
    arrivalCityName:Optional[str]
    arrivalDate:Optional[str]
    arrivalTime:Optional[str]
    departureAirportCode:Optional[str]
    departureAirportName:Optional[str]
    departureCityName:Optional[str]
    departureDate:Optional[str]
    departureTime:Optional[str]
    price:Optional[list[int]]
    flightNo : Optional[list[list[str]]]

# 使用者資料
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
