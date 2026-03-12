from sqlalchemy import Table,MetaData
from src.database.engine import engine



meta = MetaData()


userrecords = Table(
    'userrecords',
    meta,
    autoload_with=engine
)

loan_predictions = Table(
    "loan_predictions",
    meta,
    autoload_with=engine
)