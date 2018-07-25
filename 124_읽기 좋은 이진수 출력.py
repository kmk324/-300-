# 숫자를 입력 받아 2진수를 출력하는 print_readable_bin() 함수를 작성하라. 출력된 이진수는 가독성을 위해 네 자리마다 '_' 구분자가 삽입되어 있다.

def print_readable_bin(digits):
    return format(digits, '_b')


print(print_readable_bin(16))
