# 파일 이름이 리스트에 저장되어 있을 때 확장자가 *.h나 *.c인 파일에 대한 리스트를 생성하라.

filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']
result = []
for i, item in enumerate(filenames):
    if (item.endswith('.h') or item.endswith('.c')):
        result.append(item)
print(result)
