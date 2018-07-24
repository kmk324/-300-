# 다음과 같이 도시 이름을 저장하고 있는 리스트가 있을 때 이름이 가장 긴 도시를 출력하는 프로그램을 작성하라.
city = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']
city.sort(key=len)
longestLen=len(city[-1])

for i in range (len(city)-1,-1,-1):
    if(len(city[i])==longestLen):
        print(city[i])
    else:
        break