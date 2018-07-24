# 087 문제를 if, elif, else와 같은 제어문을 사용하지 않고 풀어라. (힌트: 딕셔너리를 사용하여 통화별 매매 금액 산출)

curr_ExchangeRate = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
user_input = input("입력: ").split()
amount = float(user_input[0])
currency = user_input[1]

print("{0:.2f} 원".format(amount * curr_ExchangeRate[currency]))
