# 다음과 같이 도시 이름을 저장하고 있는 리스트가 있을 때 이름이 가장 긴 도시를 출력하는 프로그램을 작성하라.
city = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']
city.sort(key=len)
shortesLen=len(city[0])

for i in range (len(city)):
    if(len(city[i])==shortesLen):
        print(city[i])
    else:
        break