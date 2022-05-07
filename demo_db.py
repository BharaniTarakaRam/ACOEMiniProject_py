def calc_add(a,b):
    return a+b

def calc_mul(a,b):
    return a*b
def calc_sub(a,b):
    return a-b
def calc_div(a,b):
    return a/b

def clac_squ(a):
    return a*a

def ur_name(str):
    return str


def num(num):
    return num

def evennumber(a):
    return a


def oddnumber(a):
    return a

def eve_num(a):
    if a%2==0:
        print(a,"the number is even")
    else:
        print(a,"the number is odd")


def prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")


