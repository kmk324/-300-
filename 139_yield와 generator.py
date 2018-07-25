# 파이썬 제너레이터란 yield 키워드가 사용된 함수를 의미한다.
# 아이템을 찾는 코드를 작성할 때 yield를 사용한 제너레이터 함수가 주로 사용된다.
# 제너레이터를 사용하면 아이템을 찾는 코드와 결과를 저장하는 코드를 분리할 수 있으며,
# 대량의 데이터를 처리할 때 더 적은 메모리가 사용된다.
# 입력 리스트에서 홀수를 추출하는 제너레이터 함수인 pickup_odd_by_iter를 구현하고 이를 사용해보자.

def pickup_odd_by_iter(items):
        for item in items:
            if item % 2 == 1:
                yield item


result = list(pickup_odd_by_iter([1, 2, 3, 4]))
print(result)