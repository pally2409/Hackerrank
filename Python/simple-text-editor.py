s = ""
operation_stack = []
n = int(input())

for i in range(n):
    opr = input().strip().split(' ')
    if opr[0] == '1':
        operation_stack.append('1 ' + str(len(opr[1])))
        s += opr[1]
    elif opr[0] == '2':
        operation_stack.append('2 ' + s[(-1)*int(opr[1]):])
        s = s[:(-1)*int(opr[1])]
    elif opr[0] == '3':
        print(s[int(opr[1])-1])
    elif opr[0] == '4':
        popped = operation_stack.pop()
        popopr = popped.split(' ')
        if popopr[0] == '1':
            s = s[:(-1)*int(popopr[1])]
        elif popopr[0] == '2':
            s += popopr[1]

