import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np



def hitormiss(inp):
    for i in inp:
        yield float(re.sub(',', '', i[1::]))
        

p = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", \
     "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", \
     "kiwi", "kiwi", "mango", "blueberry", "blackberry", \
     "gooseberry", "papaya"]

v = ['a', 'e', 'i', 'o', 'u']


print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>')
df = pd.Series(p)
print(df)
print(df.describe())
print(df.unique())
print(df.value_counts())
print(df.value_counts().head(1))
print(df.value_counts().tail(1))
print(df.max())
print([d for d in df if len(d) > 4])
print([d.capitalize() for d in df])
print(sum([d.count('a') for d in df]))
print([len([dd for dd in d if dd in v]) for d in df])
print([d for d in df.apply(lambda x :  x.count('o')) if d > 1])
print([d for d in df if 'berry' in d])
print([d for d in df if 'apple' in d])
###########################
print([d for d in df.apply(lambda x : (x, x.count('a')))])
print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>')
df = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
df = pd.Series(df)
print(df)
print(df.dtypes)
print(max([d for d in hitormiss(df)]))
print(min([d for d in hitormiss(df)]))
##print(pd.cut(hitormiss(df), 4))
#plt.hist([int(d) for d  in hitormiss(df)], bins = 20, alpha = .4)
#plt.show()

print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>')

df = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
df = df.sort_values()
print(df)
print(df.head(1))
print(df.tail(1))
print(sum(df) / len(df))
#plt.hist(df, bins = 20, alpha = .8, density = .5)
#plt.show()
df[df > 89] = 3
df[df > 79] = 2
df[df > 69] = 1
df[df > 59] = 0

print(df)

print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>')

df = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
print(df)
print(df.value_counts().head(1))
print(df.value_counts().tail(1))
print(sum(df.isin(v)))
print(len(df) - sum(df.isin(v)))
new_df = [d.upper() for d in df]
print(new_df)
plt.bar(range(1, 7), df.value_counts().head(6))
plt.show()