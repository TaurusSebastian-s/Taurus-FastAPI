from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'tb_users'

    UserId_PK_CMS = Column(Integer, primary_key=True)
    Admin_ID = Column(Integer, nullable=True)
    Admin_ID_Old = Column(Integer, nullable=True)
    Admin_ID_New = Column(Integer, nullable=True)
    s_UserCode = Column(String(50), nullable=True)
    n_PersonInfoId_FK = Column(Integer, nullable=True)
    Username = Column(String(50), nullable=True)
    Password = Column(String(255), nullable=True)
    Email = Column(String(100), nullable=True)
    created_on = Column(DateTime, nullable=True)
    closing_date = Column(DateTime, nullable=True)
