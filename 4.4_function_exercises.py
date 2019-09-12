import re

def is_two(inp):
    if inp == 2 or inp == '2':
        return True
    return False

def is_vowel(inp):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if inp == 'vowel_list':      # for remove_vowles_function
        return vowels        
    if inp in vowels:
        return True
    return False


def is_consonant(inp):
    if is_vowel(inp) == False:
        return True
    return False

def string_word(inp):
    if is_consonant(inp[0]) == True:
        return inp.capitalize()
    return inp



calculate_tip = lambda amount, percentage : (amount / 100) * (percentage * 100)

apply_discount = lambda amount, discount : amount - (amount / 100) * (discount * 100)

handle_commas = lambda inp : re.sub(',', '', inp)

def get_letter_grade(inp):
    if inp > 89:
        return 'A'
    if inp < 90 and inp > 79:
        return 'B'
    if inp < 80 and inp > 69:
        return 'C'
    if inp < 70 and inp > 59:
        return 'D'
    return 'F'

def remove_vowles(inp):
    vowels = is_vowel('vowel_list')
    for i in inp:
        if i in vowels:
            inp =  re.sub(i, '', inp)
    return inp

def normalize_name(inp):
    syntax_check = ["%", "/", "\n", "\r"]
    for i in inp:
        if i in syntax_check:
            inp = re.sub(i, '', inp)
    return re.sub(' ', '_', inp.strip()).lower()


def cum_sum(inp):
    new_list = []
    check_val = 0
    for i in inp:
        new_list.append(i + check_val)
        check_val += i
    return new_list


def twelveto24(inp):
    check = ['a', 'm', 'p', ':']
    new_inp = inp
    for i in inp:
        if i in check:
            new_inp = re.sub(i, '', new_inp)
    new_inp = int(new_inp)
    if inp[5] == 'p' or inp[4] == 'p':
        new_inp += 1200
    return str(new_inp)

print(twelveto24('06:45pm'))