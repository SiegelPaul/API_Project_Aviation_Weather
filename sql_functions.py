# We import a method from the  modules to address environment variables and 
# we use that method in a function that will return the variables we need from .env 
# to a dictionary we call sql_config

from dotenv import dotenv_values
import sqlalchemy
import pandas as pd

def get_sql_config():
    '''
        Function loads credentials from .env file and
        returns a dictionary containing the data needed for sqlalchemy.create_engine()
    '''
    needed_keys = ['host', 'port', 'database','user','password']
    dotenv_dict = dotenv_values(".env")
    sql_config = {key:dotenv_dict[key] for key in needed_keys if key in dotenv_dict}
    return sql_config
# this function is for database connection

# Import sqlalchemy and pandas - do this only when instructed



# Insert the get_data() function definition below - do this only when instructed in the notebook
def get_data(sql_query):
    sql_config = get_sql_config()
    engine = sqlalchemy.create_engine('postgresql://user:pass@host/database', connect_args=sql_config)
    with engine.begin() as conn: 
         results = conn.execute(sql_query)
         return results.fetchall()
    

#Insert the get_dataframe() function definition below - do this only when instructed in the notebook

def get_dataframe(sql_query):
    sql_config = get_sql_config()
    engine = sqlalchemy.create_engine('postgresql://user:pass@host/database', connect_args=sql_config)
    # with engine.begin() as conn: 
    #      results = conn.execute(sql_query)
    df = pd.read_sql_query(sql_query,con=engine)
    return df
     
# Insert the get_engine() function definition below - when instructed
def get_engine():
    sql_config = get_sql_config()
    engine = sqlalchemy.create_engine('postgresql://user:pass@host/database',connect_args=sql_config)
    return engine

