import random
password="ABCEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*(){}?/"
length=int(input("Enter the size of password: "))
a="".join(random.sample(password,length))
print("your password is:" ,a)