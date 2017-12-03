import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DATE
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

engine = create_engine("mysql+pymysql://root:12345@localhost/python",
                       encoding='utf-8')
Base = declarative_base()  # 生成orm基类


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)
    gender = Column(Enum("M", "F"), nullable=False)

    def __repr__(self):
        return '<{} name;{} register_date:{} gender:{}>'.format(self.id, self.name, self.register_date, self.gender)


class StudyRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'))

    def __repr__(self):
        return '<%s name:%s>' % (self.id, self.day)


Base.metadata.create_all(engine)  # 创建表结构
