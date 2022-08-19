#숫자를 여러개 입력해주세요. :10 20 30 40 50
#[10, 20, 30, 40, 50]
#가장 큰 값 : 50
#가장 작은 값 : 10
#나머지 값의 평균 : 30.0
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
  


list_1 = list(map(int, input().split()))
print(max(list_1))
print(min(list_1))


list_1.remove(MAX(list_1))
list_1.remove(MIN(list_1))

average = sum(list_1)/len(list_1)
print(average)




            
        
