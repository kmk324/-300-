# 입력된 문자열들을 연결한 후, 화면에 출력하는 print_my_string (string1, string2, ...) 함수를 작성하여라. 단, 입력 문자열은 여러개 입력될 수 있다.

def print_my_string(*args):
    result = ""
    for string in args:
        result += string
    print(result)


print_my_string("s", "d", "f")
