from sqlalchemy import create_engine, MetaData
engine = create_engine("mysql+pymysql://master:craft@db/demo")
meta = MetaData()
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
