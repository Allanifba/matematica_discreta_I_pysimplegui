def base_10_para_base_b(n, b):
    base_n = ""
    n1 = n
    while n > 0:
        dig = int(n % b)
        if dig < 10:
            base_n += str(dig)
        else:
            base_n += chr(ord('A') + dig - 10)
        n //= b
    base_n = base_n[::-1]
    return print(f'O valor correspondente ao número decimal {n1} na base {b} é {base_n}.')


'''
Exemplo: base_10_para_base_b(10,3)
'''

