# 사용자로부터 '10:00:01'와 같은 형태로 시간을 입력 받은 후 해당 시간이 00:00:00 으로부터 몇 초가 지났는지를 출력하라.
user_input = input('time: ')
user_input = user_input.split(':')
print(int(user_input[0]) * 3600 + int(user_input[1]) * 60 + int(user_input[2]))
