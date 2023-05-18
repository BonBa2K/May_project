from pydantic import BaseModel
from pydantic.schema import Optional

class FP_bagF_City(BaseModel):
    code:Optional[str]
    country:Optional[str]
    lineType:Optional[str]
    Name:Optional[str]

class FP_bagF_Baginfo(BaseModel):
    weight:Optional[int]
    unit:Optional[str]
    piece:Optional[int]
    size:Optional[str]
    sizeType:Optional[int]
    text:Optional[str]
    
class Flight_seats_FP_bagF(BaseModel):
    fromCity:FP_bagF_City
    toCity:FP_bagF_City
    checkInBaggage:FP_bagF_Baginfo
    carryOnBaggage:FP_bagF_Baginfo
    segmentNo:Optional[int]
    sequenceNo:Optional[str]
    passengerType:Optional[str]
    route:Optional[str]

class Flight_seats_FP_bag(BaseModel):
    Segment:Optional[str]
    Text:Optional[str]

class Flight_seats_FP(BaseModel):
    baggageFormats:Optional[list[Flight_seats_FP_bagF]]
    penaltyFormat:Optional[str]
    baggageTag:Optional[str]
    penaltyFlag:Optional[int]
    penaltyTag:Optional[str]
    FarePenaltiesFlag:Optional[int]
    Penalties:Optional[str]
    Baggages:Optional[list[Flight_seats_FP_bag]]
    NationDisallowed:Optional[str]
    NationAllowed:Optional[str]
    CityAllowed:Optional[str]
    Remark:Optional[str]