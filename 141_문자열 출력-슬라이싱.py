# 한 라인의 텍스트를 입력 받아 "5 (가로) x n (세로)"로 텍스트를 변환하는 print5xn(string) 함수를 작성하여라.

def print5xn(string):
    for i in range (1,len(string)):
        if i % 5 == 0 :
            print(string[i])
        else :
            print(string[i], end='')

print5xn("sdfsfasdasdasd")