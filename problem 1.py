def sorter(arra, typ):
    if typ == "none":
        return arra
    elif typ == 'asc':
        return arra.sort()
    elif typ == "desc":
        return arra.sort()[-1::-1]
    else:
        return 'Error in type of sorting!!'

arra = list(map(int, input().split()))
typ = input('enter none for same list; asc for increasingly sorted; desc for decreasingly sorted:')
print(sorter(arra,typ))
