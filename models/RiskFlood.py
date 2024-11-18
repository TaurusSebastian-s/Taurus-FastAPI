from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RiskAdditionalFloodInfo(Base):
    __tablename__ = 'tb_poriskadditionalfloodinfos'

    PORiskMasterId_PK = Column(Integer, primary_key=True)
    n_PolicyId_FK = Column(Integer, nullable=True)
    n_RiskId_FK = Column(Integer, nullable=True)
    FloodRiskLevel = Column(String(50), nullable=True)
    metadata = Column(LONGTEXT, nullable=True)
