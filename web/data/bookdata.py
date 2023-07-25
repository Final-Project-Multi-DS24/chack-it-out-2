from sqlalchemy import create_engine
import pandas as pd
db_connection_str = 'mysql+pymysql://root:1234@127.0.0.1/book'
db_connection = create_engine(db_connection_str)
conn = db_connection.connect()
df=pd.read_sql("SELECT * FROM tb_book", con=conn)