def get_even_list(l):
    new_l=[]
    for i in range(len(l)):
        if l[i]%2==0:
            new_l.append(l[i])
    return(new_l)

l = list(map(int, input('input a list of numbers separated by space: ').split()))
new_list = get_even_list(l)
print(new_list)
