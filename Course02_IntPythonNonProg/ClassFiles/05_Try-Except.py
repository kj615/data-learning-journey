
print("before")

try:
    #4 / 0
    print(age)
except NameError as e:
    print("this was a name issue")
    print(e)
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e:
    print("Something went wrong")

class CheeseError(Exception):
    pass

# Define your own exception in a function
def upper_fun(word):
    if len(word) <= 0:
        raise CheeseError("The word has to have at least 1 letter!")
    return word.upper()

print(upper_fun("hello"))


print("after")


# Challenge
# Find something not mentioned that will throw
# an exception and put it in a try, except

list = "not a list"

try:
    list.append(1)
except AttributeError:
    print("there is an attribute issue")