import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Replace with your actual connection string
DATABASE_URL = "postgresql://dbAdmin2025:My%24ecurePass2025%21@mystudyproject.postgres.database.azure.com:5432/postgres?sslmode=require"

def test_db_connection():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            print("Connection successful! Test query returned:", result.fetchone())
    except OperationalError as e:
        print("Connection failed:", str(e))

if __name__ == "__main__":
    test_db_connection()