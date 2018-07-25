# 함수의 인자로 리스트를 입력 받아 아이템의 순서는 유지하면서 중복된 데이터를 제거하는 함수를 구현하라.

def remove_duplication(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items) - 1):
            if items[i] == items[j]:
                del items[i]
                break
    return items


print(remove_duplication([1, 1, 2, 3, 4, 4, 6, 6, 7]))
