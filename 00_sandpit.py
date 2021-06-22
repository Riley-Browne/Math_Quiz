import random

operartion = "/"

num_1 = random.randint(1, 12)
num_2 = random.randint(1, 12)

if operartion == "/":
    num_3 = num_2 * num_1
    
    question = "{} {} {}".format(num_3, operartion, num_2)
else:
    question = "{} {} {}".format(num_1, operartion, num_2)

answer = eval(question)
answer =  int(answer)

print(question)
print(answer)