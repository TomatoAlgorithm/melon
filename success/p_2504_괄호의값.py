import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    stack = []
    statement = input()
    res = 0
    
    for s in statement:
        tmp = ''
        if(s == '('):
            if(len(stack) == 0):
                stack.append(s)
            elif(stack[-1] == '(' or stack[-1] == '['):
                stack.append("*")
                stack.append(s)
            elif(stack[-1] == ')' or stack[-1] == ']'):
                return 0
            else:
                stack.append("+")
                stack.append(s)
        elif(s=='['):
            if(len(stack) == 0):
                stack.append(s)
            elif(stack[-1] == '(' or stack[-1] == '['):
                stack.append("*")
                stack.append(s)
            elif(stack[-1] == ')' or stack[-1] == ']'):
                return 0
            else:
                stack.append("+")
                stack.append(s)
        elif(s == ')'):
            if(stack.count('(') == 0):
                return 0
            if(stack[-1] == '('):
                stack.pop()
                stack.append(2)
            else:
                while(len(stack) > 0):
                    elem = stack.pop()
                    if(elem == '('):
                        tmp+='2'
                        try:
                            stack.append(eval(tmp))
                        except:
                            return 0
                        break
                    elif(elem == '+'):
                        tmp+=str(elem)
                        tmp+=str(stack.pop())
                        try:
                            tmp = str(eval(tmp))
                        except:
                            return 0
                    else:
                        tmp+=str(elem)
        elif(s == ']'):
            if(stack.count('[') == 0):
                return 0
            if(stack[-1] == '['):
                stack.pop()
                stack.append(3)
            else:
                while(len(stack) > 0):
                    elem = stack.pop()
                    if(elem == '['):
                        tmp+='3'
                        try:
                            stack.append(eval(tmp))
                        except:
                            return 0
                        break
                    elif(elem == '+'):
                        tmp +=str(elem)
                        tmp +=str(stack.pop())
                        try:
                            tmp = str(eval(tmp))
                        except:
                            return 0
                    else:
                        tmp+=str(elem)
                     
    tmp=''
    for s in stack:
        tmp+=str(s)
    try:
        return eval(tmp)
    except:
        return 0

print(solution())