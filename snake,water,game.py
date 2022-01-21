# import random


# def gameWin(comp, you):
#     if comp == you:
#         return None
#     elif comp == 's':
#         if you == 'w':
#             return False
#         elif you == 'g':
#             return True
#     elif comp == 'w':
#         if you == 'g':
#             return False
#         elif you == 's':
#             return True
#     elif comp == 'g':
#         if you == 's':
#             return False
#         elif you == 'w':
#             return True


# print("Comp turn: Snake(s) water(w) or gun(g)?")
# randNo = random.randint(1, 3)

# if randNo == 1:
#     comp = 's'
# elif randNo == 2:
#     comp = 'w'
# elif randNo == 3:
#     comp = 'g'

# you = input("your turn: Snake(s) water(w) or gun(g)?")
# a = gameWin(comp, you)
# print(f"Computer chose {comp} ")
# print(f"You chose {you}")
# if a == None:
#     print(" The game is tie!")
# elif a:
#     print(" you Win!")
# else:
#     print(" You Lose!")


def function(a, b):
    """This is a function will calculate the average of two number"""
    average = (a+b)/2
    print(average)
    return average


v = function(2, 3)
print(v)
print(function.__doc__)


def Multiplication(a, b):
    """This function shows the multiplication of two number"""
    multiply = a*b
    # print(multiply)
    return multiply


v = Multiplication(4, 5)
print(v)
print(Multiplication.__doc__)


def Dividation(a, b):
    """This function shows that dividation of two number"""
    divide = a/b
    # print(divide)
    return divide


v = Dividation(30, 5)
print(v)
print(Dividation.__doc__)
