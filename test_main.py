from fastapi.testclient import TestClient
from main import app
from models import Currencies
from database.database import DataBase
import json

client = TestClient(app)

'''
def test_read_today_records():
    db_obj = DataBase('db.json')
    for currency in Currencies:
        response = client.get(f'/today/{currency}/')
        test_obj = response.json()
        #print(test_obj['message'])
        assert response.status_code == 200
        assert test_obj == str
        assert test_obj[0]['hour'] == str
        assert test_obj[0]['value'] == float

'''