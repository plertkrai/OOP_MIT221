

def getPID():
    pid = input('Enter your pid: ')  #str
    lpid = [int(x) for x in pid]
    return lpid # list

def getFortune(var):
    if var % 2 == 0:
        print('Your fortune is good')
    else:
        print('Your fortune is very good')

PID = getPID()
print(f'The data from user: {sum(PID)}')
print(f'The prediction result is: {getFortune(sum(PID))}')



print("Hello, MIT221")
