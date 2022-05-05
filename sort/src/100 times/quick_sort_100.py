import time  # 시간 측정 위해 time 모듈 추가
import random  # 리스트를 무작위로 섞기위해 random 모듈 추가
from typing import MutableSequence


def quick_sort(ls):
    if len(ls) <= 1:
        return ls

    pivot = ls[len(ls) // 2]
    less_ls, equal_ls, greater_ls = [], [], []
    for num in ls:
        if num < pivot:
            less_ls.append(num)
        elif num > pivot:
            greater_ls.append(num)
        else:
            equal_ls.append(num)
    return quick_sort(less_ls) + equal_ls + quick_sort(greater_ls)

time1 = []
quick_time_t = 0

ls = []  # 빈 리스트 생성
for i in range(5, 21):
    for j in range(100):
        j += 1
        n = 2 ** i
        ls.append(n)
        random.shuffle(ls)  # 정렬하기 전 무작위로 섞기

        start = time.time()
        quick_sort(ls)  # 선택 정렬 실행 시간
        quick_time = (time.time() - start) * 1000

        quick_time_t = quick_time_t + quick_time

    time1.append(quick_time_t/100)

print(time1)
print(len(time1))