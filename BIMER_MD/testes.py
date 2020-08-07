baixanainclusao = True
naturezaAtiva = False
mlist = ["baixanainclusao", False, True]

def boostr(x):
    if (type(x) == bool) & (x == True):
        return 'S'
    elif (type(x) == bool) & (x == False):
        return 'N'

    return x

x = map(boostr, mlist)

#convert the map into a list, for readability:
print(list(x))                