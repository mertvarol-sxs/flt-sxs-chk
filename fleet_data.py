import pandas as pd
from datetime import datetime

def initialize_fleet_data():
    data = {
        'Reg.': ['TC-ABC', 'TC-DEF', 'TC-GHI'],
        'Aircraft Type': ['B737-800NG', 'B737-8', 'A320neo'],
        'Aircraft Variant': ['', '', ''],
        'Date of Manufacture': [pd.Timestamp('2010-05-01'), pd.Timestamp('2018-07-01'), pd.Timestamp('2020-03-01')],
        'DOI': [pd.Timestamp('2010-06-01'), pd.Timestamp('2018-08-01'), pd.Timestamp('2020-04-01')],
        'DOE': [pd.NaT, pd.NaT, pd.NaT],
        'Lease Type': ['OWN', 'OPS', 'FIN'],
        'Lease End Date': [pd.NaT, pd.Timestamp('2028-08-01'), pd.NaT],
        'Market Value': [12000000, 18000000, 15000000],
        'Monthly Lease (OPS)': [None, 250000, None]
    }
    return pd.DataFrame(data)