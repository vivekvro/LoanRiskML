
from src.database.tables import userrecords,loan_predictions
from src.database.engine import engine
from sqlalchemy import select,Table

def insert_in_userrecords(data: dict):
    try:
        with engine.begin() as conn:
            conn.execute(userrecords.insert(), data)
        return 1
    except Exception as e:
        print(e)
        return 0


def insert_in_loan_predictions(data: dict):
    try:
        with engine.begin() as conn:
            conn.execute(loan_predictions.insert(), data)
        return 1
    except Exception as e:
        print(e)
        return 0 

def get_by_id(user_id: int,table:Table):
    with engine.connect() as conn:
        result = conn.execute(
            select(table).where(table.c.id==user_id)
        )
        row = result.fetchone()

        if row:
            return dict(row._mapping)

        return None
