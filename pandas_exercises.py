import pandas as pd
import numpy as np
import pickle
import itertools
import threading
#from ethropic_encryption import *
#from dbtools import *
import getpass
import MySQLdb
import pandas.io.sql as psql


#pandas_exercises is at the bottom, these are extra modules I created and implemeted
#Sorry for being extra
#I tried to stack these and everything broke

##########################################################
##########################################################
#ethropic_encryption
#used to enrypt username, password, and other password


def ebets(alph_num):
    alph_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890)(*&^%$#@!~`-=_+][{}\\|:;/.,<>?"
    alphs = [alph_1]
    return alphs[alph_num]


#working on this
def scramble_encryption(a):
    return_alph = []
    for i in range(10):
        alph = list(a)
        for i in range(len(alph)):
            char = random.choice(alph)
            return_alph.append(char)
            alph.remove(char)
    return ''.join(return_alph)
 

def e_1(key, inp):
    key = list(map(int, str(key)))
    inp = re.sub(' ', '_', inp)
    bird_word = []
    final_word = []
    alph = ebets(key[0])
    for i in inp:
        index = alph.index(i)
        if index == 91:
            i = alph[0 + key[1]]
        if index == 91:
            i = alph[0 + (key[1] - 1)]
        else:
            i = alph[index + key[1]]
        bird_word.append(i)
    bird_word = ''.join(bird_word)
    for i in range(10):
        fake_news = []
        for ii in range(random.randint(2, (len(inp) + random.randint(0, len(inp))))):
            fake_news.append(random.choice(alph))
        if key[2] == i:
            final_word.append(bird_word)
        else:
            final_word.append(''.join(fake_news))
    return ' '.join(final_word)



def d_1(key, inp):
    key = list(map(int, str(key)))
    inp = inp.split()
    bird_word = []
    alph = ebets(key[0])
    for i in inp[key[2]]:
        index = alph.index(i)
        if index == 0:
            i = alph[91 - key[1]]
        if index == 1:
            i = alph[91 - (key[1] + 1)]
        else:
            i = alph[index - key[1]]
        bird_word.append(i)
    return ''.join(bird_word)
        






##########################################################
##########################################################
#dbtools
#allows you to run sql queries and return subsets of data
#password reset everytime requiring a one time login
#may need to make some pickle save files with encryption to initialize this module

pickle.dump('!!!!!', open('userlogin.p', 'wb'))



def init_login():
    key = getpass.getpass(prompt = '>>ENCRYPTION_KEY>> ')
    inp = getpass.getpass(prompt = '>>ENTER_PASSWORD>> ')
    if inp != e.d_1(key, pickle.load(open('passw0rd.p', 'rb'))):
        return '<<!INVALID_PASSWORD!>>'
    pickle.dump(key, open('userlogin.p', 'wb'))
    return '<<LOGIN_ACCEPTED>>'


def init_reset():
    key = getpass.getpass(prompt = '>>ENCRYPTION_KEY>> ')
    old_check = getpass.getpass(prompt = '>>ENTER_OLD_PASSWORD>> ')
    if old_check == e.d_1(key, pickle.load(open('passw0rd.p', 'rb'))):
        print('<<LOGIN_ACCEPTED>>')
        while True:
            print('<><><><><><><><><><><><><><>')
            command = input('<<[P]assword_reset / [C]ancel>> ')
            if command == 'P':
                new_check = input('>>ENTER_NEW_PASSWORD>>')
                are_you_sure = input('<<[Y]es / [N]o / [E]xit')
                if are_you_sure == 'Y':
                    pickle.dump(e.e_1(key, new_check), open('passw0rd.p', 'wb'))
            if command == 'C':
                return '<<EXIT_COMPLETE>>'
                
            

def get_db_url(database = 'employees', contin = True):
    pick = pickle.load(open('userlogin.p', 'rb'))
    if pick == '!!!!!':
        print('<<!LOGIN_REQUIRED!>>')
        return
    else:
        key = pick
    db=MySQLdb.connect(host='157.230.209.171', user=e.d_1(key, pickle.load(open('user.p', 'rb'))), \
                       passwd=e.d_1(key, pickle.load(open('sql_pass.p', 'rb'))), db=database)
    if contin == False:
        return db
    while True:
        try:
            command = input('>>ENTER_COMMAND>> ')
            if command == '/RETURN':
                return df
            if command == '/EXIT':
                db.close()
                return '<<EXIT COMPLETE>>'
            df = psql.read_sql(command, con=db)
            print(df)
        except:
            print('<<!ERROR!>>')

##########################################################
##########################################################
#pandas_exercises
    
def advanced_mpg():
    mpg = pickle.load(open('cars.p', 'rb'))
    print(mpg)
    mpg['average_milage'] = (mpg.hwy + mpg.cty) / 2
    mpg['is_auto'] = (mpg['trans'].str.contains('auto'))
    print(mpg)
    print(mpg.groupby('manufacturer')['average_milage'].mean())
    print('<<<<<>>>>>')
    print(len(mpg['manufacturer'].unique()))
    print(len(mpg['model'].unique()))
    print(mpg[['trans', 'is_auto']])
    mpg['is_auto'].replace({True : 'Automatic', False : 'Manual'}, inplace = True)
    print(mpg.groupby('is_auto')['average_milage'].mean())
    mpg.join(df1, df2, ['']).on
    
def advanced_joins():
    users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]})
    roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']})
    print(users)
    print(roles)
    join = pd.merge(users, roles, on='id', how='inner')
    print(join)



#head to dbtools to see all of it
def advanced_sqljoins():
    db = get_db_url(database = 'employees', contin = False)
    pd.read_sql('SELECT * FROM employees', db)



advanced_sqljoins()