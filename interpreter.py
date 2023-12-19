import psycopg2

from sqlalchemy import create_engine

 
# Create an engine instance
alchemyEngine   = create_engine('postgresql+psycopg2://postgres:1234@127.0.0.1:5432', pool_recycle=3600);

# Connect to PostgreSQL server
dbConnection = alchemyEngine.connect()
