
#1. Написать функцию, которая будет принимать
# целое положительное число и возвращать True,
# если это число простое, иначе - False.
def primer (x) :
    if x % 2 == 0 :
        return False
    a = 3
    while a * a <= x and x % a != 0 :
        a +=2
    return a * a > x
print (primer(5412))



#2. На вход функции передается строка вида: "1 9 3 4 5 "
# необходимо вернуть максимальное и минимальное число из этой последовательности.
def numbers (array: str) -> tuple :
    list_char = array.split()
    list_num = list(map(int,list_char))
    return min(list_num) , max (list_num)
print (numbers("1 9 3 4 5"))




#3. Написать функцию, принимающую строку вида: "The sunset sets at twelve o' clock."
# и возвращающую строку: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
# где каждое число это порядковый номер буквы в алфавите.
# Например при передаче строки: "abc" должно вернуться "1 2 3". *Без учета регистра.
import string
from functools import reduce
print (string.ascii_lowercase)
def alphabet (array : str) -> str :
    numbers = [string.ascii_lowercase.index(char.lower()) + 1 for char in array
              if char.lower() in string.ascii_lowercase]
    output = reduce(lambda x, y:  f"{x}{y}", numbers)
    return output
print (alphabet("The sunset sets at twelve o' clock"))