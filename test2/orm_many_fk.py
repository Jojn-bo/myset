from sqlalchemy import Integer, ForeignKey,String,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer, ForeignKey('address.id'))
    shipping_address_id = Column(Integer, ForeignKey('address.id'))

    billing_address = relationship('Address', foreign_keys=[billing_address_id])
    shipping_address = relationship('Address', foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return self.street


engine = create_engine("mysql+pymysql://root:12345@localhost/python",
                       encoding='utf-8')

Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)
session = Session_class()

# addr1 = Address(street='Tiantongyuan', city='ChangPing', state='BJ')
# addr2 = Address(street='Wudaokou', city='Haidian', state='BJ')
# addr3 = Address(street='Yanjiao', city='LangFang', state='HB')
#
# session.add_all([addr1, addr2, addr3])
#
# c1 = Customer(name='Alex',billing_address=addr1,shipping_address=addr2)
# c2 = Customer(name='Jack',billing_address=addr3,shipping_address=addr3)
#
# session.add_all([c1, c2])

# obj = session.query(Customer).filter(name='alex').first()
# print(obj.name, obj.billing_address, obj.shipping_address)

session.commit()