def trans(n, system):
    alf = '0123456789ABCDEF'
    s = ''
    while n > 0:
        s += alf[n % system]
        n //= system
    return s[::-1]

def summ(a, b, system):
    a = trans(a, system)
    b = trans(b, system)
    max_len = max(len(a), len(b))
    data_a = list(a.zfill(max_len))
    data_b = list(b.zfill(max_len))
    
    data_a = ' '.join(data_a)
    data_a = data_a.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F', '15')
    data_a = data_a.split()
    
    data_b = ' '.join(data_b)
    data_b = data_b.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F', '15')
    data_b = data_b.split()
    
    data_a  = data_a[::-1]
    data_b  = data_b[::-1]
    
    data_sum = (max_len + 1) * [0]
    for i in range(len(a)):
        data_sum[i] = int(data_a[i]) + int(data_b[i])

    remains = 0
    for i in range(len(data_sum)):
        data_sum[i] += remains
        remains = data_sum[i] // system
        data_sum[i] %= system

    while len(data_sum) > 1 and data_sum[-1] == 0:
        data_sum.pop()
        
    data_sum = data_sum[::-1]
    s = ''
    alf = '0123456789ABCDEF'
    for i in range(len(data_sum)):
        s += alf[data_sum[i]]
    return s

#10110010110101011000000100010001100011110100100110
#10211010211121020201221202122012
#26265300421436446
#2CB5604463D26

     


def mult(a, b, system):
    a = trans(a, system)
    b = trans(b, system)
    max_len = max(len(a), len(b))
    data_a = list(a)
    data_b = list (b)
    
    data_a = ' '.join(data_a)
    data_a = data_a.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F', '15')
    data_a = data_a.split()
    
    data_b = ' '.join(data_b)
    data_b = data_b.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F', '15')
    data_b = data_b.split()
    
    data_a  = data_a[::-1]
    data_b  = data_b[::-1]

    data_mult = [0]*(len(data_a)+len(data_b))

    for i in range(len(a)):
        for j in range(len(b)):
            data_mult[i+j] += int(data_a[i]) * int(data_b[j])

    remains = 0
    for i in range(len(data_mult)):
        data_mult[i] += remains
        remains = data_mult[i] // system
        data_mult[i] %= system

    while len(data_mult) > 1 and data_mult[-1] == 0:
        data_mult.pop()
        
    data_mult = data_mult[::-1]
    s = ''
    alf = '0123456789ABCDEF'
    for i in range(len(data_mult)):
        s += alf[data_mult[i]]
    return s

def dif(a, b, system):
    if a < b:
        c = b
        b = a
        a = c
    a = trans(a, system)
    b = trans(b, system)
    max_len = max(len(a), len(b))
    data_a = list(a.zfill(max_len))
    data_b = list(b.zfill(max_len))
    
    data_a = ' '.join(data_a)
    data_a = data_a.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F', '15')
    data_a = data_a.split()
    
    data_b = ' '.join(data_b)
    data_b = data_b.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14').replace('F', '15')
    data_b = data_b.split()
    
    data_a  = data_a[::-1]
    data_b  = data_b[::-1]
    
    data_dif = (max_len) * [0]
    for i in range(len(a)):
        data_dif[i] = int(data_a[i]) - int(data_b[i])

    remains = 0
    for i in range(len(data_dif)):
        if data_dif[i] < 0:
            data_dif[i] += system
            data_dif[i+1] -= 1

    while len(data_dif) > 1 and data_dif[-1] == 0:
        data_dif.pop()
        
    data_dif = data_dif[::-1]
    s = ''
    alf = '0123456789ABCDEF'
    for i in range(len(data_dif)):
        s += alf[data_dif[i]]
    return s

print('Введите числа:')
a = int(input())
b = int(input())

#print('Какую операцию с ними произвести?(Напишите "сложение", "вычитание" или "умножение")')
#ans = str(input())
print('Введите систему счисления, в которой требуется дать ответ:')
system = int(input())
#if ans == 'умножение':
print(str(a)+'_' + '10' + " *"  + str(b) +'_' + '10' + ' ='  + str(trans(a, system))+'_' + str(system) + " * " + str(trans(b, system))+'_' + str(system) + ' = ' + str(mult(a, b, system)))
#if ans == 'вычитание':
print(str(a)+'_' + '10' + " - " + str(b) +'_' + '10' + ' = ' + str(trans(a, system))+'_' + str(system) + " - " + str(trans(b, system))+'_' + str(system) + ' = ' + str(dif(a, b, system)))
#if ans == 'сложение':
print(str(a)+'_' + '10' + " + " + str(b) +'_' + '10' + ' = ' + str(trans(a, system))+'_' + str(system) + " + " + str(trans(b, system))+'_' + str(system) + ' = ' + str(summ(a, b, system)))

'''
def trans16list(n):
    alf = '0123456789ABCDEF'
    d = []
    i = 0
    while n > 0:
        d.append(n % 16)
        n //= 16
        i = 0
    return d[::-1]

def trans8(n):
    s = ''
    while n > 0:
        s += str(n % 8)
        n //= 8
    return s[::-1]

def trans3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]

def trans2(n):
    s = ''
    while n > 0:
        s += str(n % 2)
        n //= 2
    return s[::-1]
'''
