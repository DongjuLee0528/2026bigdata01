import pandas as pd

df = pd.DataFrame(
    data={
        '국': [1, 6, 7],
        '영': [2, 4, 8],
        '수': [3, 5, 9],
        '미세먼지': [10, 3, 11]
    },
    index=[1, 2, 3]
)
print(df)
df_new = df.drop(columns=['수', '미세먼지'])
print(df_new)