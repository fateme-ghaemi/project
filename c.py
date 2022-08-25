import math
time=0
time=int(input('how much do you want to use the calculator?'))

for i in range(time):
    time-=1
    x=float(input('enter the first number:'))
    y=float(input('enter the second number:'))
    op=input('enter your operator:')
    
    if op=='+':
        z=x+y
    elif op=='-':
        z=x-y
    elif op=='*':
        z=x*y
    elif op=='/':
        z=x/y
    elif op=="**2":
        z=x**2
    elif op=='**':
        z=x**y
    elif op=='%':
        z=x%y
    elif op=='//':
        z=x//y
    elif op=='radical':
        radical=math.sqrt(x) 
        z=float(radical)
    elif op=='sin':
        sin=math.sin(x)
        z=float(sin)
    elif op=='cos':
        cos=math.cos(x)
        z=float(cos)
    elif op=='ghadre_motlagh':
        ghadre_motlagh=math.fabs(x)
        z=float(ghadre_motlagh)
    elif op=='log':
        log=math.log(x,y)
        z=float(log)
    elif op=='radians':
        radians=math.radians(x)
        z=float(radians)
    elif op=='tan':
        tan=math.tan(x)
        z=float(tan)
    elif op=='factorial':
        factorial=math.factorial(int(x))   
        z=float(factorial)
    print(z)
    print(time)
            