# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

curr_ExchangeRate = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
user_input = input("입력: ")
user_input = user_input.split(' ')
user_input[0] = float(user_input[0])

if (user_input[1] == "달러"):
    print('{0:.2f} 원'.format(user_input[0] * curr_ExchangeRate["달러"]))
elif (user_input[1] == "엔"):
    print('{0:.2f} 원'.format(user_input[0] * curr_ExchangeRate["엔"]))
elif (user_input[1] == "유로"):
    print('{0:.2f} 원'.format(user_input[0] * curr_ExchangeRate["유로"]))
else:
    print('{0:.2f} 원'.format(user_input[0] * curr_ExchangeRate["위안"]))
