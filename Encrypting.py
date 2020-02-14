import random 


string = str(input("Enter: "))
r = ["1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","_","=","+","`","~","/","?","<",">",".",","]
result = []
num = [1,2,3,4,5,6,7,8,9]
for i in string:
    ranum = random.choice(num)
    for l in range(ranum):
        ran = random.choice(r)
        result.append(ran)
    result.append(i)
    ranum = random.choice(num)
    for o in range(ranum):
        ran = random.choice(r)
        result.append(ran)


res = result[::-1]
t = ''.join(res)
print(t)

    