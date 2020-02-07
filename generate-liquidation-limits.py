import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


def generate_liquidation_limits(cin7_df, start_date_string, end_date_string):
    liquidation_limits = pd.DataFrame(columns=['Cin7', 'Year', 'Month', 'Liquidation Limit'])
    iterator_date = datetime.strptime(start_date_string, '%Y.%m.%d.')
    end_date = datetime.strptime(end_date_string, '%Y.%m.%d.')

    while iterator_date < end_date:
        df = cin7_df[['Cin7']]
        df['Year'] = iterator_date.strftime('%Y')
        df['Month'] = iterator_date.strftime('%B')
        df['Liquidation Limit'] = 0.2
        liquidation_limits = liquidation_limits.append(df, ignore_index=True)
        iterator_date += relativedelta(months=1)

    return liquidation_limits
