"""Database storage using SQLAlchemy."""

from datetime import datetime
from typing import List, Dict, Any

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Float
from sqlalchemy.orm import sessionmaker, declarative_base

from aire.config.settings import Settings

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    date = Column(DateTime)
    category = Column(String(50))
    severity = Column(Float)

class Benchmark(Base):
    __tablename__ = "benchmarks"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    metric = Column(String(100))
    value = Column(Float)
    category = Column(String(50))

class Evaluation(Base):
    __tablename__ = "evaluations"
    id = Column(Integer, primary_key=True)
    assessment = Column(String(255))
    score = Column(Float)
    category = Column(String(50))
    date = Column(DateTime)

class Database:
    def __init__(self, url: str):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def store_incidents(self, data: List[Dict[str, Any]]) -> None:
        session = self.Session()
        for item in data:
            # Convert date string to datetime if needed
            if 'date' in item and isinstance(item['date'], str):
                item['date'] = datetime.fromisoformat(item['date'])
            incident = Incident(**item)
            session.add(incident)
        session.commit()
        session.close()

    def store_benchmarks(self, data: List[Dict[str, Any]]) -> None:
        session = self.Session()
        for item in data:
            benchmark = Benchmark(**item)
            session.add(benchmark)
        session.commit()
        session.close()

    def store_evaluations(self, data: List[Dict[str, Any]]) -> None:
        session = self.Session()
        for item in data:
            if 'date' in item and isinstance(item['date'], str):
                item['date'] = datetime.fromisoformat(item['date'])
            evaluation = Evaluation(**item)
            session.add(evaluation)
        session.commit()
        session.close()