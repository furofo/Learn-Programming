### SQL Alchemy Example
from sqlalchemy import Engine, text, create_engine, Column, Integer, String
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# Define the base class for the ORM
Base = declarative_base()

# Define a sample class to be mapped to the table
class Sample(Base):
    __tablename__ = 'some_table'
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)

# Create an in-memory SQLite database
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Session = sessionmaker(engine)
# Create the table
Base.metadata.create_all(engine)

# Create some sample objects
some_object = Sample(x=1, y=10)
some_other_object = Sample(x=2, y=20)

# Define a SQL statement
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")

# Use a session to add objects and commit them to the database
with Session.begin() as session:
    session.add(some_object)
    session.add(some_other_object)


# Query the database using the defined statement
with Session() as session:
    result = session.execute(stmt, {'y': 15})
    for row in result:
        print(f"x: {row.x}, y: {row.y}")