# icecream 딕셔너리에서 최소 가격의 아이스크림 이름을 출력하라.

icecream = {'Tankboy': 1200, 'Ppangppare': 1800, 'Worldcorn': 1500, 'Melona': 1000}

for name, price in icecream.items(): # list와 비교,
    if price == min(icecream.values()):
        print(name)