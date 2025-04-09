lst = [1,2,3, [1,2,3,[3,4,[4,3]],2]]
lst1 = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]

def flatten(lst,flatten_list=[]):
    i=0
    for i in lst:
        if type(i) is list:
            flatten(i,flatten_list)#recursion
        else:
            flatten_list.append(i)
    return flatten_list
    

def convert(lst):
    out=[]
    for i in lst:
        if type(i) is list:
            out.append(convert(i))#recursion
        else:
            out.append([int(i) for i in list(i) if i.isdigit()])# list comprenhesion to append iff it is digit
    return out


print(flatten(lst))


print(convert(lst1))
    