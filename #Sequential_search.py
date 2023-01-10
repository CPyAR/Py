#Sequential serach
a=[2,4,1,5,7]
# tamanho array
a_size=len(a)
#print(a_size)
#define function arr-> array and k->key
def my_search (arr, k):
    for i in range (0,len(arr),+1):
        if arr[i]==k:
            #returns indice da lista
            return i
    return -1
#number to search key
key=int(input('Insert value to search: '))
if my_search(a,key)==-1:
    print('Value not found ')
    print(a)
else:
    print('value is in', my_search(a,key),' index')