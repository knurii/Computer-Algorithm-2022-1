import time  # 시간 측정 위해 time 모듈 추가
import random  # 리스트를 무작위로 섞기위해 random 모듈 추가
from typing import MutableSequence

# 쉘 정렬
def shell_sort(a :  MutableSequence) -> None:
    n = len(a)
    h = n // 3
    while h > 0:
        for i in range(h,n):
            j = i -h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h //= 2

time1 = []
time_t = 0

ls = []  # 빈 리스트 생성
for i in range(5, 21):
    for j in range(100):
        j += 1
        n = 2 ** i
        ls.append(n)
        random.shuffle(ls)  # 정렬하기 전 무작위로 섞기

        start = time.time()
        shell_sort(ls)  # 삽입 정렬 실행 시간
        shell_time = (time.time() - start) * 1000

        time_t = time_t + shell_time

    time1.append(time_t / 100)

print(time1)
print(len(time1))


