'''
https://projecteuler.net/problem=22
'''

import urllib.request
import pandas as pd

target_url = 'https://projecteuler.net/project/resources/p022_names.txt'


def str_value(mystring):
    x = 0
    for i in mystring:
        x += (ord(i)-64)

    return x


data = urllib.request.urlopen(target_url)
data = data.read()
data = data.decode('utf-8')

names = data.split(",")
names = [i.replace('"', '') for i in names]
names.sort()


df = pd.DataFrame(names, columns=['name'])
df = df.reset_index(drop=True)
df.index += 1

df['word_value'] = df['name'].apply(lambda row: str_value(row))
df['pos_value'] = df.index
df['total_value'] = df.apply(
    lambda row: row['word_value'] * row['pos_value'], axis=1)
print(df['total_value'].sum())
