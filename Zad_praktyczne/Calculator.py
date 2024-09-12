def removeSpace():
    j = -1
    for i in operation:
        j +=1
        if i == " ":
            operation.pop(j)

def change_to_previosu():
    j = -1
    for i in operation:
        j +=1
        if i == "_":
            operation[j] = int(previous_result)

def add(resault, i):
    return resault + int(operation [i+1])

def sub(resault, i):
    return resault - int(operation [i+1])

def mul(resault, i):
    return resault * int(operation [i+1])

def div(resault, i):
    return resault / int(operation [i+1])

def agg(resault, i):
    return resault ** int(operation [i+1])

previous_result = 0
while(True):

    print("Type operation")
    operation = input("")
    if operation == "exit":
        break

    operation = list(operation)
    removeSpace()
    change_to_previosu()
    resault = int(operation[0])
    
    i = -1
    for char in operation:
        i +=1
        if char == "+":
            resault = add(resault, i)
        if char == "-":
            resault = sub(resault, i)
        if char == "*":
            resault = mul(resault, i)
        if char == "/":
            resault = div(resault, i)
        if char == "^":
            resault = agg(resault, i)

    previous_result = resault 
    print("Result is: " + str(resault))