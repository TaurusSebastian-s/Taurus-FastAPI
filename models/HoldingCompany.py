from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HoldingCompany(Base):
    __tablename__ = 'tb_holdingcompanies'

    n_HoldingCompanyId_PK = Column(Integer, primary_key=True)
    s_HoldingCompanyCode = Column(String(50), nullable=True)
    s_HoldingCompanyName = Column(String(255), nullable=True)
    n_Personinfo_FK = Column(Integer, nullable=True)
    company_address = Column(Text, nullable=True)
    website_url = Column(String(500), nullable=True)
    logo_url = Column(String(500), nullable=True)
    phone_no = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True)
    naic_number = Column(Integer, nullable=True)
    metadad = Column(LONGTEXT, nullable=True)
    payment_wesite_url = Column(String(500), nullable=True)
    payment_mailling_address = Column(Text, nullable=True)
    payment_overnight_address = Column(Text, nullable=True)
    start_time = Column(String(50), nullable=True)
    end_time = Column(String(50), nullable=True)
    primary_color = Column(String(50), nullable=True)
    secondary_color = Column(String(50), nullable=True)
    n_CreatedUser = Column(Integer, nullable=True)
    d_CreatedDate = Column(DateTime, nullable=True)
    n_UpdatedUser = Column(Integer, nullable=True)
    d_UpdatedDate = Column(DateTime, nullable=True)
