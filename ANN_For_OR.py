import random

X= [1,1,0,0]
Y = [1,0,1,0]

outputs = [1,1,1,0]


def ann(X,Y,outputs):
    w1 = random.random()
    w2 = random.random()
    w0 = random.random()
    learning_rate = 0.001
    bias = 1
    errorcheck = False
    while(errorcheck):
        for i in range(4):
            calculated = X[i] * w1 + Y[i] * w2 + bias * w0
            error = calculated - outputs[i]
            w1 =(learning_rate * error * X[i]) + w1
            w2 =(learning_rate * error * Y[i]) + w2
            if (error == 0):
                errorcheck == True
    return w1, w2
def userinput():
    while True:
        try:
            value1 = int(input("Please enter true[1] or false[0] for value 1: "))
            if value1 not in range(0,2):
                raise ValueError
            else:
                 break
        except ValueError:
            print("Invalid input. Please enter either true[1] or false[0]: ")
    while True:
        try:
            value2 = int(input("Please enter true[1] or false[0] for value 2: "))
            if value2 not in range(0,2):
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid input. Please enter either true[1] or false[0]: ")
        
            
    return float(value1), float(value2)
def anncheck(w1,w2,value1,value2):
    check = value1 * w1 + value2 * w2

    if (check <= 0.00):
        print (False)
    else:
        print(True)
    
x,y = ann(X,Y,outputs)
value1,value2 = userinput()
anncheck(x,y,value1,value2)
