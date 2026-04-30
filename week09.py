from os import rename

import numpy as np
import pandas as pd

df = pd.DataFrame(data={'국':[1, 2, 3], '영':[6, 4, 5], '수':[7, 8, 9]}, index=[1, 2, 3])
print(df)

df_new = (
    pd.melt(df)
    .rename(columns={
        'variable': 'var',
        'value': 'val'
    })
    .query('val >= 5')
)

print(df_new)