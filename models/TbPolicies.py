from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TbPolicies(Base):
    __tablename__ = "tb_policies"
    n_PolicyNoId_PK = Column(Integer, primary_key=True)
    s_QuoteNumber = Column(String, nullable=True)
    d_BookingDate = Column(Date, nullable=True)
    n_CitizenTotalPremium = Column(Float, nullable=True)
    s_PolicyStatusCode = Column(String, nullable=True)
    d_InceptionDate = Column(Date, nullable=True)
    s_RenewalTypeCode = Column(String, nullable=True)
    agent_metadata = Column(String, nullable=True)
    s_IssueStateCode = Column(String, nullable=True)
    n_IssueCompanyID_FK = Column(Integer, nullable=True)
