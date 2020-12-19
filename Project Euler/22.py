'''
https://projecteuler.net/problem=22
'''


import pandas as pd


target_url = 'https://projecteuler.net/project/resources/p022_names.txt'


def str_value(mystring):
    x = 0
    for i in mystring:
        x += (ord(i)-64)

    return x


df = pd.read_csv(target_url,
                 engine='python', header=None)
df = df.T
df = df.sort_values(by=0)
df = df.dropna()
df = df.reset_index(drop=True)
df.index += 1

df['word_value'] = df[0].apply(lambda row: str_value(row))
df['pos_value'] = df.index
df['total_value'] = df.apply(
    lambda row: row['word_value'] + row['pos_value'], axis=1)
print(df['total_value'].sum())
