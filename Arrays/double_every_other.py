'''
- write a function that doubles every second integer in a list
- start from the left
'''

def double_every_other(lst):
    res = []
    
    for i, v in enumerate(lst):
        if i % 2 != 0:
            res.append(v*2)
        else:
            res.append(v)
    return res


def double_every_other(lst):
    return [x * 2 if x % 2 else x for i, x in enumerate(lst)]


print(double_every_other([1,2,3,4,5])) # [1,4,3,8,5]