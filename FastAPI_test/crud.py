from .schemas import useful_F_data
from .database import mydb
from bson.objectid import ObjectId


def post_flight_multi(arrival_AC: str, departure_AC: str, dDate: str):
    # 從資料庫中取得符合「出發地」、「目的地」的資料
    mycol = mydb["Flight"]
    x = mycol.find(
        {
            "arrivalAirportCode": arrival_AC,
            "departureAirportCode": departure_AC,
        }
    )
    Ans = []
    # 對每筆資料進行一次處理
    for ele in x:
        # 如果符合出發日期則匯入輸出list中
        if ele["flightDetails"][0]["goDate"] == dDate:
            
            flightNo_tmp_1 = []
            flightNo_tmp_2 = []
            price_tmp = []
            arriveD = ""

            # 根據行李規則的不同，價格可能會有複數種，於是用list來儲存
            for seatIn in ele["seats"]:
                price_tmp.append(seatIn["price"])
            # 取得航班號碼與出發日
            for el in ele["flightDetails"]:
                arriveD = el["toDate"]
                flightNo_tmp_2.append(el["flightNo"])
            # 航班號碼可能會因為轉機而出現複數種，於是用list來儲存
            flightNo_tmp_1.append(flightNo_tmp_2)

            Ans.append(
                useful_F_data(
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


def post_trend_price(month: str, origin: str, destination: str):
    TrendCol = mydb["TrendData"]
    # 從資料庫中取得符合「目的地」的資料
    # 資料庫端僅提供從台北出發，有待修改
    DestDict = TrendCol.find_one({"destination": destination})
    Ans = []

    # 對每筆資料進行一次處理
    for ele in DestDict["TD"]:
        # 如果符合出發日期則匯入輸出list中
        if "-" + month + "-" in ele["outboundDate"]:
            Ans.append(ele["price"])
            print("Ans == ")
            print(Ans)
    return Ans


# def post_flight_multi_all(arrival_AC: str, departure_AC: str, dDate: str):
#     x = mycol.find(
#         {
#             "arrivalAirportCode": arrival_AC,
#             "departureAirportCode": departure_AC,
#             "departureDate": dDate,
#         }
#     )
#     Ans = []
#     for ele in x:
#         Ans.append(ele)
#     return Ans

# def post_LogIn(UN: str, PW: str):
#     UserCol = mydb["UserTest"]
#     x = list(UserCol.find({"username": UN, "password": PW}))
#     return "good"


# def get_flight_from_airline_code(searchCode: str):
#     x = mycol.find({"airlineCode": searchCode})
#     Ans = []
#     for ele in x:
#         Ans.append(ele)
#     return Ans


# def get_flight_from_airport_code(arrivalAC: str, departureAC: str):
#     x = mycol.find(
#         {"arrivalAirportCode": arrivalAC, "departureAirportCode": departureAC}
#     )
#     Ans = []
#     for ele in x:
#         Ans.append(ele)
#     return Ans


# def get_flight_from_oid(id_in: str):
#     ele = mycol.find_one({"_id": ObjectId(id_in)})
#     return ele

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

