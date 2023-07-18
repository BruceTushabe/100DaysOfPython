from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create the database engine
engine = create_engine('mysql+mysqlconnector://username:password@localhost/database_name', echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Define your data model using SQLAlchemy's declarative syntax
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship('Order', back_populates='customer')

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    total_amount = Column(Integer)
    customer = relationship('Customer', back_populates='orders')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example usage: Inserting data into the database
customer1 = Customer(name='John Doe')
customer2 = Customer(name='Jane Smith')
session.add_all([customer1, customer2])
session.commit()

order1 = Order(total_amount=100, customer=customer1)
order2 = Order(total_amount=200, customer=customer2)
session.add_all([order1, order2])
session.commit()

# Example usage: Querying data from the database
customers = session.query(Customer).all()
for customer in customers:
    print(customer.name)
    for order in customer.orders:
        print(f"Order ID: {order.id}, Amount: {order.total_amount}")

# Close the session
session.close()
