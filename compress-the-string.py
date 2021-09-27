from itertools import groupby

string = input()

for c, items in groupby(string):    
    print(tuple([len(list(items)),int(c)]), end=' ')