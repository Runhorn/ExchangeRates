from tinydb import TinyDB, Query


class DataBase:
    def __init__(self, db_name):
        tables_list = ['eur', 'usd', 'chf', 'gbp']
        self.db_name = db_name
        db = TinyDB(self.db_name)

        for table_name in tables_list:
            if table_name not in db.tables():
                db.table(table_name)

        db.close()

    def insert_data(self, data_dict):
        db = TinyDB(self.db_name)
        row = Query()
        table = db.table(data_dict['currency'])
        if table.contains(row.date == data_dict['date'] and row.hour == data_dict['hour']):
            pass
        else:
            db.table(data_dict['currency']).insert({
                'date': data_dict['date'],
                'hour': data_dict['hour'],
                'value': data_dict['exchange_rate']
            })
        db.close()