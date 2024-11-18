from models import GroupingData

tenant_data = [
    GroupingData.GroupingData(name="Tenant 1", type="tenant", quotes=100, quoteNB=90, quoteConversion=90.0,
                              quoteNBPremium=50000,
                              averageNBPremium=550, pif=80, expiredPolicies=10, expiredPremium=10000, retention=85.5),
    GroupingData.GroupingData(name="Tenant 2", type="tenant", quotes=120, quoteNB=110, quoteConversion=91.6,
                              quoteNBPremium=60000,
                              averageNBPremium=600, pif=100, expiredPolicies=5, expiredPremium=8000, retention=87.3),
    GroupingData.GroupingData(name="Tenant 3", type="tenant", quotes=80, quoteNB=75, quoteConversion=93.8,
                              quoteNBPremium=40000,
                              averageNBPremium=533, pif=65, expiredPolicies=8, expiredPremium=5000, retention=82.4),
]

agent_data = [
    GroupingData.GroupingData(name="Agent 1", type="agent", quotes=150, quoteNB=120, quoteConversion=80.5,
                              quoteNBPremium=55000,
                              averageNBPremium=458.33, pif=80, expiredPolicies=0, expiredPremium=0, retention=80.5),
    GroupingData.GroupingData(name="Agent 2", type="agent", quotes=170, quoteNB=145, quoteConversion=85.2,
                              quoteNBPremium=62000,
                              averageNBPremium=427.59, pif=100, expiredPolicies=0, expiredPremium=0, retention=85.2),
    GroupingData.GroupingData(name="Agent 3", type="agent", quotes=130, quoteNB=103, quoteConversion=78.9,
                              quoteNBPremium=48000,
                              averageNBPremium=465.05, pif=70, expiredPolicies=0, expiredPremium=0, retention=78.9),
]

state_data = [
    GroupingData.GroupingData(name="TX", type="state", quotes=120, quoteNB=100, quoteConversion=83.3,
                              quoteNBPremium=5000,
                              averageNBPremium=50, pif=80, expiredPolicies=10, expiredPremium=500, retention=90.0),
    GroupingData.GroupingData(name="FL", type="state", quotes=110, quoteNB=95, quoteConversion=86.4,
                              quoteNBPremium=4800,
                              averageNBPremium=50.53, pif=78, expiredPolicies=8, expiredPremium=400, retention=91.2),
    GroupingData.GroupingData(name="NY", type="state", quotes=150, quoteNB=120, quoteConversion=80.0,
                              quoteNBPremium=6000,
                              averageNBPremium=50.0, pif=100, expiredPolicies=15, expiredPremium=600, retention=85.5),
    GroupingData.GroupingData(name="GA", type="state", quotes=90, quoteNB=85, quoteConversion=94.4, quoteNBPremium=4500,
                              averageNBPremium=52.94, pif=70, expiredPolicies=5, expiredPremium=300, retention=92.5)
]
