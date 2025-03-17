from sqlalchemy import create_engine, Column, String, Integer, Float, Text, Boolean, TIMESTAMP, ForeignKey, LargeBinary, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError
import datetime

# SQLAlchemy Database Connection Details
DB_NAME = "algeval"
DB_USER = "postgres"
DB_PASSWORD = "ashascugpt4o"
DB_HOST = "localhost"
DB_PORT = "5432"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
database_func = func
# Define the Instructor table
class Instructor(Base):
    __tablename__ = 'Instructor'
    
    instructor_name = Column(String(255), primary_key=True)
    email = Column(Text)
    department = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

# Define the Sessions table
class Sessions(Base):
    __tablename__ = 'Sessions'
    
    session_id = Column(String(255), primary_key=True)
    instructor_name = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    
    instructor = relationship("Instructor", backref="sessions", uselist=False)
    instructor_name = Column(String(255), ForeignKey('Instructor.instructor_name', ondelete="CASCADE"))

# Define the AnswerKey table
class AnswerKey(Base):
    __tablename__ = 'AnswerKey'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(255), nullable=False)
    sol_weight = Column(Float, nullable=False)
    fa_weight = Column(Float, nullable=False)
    ak_latex = Column(Text, nullable=False)
    ak_file = Column(LargeBinary, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    
    session = relationship("Sessions", backref="answer_keys")
    session_id = Column(String(255), ForeignKey('Sessions.session_id', ondelete="CASCADE"))

# Define the StudentHAS table
class StudentHAS(Base):
    __tablename__ = 'StudentHAS'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    answer_key_id = Column(Integer, nullable=False)
    has_name = Column(Text)
    has_latex = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    sol_fraction = Column(Text, nullable=True)
    sol_grade = Column(Float, nullable=False)
    fa_grade = Column(Float, nullable=False)
    overall_grade = Column(Float, nullable=False)
    used_asm = Column(Boolean, default=False, nullable=False)
    has_file = Column(LargeBinary, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    
    answer_key = relationship("AnswerKey", backref="student_has")
    answer_key_id = Column(Integer, ForeignKey('AnswerKey.id', ondelete="CASCADE"))

def setup_tables():
    """Ensure all tables exist before storing data."""
    try:
        # Create all tables
        Base.metadata.create_all(engine)
        print("All tables set up successfully.")
    except SQLAlchemyError as e:
        print(f"Database Setup Error: {e}")

# Call the setup_tables function to create the tables
if __name__ == "__main__":
    setup_tables()
