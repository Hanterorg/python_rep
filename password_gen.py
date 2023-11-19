import random

simbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
a = 1
while a>0:
    len = int(input('Введите длинну пароля:'))
    pas = ''
    for i in range(len):
        sim = random.choice(simbols)
        pas+= sim
    print(pas)
