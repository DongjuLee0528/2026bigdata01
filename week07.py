import numpy as np

# l1 = [9, '짬뽕', 3.7, [1, 2, 3]]  # 정수, 문자열, 실수, 리스트
l1 = [9, '짬뽕', 3.7]  # 정수, 문자열, 실수

array01 = np.array(l1)

print(l1)
print(array01)

array02 = np.arange(10)
print(array02)

array03 = np.ones(shape=(2, 4), dtype=int)
print(array03)
print(array03.T)