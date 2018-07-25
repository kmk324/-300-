# 정숫값과 자리수 값을 입력받아 위와 같은 형태로 2의 보수를 출력하는 프로그램을 작성하라.
# re

def twos_complement(num, numOfDigits):
    if num >= 0:
        return (format(num, 'b').zfill(numOfDigits))
    else:
        num = (format(abs(num) - 1, 'b').zfill(numOfDigits))
        minus_comp = ""
        for i in range(len(num) - 1, -1, -1):
            minus_comp += str((int(num[i]) + 1) % 2)
        minus_comp = minus_comp[-1::-1]
        return (minus_comp)


print(twos_complement(-4, 3))
