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

df_new = df.loc[df['국'] > 5, ['영','화']]

print(df_new)