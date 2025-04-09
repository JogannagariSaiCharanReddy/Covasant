D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
    
def intersection(d1,d2):
    return {item:d1[item] for item in d1 if item in d2}

def sub(d1,d2):
    return {item:d1[item] for item in d1 if item not in d2}


def union(d1,d2):
    return d1|d2            


def merge(d1,d2):    
    for item in d2:
        if item in d1:
            d1[item]+=d2[item]
        else:
            d1[item]=d2[item]
    return d1
    
print(union(D1,D2))
print(intersection(D1,D2))            
print(sub(D1,D2))
print(merge(D1,D2))
    