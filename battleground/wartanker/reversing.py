def crypto_solver(equation, enc_flag, functions=''):
    exec(functions)
    flag = ''
    for i in enc_flag: # encrypted flag
        for j in range(256):
            if eval(equation) == i:
                flag += chr(j)
    return flag
