import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


def price_to_float(inp):
    for i in inp:
        yield float(re.sub(',', '', i[1::]))

def count_vowels(inp):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in inp:
        print(i)
        if i in vowels:
            count += 1
    print(count)
    return str(count)

def fruits_pandas():
    vowels = ['a', 'e', 'i', 'o', 'u']
    fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
    print('<<<<<<<<<<<<<<<>>>>>>>>>>')
    print(fruits)
    print(fruits.describe())
    print(fruits.unique())
    print(fruits.value_counts())
    print(fruits.value_counts().idxmax())
    print(fruits.value_counts().idxmin())
    print(fruits.max())
    print(fruits[fruits.str.len() > 4])
    print(fruits.str.capitalize())
    print(sum(fruits.str.count('a')))
    #print(fruits.apply(count_vowels(fruits)))
    print(fruits[fruits.apply(lambda x : x.count('o') > 1)])
    print(fruits[fruits.str.contains('berry')])
    print(fruits[fruits.str.contains('apple')])
    #print(fruits[fruits.apply(count_vowels(fruits))])

def prices_pandas():
    prices = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
    prices = pd.Series([price for price in price_to_float(prices)])
    print(prices)
    print(prices.max())
    print(prices.min())
    print(pd.cut(prices, 4))
    plt.hist(prices, 4)
    plt.show()


def scores_pandas():
    scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
    print(scores)
    print(max(scores))
    print(min(scores))
    plt.hist(scores, 4)
    plt.show()
    print(scores + (100 - max(scores)))


def letters_pandas():
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
    print(letters)
    print(letters.value_counts().head(1))
    print(letters.value_counts().tail(1))
    num_of_vowels = sum(letters.isin(vowels))
    print(num_of_vowels)
    print(len(letters))
    print(len(letters) - num_of_vowels)
    print(letters.str.capitalize())
    index = letters.value_counts().head(6)
    index = index.index
    plt.bar(index, letters.value_counts().head(6))
    plt.show()
    



