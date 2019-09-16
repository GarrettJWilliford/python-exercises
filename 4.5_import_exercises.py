from functions_exercises import cum_sum, string_word, normalize_name
import functions_exercises
import itertools
import json
import re





print(len(list(itertools.product([1, 2, 3], ['A', 'B', 'C']))))

print(len(list(itertools.permutations('abcd', 2))))

users = json.load(open('profiles.json', 'rb'))


print(len(users))

a = 0
for i in range(len(users)):
    if users[i]['isActive'] == True:
        a += 1
print(a)

print([users[i]['isActive'] if users[i]['isActive'] == True for i in range(len(users))])

a = 0
for i in range(len(users)):
    if users[i]['isActive'] == False:
        a += 1
print(a)




def remove_extra(inp):
    for i in inp:
        inp = functions_exercises.handle_commas(inp)
        return re.sub(r"[^\w]", '', inp)

def return_list_extra(inp):
    for i in inp:
        i = remove_extra(i)
        yield i

def add_decimal(inp):
    inp = list(inp)[::-1]
    inp.insert(2, '.')
    ''.join(inp[::-1])
    return ''.join(inp[::-1])


a = 0
for i in range(len(users)):
    a += int(remove_extra(users[i]['balance']))
average_hold = a
grand_sum = add_decimal(str(a))
print(grand_sum)

avg  = int(average_hold / len(users))
print(add_decimal(str(avg)))



balance_list = [int(i) for i in return_list_extra([users[i]['balance'] \
    for i in range(len(users))])]
print(add_decimal(str(min(balance_list))))
print(add_decimal(str(max(balance_list))))


print([max(users[i]['favoriteFruit'] for i in range(len(users)))])

print([min(users[i]['favoriteFruit'] for i in range(len(users)))])


print(sum([int(users[i]['greeting'][::-1][17:19][::-1]) for i in range(len(users))]))