import time  # 시간 측정 위해 time 모듈 추가
import random  # 리스트를 무작위로 섞기위해 random 모듈 추가
from typing import MutableSequence

# 힙 정렬
def heap_sort(a : MutableSequence) -> None:
    def down_heap (a : MutableSequence, left: int, right: int) -> None:
        tmp = a[left]
        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if tmp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = tmp

    n = len(a)

    for i in range((n-1) // 2,-1,-1):
        down_heap(a, i, n-1)

    for i in range(n-1, 0 , -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)

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
        heap_sort(ls)  # 삽입 정렬 실행 시간
        heap_time = (time.time() - start) * 1000

        time_t = time_t + heap_time

    time1.append(time_t / 100)

print(time1)
print(len(time1))


