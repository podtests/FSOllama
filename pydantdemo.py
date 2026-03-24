from pydantic import BaseModel
from typing import TypedDict


class User(TypedDict):
    name: str
    age: int

u: User = {
    "name": "Akhil",
    
}

print(u["name"])



class WeatherResponse(BaseModel):
    city: str
    weather: str
    temperature: str

w = WeatherResponse(city="Delhi", weather="Sunny", temperature="78")
# print(w.model_json_schema())
#print(WeatherResponse.model_json_schema())
#print(WeatherResponse.model_dump())
#print(w)
# print(w.model_dump())
# print(w.model_dump_json())
# print(WeatherResponse.model_json_schema())

#w = w.model_validate_json('{"city":"78","weather":"Sunny","temperature":"78"}')
