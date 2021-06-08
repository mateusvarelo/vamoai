def cal(num1,num2,operador):
    return eval(f'{num1}{operador}{num2}')
print(cal(2,3,'**'))# 2*2*2=8 (2 elevado a 3)
print(cal(5,5,'/'))#5/5 = 1 (Divisão)