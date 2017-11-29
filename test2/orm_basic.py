import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy.types import Date, Enum

#   "mysql+pymysql://root:12345@localhost/python"
# 对应    类型        用户名：密码@主机/表名
# engine = create_engine("mysql+pymysql://root:12345@127.0.0.1/python",
#                        encoding='utf-8', echo=True)#echo=True 会打印所有的信息
engine = create_engine("mysql+pymysql://root:12345@localhost/python",
                       encoding='utf-8')
Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '<%s name:%s>' % (self.id, self.name)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(Date, nullable=False)
    gender = Column(Enum("M", "F"), nullable=False)

    def __repr__(self):
        return '<{} name;{} register_date:{} gender:{}>'.format(self.id, self.name, self.register_date, self.gender)


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

user_obj1 = User(name="alex1", password="alex3714")  # 生成你要创建的数据对象
user_obj2 = User(name="bo", password="12345")
user_obj3 = User(name='a', password='555')
user_obj4 = User(name='b', password='444')
user_obj5 = User(name='c', password='336')
user_obj6 = User(name='b', password='254')

s1 = Student(name='s2', register_date='2015-02-22', gender='M')
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
Session.add_all([user_obj1, user_obj2, user_obj3, user_obj4, user_obj5, user_obj6, s1])

# data = Session.query(User).filter_by(name='alex').all()
# print(data[0].name, data[0].password)

# data = Session.query(User).filter_by(id=2).all()
# print(data)

# data = Session.query(User).filter(User.id > 1).filter(User.id < 4).all()
# print(data)

# print(Session.query(User).filter(User.name.in_(['Alex1', 'a'])).count())#in类似于between，count统计总条数，不区分大小写
print('user:', Session.query(User.name, func.count(User.name)).group_by(User.name).all())
date = Session.query(Student).filter_by().all()
print(date)

# Session.commit()  # 现此才统一提交，创建数据
