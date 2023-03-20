l = int(input())
valueStack = [0]
multStack = []
for _ in range(l):
    command = input().split()
    if command[0] == 'for':
        valueStack.append(0)
        multStack.append(int(command[1]))
    elif command[0] == 'add':
        valueStack[-1]+=1
    elif command[0] == 'end':
        m = multStack.pop()
        v = valueStack.pop()
        valueStack[-1]+=m*v
value = valueStack[0]
ov = 2**32-1
if value>ov:
    print('OVERFLOW!!!')
else:
    print(value)
