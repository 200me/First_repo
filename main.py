
def MAX(list_2):
    tmp = 0
    for x in list_2:
        if x > tmp :
            tmp = x
    return tmp

def MIN(list_2):
    tmp = 100
    for x in list_2:
        if x < tmp :
            tmp = x
    return tmp

def AVG(list_2):
    return (float)(sum(list_2))/len(list_2)
  
#Play

list_1 = list(map(int, input().split()))
print(max(list_1))
print(min(list_1))


list_1.remove(MAX(list_1))
list_1.remove(MIN(list_1))

average = sum(list_1)/len(list_1)
print(average)




            
        
