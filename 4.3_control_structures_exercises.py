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
    list_long = [i for i in range(1, length + 1)]
    



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

def print_num():
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
    while True:
        try:
            inp = int(input('What number would you like to go up to? >> '))
            end_num = inp
        except:
            print('Not valid as integer')
        isfirst = True
        while True:
            while isfirst == False:
                command = input('Continue?([Y]/[N]) >> ')
                if command == 'N':
                    return
                if command == 'Y':
                    start_num += inp
                    end_num += inp
                    break
                else:
                    print('Not Valid Command')
            isfirst = True
            print('Number |  Squared  | Cubed')
            print('--------------------------')
            for i in range(start_num, end_num + 1):
                square = i ** 2
                cube = i ** 3
                print(' {}    |    {}     |  {}'.format(i, square, cube))



