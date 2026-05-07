import pandas as pd

df = pd.DataFrame(
    data={
        '국': [1, 6, 7],
        '영': [2, 4, 8],
        '수': [3, 5, 9],
        '화': [10, 3, 11]
    },
    index=[1, 2, 3]
)
print(df)
#print(df.describe())
# print(df.info())
# print(df['국'].value_counts() )
# print(df.shape)
# print(df['국'].nunique())
# print(df.dtypes)
