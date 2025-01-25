### SQL Alchemy Example
from sqlalchemy import Engine, text, create_engine, Column, Integer, String
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# Define the base class for the ORM
Base = declarative_base()

# Define a sample class to be mapped to the table
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create an in-memory SQLite database
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Session = sessionmaker(engine)
# Create the table
Base.metadata.create_all(engine)

# Create some sample objects
user1 = User(name="John", age=10)
user2 = User(name="Stacy", age=10)
user3 = User(name="Alice", age=10)
user4 = User(name="Bob", age=10)
user5 = User(name="Charlie", age=10)
user6 = User(name="Diana", age=10)
user7 = User(name="Eve", age=10)
user8 = User(name="Frank", age=5)
user9 = User(name="Grace", age=5)
user10 = User(name="Hank", age=10)

# Define a SQL statement
stmt = text("SELECT name FROM User WHERE age  < :age ORDER BY name")

# Use a session to add objects and commit them to the database
with Session.begin() as session:
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.add(user5)
    session.add(user6)
    session.add(user7)
    session.add(user8)
    session.add(user9)
    session.add(user10)

# Query the database using the defined statement
with Session() as session:
    result = session.execute(stmt, {'age': 10})
    for row in result:
        print(f"Name: {row.name}")