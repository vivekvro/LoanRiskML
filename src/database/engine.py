from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()
db_key = os.getenv('MYSQL_DB_KEY')
engine = create_engine(db_key,echo=False)
