import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydataset




def iris_s():
    iris = pydataset.data('iris')
    print(iris)
    sns.despine(left=True)
    sns.barplot(data = iris, x = 'Species', y = 'Petal.Length')
    sns.lineplot(data = iris, x = 'Petal.Length', y = 'Petal.Width')
    sns.lmplot(data = iris, x = 'Sepal.Length', y = 'Sepal.Width', hue = 'Species')
    sns.scatterplot(data = iris, x = 'Petal.Length', y = 'Petal.Width', hue = 'Species')

    plt.show()

iris_s()




def anscombe_s():
    ans = sns.load_dataset('anscombe')
    ans = ans.groupby('dataset').describe()
    print(ans)






#def insects_s():
 #   insect = sns.load_dataset('InsectSprays')
  #  print(insect)


def swiss_s():
    swiss = pydataset.data('swiss')
    swiss['is_catholic'] = swiss['Catholic'] >= 60
    print(swiss)
    sns.lmplot(data = swiss, x = 'Fertility', y = 'Infant.Mortality')
    plt.show()

swiss_s()



  

def sleep_s():
    sleep = pydataset.data('sleepstudy')
    print(sleep)
    sns.barplot(data=sleep, x = 'Days', y = 'Reaction', hue = 'Subject')
    #sns.lineplot(data = sleep, x = 'Days', y = 'Reaction', hue = 'Subject')
    plt.show()

anscombe_s()
