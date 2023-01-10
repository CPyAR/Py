#Binary Search
b=[2,4,9,12,13,19]
#list size
b_size=len(b)
#intial index
b_i_ini=0
#final index
b_i_end=b_size-1
key=int(input('Insert value to search: '))
while b_i_ini<=b_i_end:
    middle=((b_i_ini +b_i_end)//2)
    if key == b[middle]:
        print('value is in', middle,' index')
        break
    elif key <b[middle]:
        # value is in the left middle part of array
        b_i_end=middle-1
    else:
        # value is in the right middle part 
         b_i_ini=middle+1