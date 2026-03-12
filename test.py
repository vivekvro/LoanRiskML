from sqlalchemy import create_engine,MetaData,Table,Column,Integer,PrimaryKeyConstraint,Enum
from dotenv import load_dotenv
load_dotenv()
import os
db_key = os.getenv('MYSQL_DB_KEY')
engine = create_engine(db_key,echo=True)

meta = MetaData()

userrecords = Table(
    "userrecords",
    meta,
    autoload_with=engine
)

meta.create_all(engine)

conn = engine.connect()




conn.commit()