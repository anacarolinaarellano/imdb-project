import os
from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP,
    Text,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

def get_postgres_uri():
    host = os.environ.get("DB_HOST", "postgres")
    port = 5432
    password = os.environ.get("DB_PASS", "abc123")
    user, db_name = "movies", "movies"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


engine = create_engine(
    get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)


Base = declarative_base()

# Object Relational Mappers
# SOLID principle identified: Interface Segregation
class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)

class MovieLine(Base):
    __tablename__ = "movie_line"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    create_time = Column(TIMESTAMP(timezone=True), index=True)
    movie = relationship(Movie)


def start_mappers():
    Base.metadata.create_all(engine)