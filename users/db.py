from sqlalchemy import create_engine, text
engine = create_engine("mysql+pymysql://master:craft@db/demo")
conn = engine.connect()

#how to use it
# result = conn.execute(text('show databases'))
# for row in result:
#     print(result)
