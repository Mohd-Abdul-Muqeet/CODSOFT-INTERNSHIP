import string
import random
n=int(input("Enter the Length of the password: "))
try:
    if(n<4):
        print("Please enter the Paaword length more than or eaual to 4")
except:
    ValueError

while True:
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits
    all_char=lower+upper+digits
    password="".join(random.choices(all_char,k=n))
    