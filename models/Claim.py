from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, DateTime, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Claim(Base):
    __tablename__ = 'tb_claims'

    ClaimId_PK = Column(Integer, primary_key=True)
    Claim_No = Column(String(50), nullable=True)
    Risk_Id = Column(Integer, nullable=True)
    n_TermMaster_FK = Column(Integer, nullable=True)
    n_potransaction_FK = Column(Integer, nullable=True)
    Policy_No_SimpleSolve = Column(String(50), nullable=True)
    n_PolicyNoId_FK = Column(Integer, ForeignKey('tb_policies.n_PolicyNoId_PK'), nullable=True)
    n_PORiskMasterFK = Column(Integer, nullable=True)
    Date_Of_Loss = Column(Date, nullable=True)
    Insured_Name = Column(String(255), nullable=True)
    n_InsuredPersonInfoId_FK = Column(Integer, nullable=True)
    Agency_Name = Column(String(255), nullable=True)
    n_AgencyPersoninfoId_FK = Column(Integer, nullable=True)
    n_AgencyAccount_FK = Column(Integer, nullable=True)
    n_SubAgentPersoninfo_FK = Column(Integer, nullable=True)
    Reported_By_PersonId_FK = Column(Integer, nullable=True)
    InHouseCounsel_Person_FK = Column(Integer, nullable=True)
    Reported_By_PersonId_FK_Old = Column(Integer, nullable=True)
    PA_PersonId_FK = Column(Integer, nullable=True)
    Reported_By_Deprecated = Column(String(255), nullable=True)
    Reported_By_Relation_Code = Column(String(50), nullable=True)
    ClaimTypeId_FK = Column(Integer, nullable=True)
    Loss_Type_Code = Column(String(50), nullable=True)
    Amount_Claimed = Column(Integer, nullable=True)
    Letter_URL_Path = Column(String(255), nullable=True)
    Remarks = Column(Text, nullable=True)
    Allocated_To_UserId_FK = Column(Integer, ForeignKey('tb_users.UserId_PK_CMS'), nullable=True)
    Date_Allocated = Column(DateTime, nullable=True)
    Date_First_Visited = Column(DateTime, nullable=True)
    Service_Repre_UserId_FK = Column(Integer, ForeignKey('tb_users.UserId_PK_CMS'), nullable=True)
    Approval_Status_Code = Column(String(50), nullable=True)
    Claim_Approved_UserId_FK = Column(Integer, ForeignKey('tb_users.UserId_PK_CMS'), nullable=True)
    Comment = Column(Text, nullable=True)
    Claim_Status_Code = Column(String(50), nullable=True)
    Claim_SubStatus_Code = Column(String(50), nullable=True)
    Date_Close = Column(Date, nullable=True)
    Total_Paid_Amount = Column(Integer, nullable=True)
    Total_Paid_Amt_New = Column(Integer, nullable=True)
    Attorney_Involved_YN = Column(Integer, nullable=True)
    PA_Involved_YN = Column(Integer, nullable=True)
    DFS_Complain_YN = Column(Integer, nullable=True)
    Catastrophe_YN = Column(Integer, nullable=True)
    Event_Name = Column(String(255), nullable=True)
    Data_Source = Column(String(255), nullable=True)
    n_PrimaryAttorneyPersonId_FK = Column(Integer, nullable=True)
    d_PrimaryAttoryAssignDate = Column(DateTime, nullable=True)
    n_CoAttorneyPersonId_FK = Column(Integer, nullable=True)
    d_CoAttoryAssignDate = Column(DateTime, nullable=True)
    n_Copytoclientfk = Column(Integer, nullable=True)
    s_CountyCode = Column(String(50), nullable=True)
    Inserted_UserId_FK = Column(Integer, nullable=True)
    Inserted_Date = Column(DateTime, nullable=True)
    Updated_UserId_FK = Column(Integer, nullable=True)
    Updated_Date = Column(DateTime, nullable=True)
    metadata = Column(LONGTEXT, nullable=True)


class ClaimChecklist(Base):
    __tablename__ = 'tb_claims_checklist'

    id = Column(Integer, primary_key=True)
    task_title = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    sequence_number = Column(Integer, nullable=True)
    is_active = Column(Enum('YES', 'NO'), nullable=True)
    created_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_by = Column(Integer, nullable=True)
    updated_at = Column(DateTime, nullable=True)


class ClaimChecklistResponse(Base):
    __tablename__ = 'tb_claim_checklist_responses'

    id = Column(Integer, primary_key=True)
    checklist_task_id = Column(Integer, ForeignKey('tb_claims_checklist.id'), nullable=True)
    claim_id = Column(Integer, ForeignKey('tb_claims.ClaimId_PK'), nullable=True)
    due_date = Column(Date, nullable=True)
    checklist_owner_id = Column(Integer, nullable=True)
    is_task_completed = Column(Enum('Y', 'N'), nullable=True)
    short_notes = Column(Text, nullable=True)
    system_assign = Column(Enum('Y', 'N'), nullable=True)
    created_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_by = Column(Integer, nullable=True)
    updated_at = Column(DateTime, nullable=True)
