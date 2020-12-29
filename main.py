import uvicorn
from fastapi import FastAPI, Path, Request, Query
from fastapi.responses import JSONResponse
from models import Currencies, MyException
from typing import List
from datetime import datetime
import database.queries
from scrapper.crone_script import perform_scrapping


app = FastAPI(title='CPTT',
              description='Currency Price Tracking Tool',
              version='0.0.1')


@app.get("/dates/{currency}/")
async def read_date_records(currency: Currencies, q: List[str] = Query(["01-12-2020", str(datetime.today().strftime("%d-%m-%Y"))])):
    query_items = {"q": q}
    try:
        result = await database.queries.currency_dates_query(currency, query_items, db_obj)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        raise MyException(e)


@app.get("/today/{currency}/")
async def read_today_records(currency: Currencies):
    try:
        result = await database.queries.currency_today_query(currency, db_obj)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        raise MyException(e)


@app.get("/all/{currency}/")
async def read_alltime_records(currency: Currencies):
    try:
        result = await database.queries.currency_alltime_query(currency, db_obj)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        raise MyException(e)


@app.exception_handler(MyException)
async def exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        content={"message": f"Error {exc} occured!"}
    )


if __name__ == "__main__":
    db_obj = perform_scrapping()
    uvicorn.run(app, host="127.0.0.1", port=8000)
