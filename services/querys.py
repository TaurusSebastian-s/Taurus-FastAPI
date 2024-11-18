import pandas as pd
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.GroupingData import GroupingData
from models.TbPolicies import TbPolicies


async def get_tenant_data(session: AsyncSession):
    result = await session.execute(
        select(
            TbPolicies.s_QuoteNumber,
            TbPolicies.d_BookingDate,
            TbPolicies.n_CitizenTotalPremium,
            TbPolicies.s_PolicyStatusCode,
            TbPolicies.d_InceptionDate,
            TbPolicies.s_RenewalTypeCode
        )
    )

    df = pd.DataFrame(result.fetchall(), columns=[
        's_QuoteNumber', 'd_BookingDate', 'n_CitizenTotalPremium',
        's_PolicyStatusCode', 'd_InceptionDate', 's_RenewalTypeCode'
    ])

    df['quoteNB'] = df['d_BookingDate'].notna().astype(int)
    df['expiredPolicies'] = (df['d_InceptionDate'] < pd.to_datetime('today')).astype(int)
    df['pif'] = (df['s_PolicyStatusCode'] != 'CANCELLED').astype(int)
    df['retention'] = df['s_RenewalTypeCode'].notna().astype(int)

    result_df = df.groupby('s_QuoteNumber').agg(
        quotes=('s_QuoteNumber', 'nunique'),
        quoteNB=('quoteNB', 'sum'),
        quoteConversion=('quoteNB', lambda x: (x.sum() / x.notna().sum()) * 100),
        quoteNBPremium=('n_CitizenTotalPremium', 'sum'),
        averageNBPremium=('n_CitizenTotalPremium', 'mean'),
        pif=('pif', 'sum'),
        expiredPolicies=('expiredPolicies', 'sum'),
        expiredPremium=('n_CitizenTotalPremium', 'sum'),
        retention=('retention', lambda x: (x.sum() / x.notna().sum()) * 100)
    ).reset_index()

    return [GroupingData(**row.to_dict()) for _, row in result_df.iterrows()]


async def get_agent_data(session: AsyncSession):
    result = await session.execute(
        select(
            TbPolicies.agent_metadata,
            TbPolicies.s_QuoteNumber,
            TbPolicies.d_BookingDate,
            TbPolicies.n_CitizenTotalPremium,
            TbPolicies.s_PolicyStatusCode,
            TbPolicies.d_InceptionDate,
            TbPolicies.s_RenewalTypeCode
        )
    )

    df = pd.DataFrame(result.fetchall(), columns=[
        'name', 's_QuoteNumber', 'd_BookingDate', 'n_CitizenTotalPremium',
        's_PolicyStatusCode', 'd_InceptionDate', 's_RenewalTypeCode'
    ])

    # Calcular las métricas
    df['quoteNB'] = df['d_BookingDate'].notna().astype(int)
    df['expiredPolicies'] = (df['d_InceptionDate'] < pd.to_datetime('today')).astype(int)
    df['pif'] = (df['s_PolicyStatusCode'] != 'CANCELLED').astype(int)
    df['retention'] = df['s_RenewalTypeCode'].notna().astype(int)

    result_df = df.groupby('name').agg(
        quotes=('s_QuoteNumber', 'nunique'),
        quoteNB=('quoteNB', 'sum'),
        quoteConversion=('quoteNB', lambda x: (x.sum() / x.notna().sum()) * 100),
        quoteNBPremium=('n_CitizenTotalPremium', 'sum'),
        averageNBPremium=('n_CitizenTotalPremium', 'mean'),
        pif=('pif', 'sum'),
        expiredPolicies=('expiredPolicies', 'sum'),
        expiredPremium=('n_CitizenTotalPremium', 'sum'),
        retention=('retention', lambda x: (x.sum() / x.notna().sum()) * 100)
    ).reset_index()

    return [GroupingData(**row.to_dict()) for _, row in result_df.iterrows()]


async def get_state_data(session: AsyncSession):
    result = await session.execute(
        select(
            TbPolicies.s_IssueStateCode,
            TbPolicies.s_QuoteNumber,
            TbPolicies.d_BookingDate,
            TbPolicies.n_CitizenTotalPremium,
            TbPolicies.s_PolicyStatusCode,
            TbPolicies.d_InceptionDate,
            TbPolicies.s_RenewalTypeCode
        )
    )

    df = pd.DataFrame(result.fetchall(), columns=[
        'name', 's_QuoteNumber', 'd_BookingDate', 'n_CitizenTotalPremium',
        's_PolicyStatusCode', 'd_InceptionDate', 's_RenewalTypeCode'
    ])

    df['quoteNB'] = df['d_BookingDate'].notna().astype(int)
    df['expiredPolicies'] = (df['d_InceptionDate'] < pd.to_datetime('today')).astype(int)
    df['pif'] = (df['s_PolicyStatusCode'] != 'CANCELLED').astype(int)
    df['retention'] = df['s_RenewalTypeCode'].notna().astype(int)

    result_df = df.groupby('name').agg(
        quotes=('s_QuoteNumber', 'nunique'),
        quoteNB=('quoteNB', 'sum'),
        quoteConversion=('quoteNB', lambda x: (x.sum() / x.notna().sum()) * 100),
        quoteNBPremium=('n_CitizenTotalPremium', 'sum'),
        averageNBPremium=('n_CitizenTotalPremium', 'mean'),
        pif=('pif', 'sum'),
        expiredPolicies=('expiredPolicies', 'sum'),
        expiredPremium=('n_CitizenTotalPremium', 'sum'),
        retention=('retention', lambda x: (x.sum() / x.notna().sum()) * 100)
    ).reset_index()

    return [GroupingData(**row.to_dict()) for _, row in result_df.iterrows()]
