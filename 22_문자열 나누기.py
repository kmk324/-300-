# 여러개의 종목코드가 구분자 ";"로 연결된 문자열이 있다. 구분자를 기준으로 각 종목 코드를 나누고 이를 파이썬 리스트로 저장하라.
companies = '000660;060310;0133340;095570;068400;006840'
sepList = companies.split(';')
print(sepList)
