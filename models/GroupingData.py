from pydantic import BaseModel
from typing import Optional

class GroupingData(BaseModel):
    name: str
    type:  Optional[str] = None
    quotes: int
    quoteNB: int
    quoteConversion: float
    quoteNBPremium: float
    averageNBPremium: float
    pif: int
    expiredPolicies: int
    expiredPremium: float
    retention: float
