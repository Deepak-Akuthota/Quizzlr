import requests

parameters={
   "amount":10,
    "type":"boolean"
    "category"=18
    }
responce=requests.get("https://opentdb.com/api.php",params=parameters)
responce.raise_for_status()
data=responce.json()
question_data=data["results"]