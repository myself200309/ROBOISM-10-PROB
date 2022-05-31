def doubler(string):
    arra = string.split('')
    nw_arra = []
    for i in range(len(arra)):
        nw_arra[i] = arra[i]*2
    return ''.join(nw_arra)

string = input('enter string to be doubled:')
print(doubler(string))
