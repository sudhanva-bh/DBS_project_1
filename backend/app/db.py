from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/bookmyshow')
engine = create_engine(DATABASE_URL)
