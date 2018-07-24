# 파이썬3에 추가된 star expression은 다음과 같이 데이터를 언패킹하는데 유용하게 사용할 수 있다.

#다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,_,_=scores
print(valid_score)