# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
user_input = input("주민등록 번호: ").replace('-', '')

sum = 0
i = 2
for number in (user_input[:-1]):
    sum += int(number) * i
    i += 1
    if i == 10:
        i = 2
    print(sum)
sum %= 11

print(sum)
if (11 - sum == int(user_input[-1])):
    print("유효한 주민등록 번호 입니다.")
else:
    print("유효하지 않는 주민등록 번호 입니다.")
