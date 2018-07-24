# date와 end_price라는 두개의 리스트를 daeshin이라는 딕셔너리로 생성하라.

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
end_price = [10500, 10300, 10100, 10800, 11000]
daeshin = dict(zip(date, end_price))
print(daeshin)
