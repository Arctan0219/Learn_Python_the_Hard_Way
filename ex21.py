def add(a, b):
    print('将%d加上%d' %(a, b))
    return(a + b)
    
def subtract(a, b):
    print('将%d减去%d' % (a, b))
    return(a - b)
    
def multiply(a, b):
    print('将%d和%d相乘' % (a, b))
    return(a * b)
    
def divide(a, b):
    print('%d除以%d' % (a, b))
    return(a / b)
    

print('使用这些函数做一些数学运算！')

age = add(30, 5)#35
height = subtract(78, 4)#74
weight = multiply(90, 2)#180
iq = divide(100, 2)#50

print('年龄：%d, 身高：%d, 体重：%d, IQ：%d' % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print('这是一个小题目')

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))#-4391

print('应该是：', what, '\n你能口算出来吗')