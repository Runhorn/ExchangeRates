from tinydb import TinyDB, Query, where
from database import database
from datetime import datetime
#from asyncio import sleep


async def currency_dates_query(currency, dates, db_obj):
    db = TinyDB(db_obj.db_name)
    Query()
    table = db.table(currency.title().lower())
    data = table.search(dates['q'][0] <= where('date') <= dates['q'][1])
    db.close()
    return data


async def currency_today_query(currency, db_obj):
    db = TinyDB(db_obj.db_name)
    Query()
    # await sleep
    table = db.table(currency.title().lower())
    data = table.search(where('date') == str(datetime.today().strftime("%d-%m-%Y")))
    db.close()
    return data


async def currency_alltime_query(currency, db_obj):
    db = TinyDB(db_obj.db_name)
    Query()
    table = db.table(currency.title().lower())
    data = table.all()
    db.close()
    return data
