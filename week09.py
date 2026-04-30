import numpy as np
import pandas as pd

aee2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
)
# df_2dlist = pd.DataFrame(arr2d, columns=['국', '영', '수'], index=[1, 2, 3])

# Creating DataFr

df_2dict = pd.DataFrame(aee2d, columns=['국', '영','수'], index=[1, 2, 3])
df_dict = pd.DataFrame(data={'국':[1, 2, 3], '영':[6, 4, 5], '수':[7, 8, 9]}, index=[1, 2, 3])
print(aee2d)
print(df_2dict)
print(df_dict)