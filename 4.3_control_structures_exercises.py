def day_of_week(inp):
    if inp == 'Monday':
        return 'That is a Monday'
    if inp != 'Monday':
        return 'That is not a Monday'
    if inp == 'Saturday' or inp == 'Sunday':
        return 'That is a weekday'



day_of_week('Monday')



def hours_worked(hours, pay):
    if hours < 40:
        return pay * hours
    time_half = (pay * .5) * (hours - 40)
    return pay * hours + time_half

a = hours_worked(45, 10)
print(a)
b = input('!')


i = 5
while True:
    if i > 15:
        break
    print(i)
    i += 1

i = 0
while True:
    if i == 100:
        break
    i += 2
    print(i)
    
i = 100
while True:
    if i == -10:
        break
    print(i)
    i -= 5

i = 2
while True:
    if i > 10000000:
        break
    print(i)
    i = i ** 2

i = 100
while True:
    if i == 5:
        break
    print(i)
    i -= 5

i = 2
while True:
    if i > 10000000:
        break
    print(i)
    i = i ** 2

def ten_multi(inp):
    total_calc = []
    try:
        for i in range(1, 10):
            answer = inp * i
            print(str(inp) + ' X ' + str(i) + ' = ' + str(answer))
            total_calc.append(answer)
        return total_calc
    except:
        return 'error'
    
def repeating_numbers(length):
    num_count = 1
    for i in range(length + 1):
        num_list = []
        for i in range(num_count):
            num_list.append(str(num_count))
        print(''.join(num_list))
        num_count += 1


def positive_ip(inp):
    try:
        inp = int(inp)
    except:
        print('error code 1: Not valid number')
        return
    for i in range(0, inp + 1):
        print(str(i))
    
  
def positive_down(inp):
    try:
        inp = int(inp)
    except:
        print('error code 1: Not valid number')
        return
    for i in range(inp, 0, -1):
        print(str(i))
    

def skipdigit():
    inp = input('Pick a number>> ')
    try:
        inp = int(inp)
        if inp % 2 != 0 and inp != 1:
            return  'Not an even number'
    except:
        return 'Not a valid Number'
    for i in range(1, 51):
        if i == inp and (inp % 2) == 0:
            continue
        if i != inp and (inp % 2) == 1:
            print(str(i))

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            continue
        if i % 3 == 0:
            print('Fizz')
        if i % 5 == 0:
            print('Buzz')
        else:
            print(str(i))




def table_of_powers():
    start_num = 1
    try:
        inp = int(input('What Number do you want to go to? >> '))
    except:
        print('error code 1: Not a number')
        return
    end_num = start_num + inp
    isfirst = True
    while True:
        if isfirst == False:
            continuee = input('Continue? >> ')
            if continuee == 'Y':
                start_num += inp
                end_num += inp
            if continuee == 'N':
                return
        for i in range(start_num, end_num):
            square = i ** 2
            cube = i ** 2
            print(' {}    |    {}     |  {}'.format(i, square, cube))
        isfirst = False
            
  