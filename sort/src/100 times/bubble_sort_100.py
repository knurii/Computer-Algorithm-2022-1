import time  # 시간 측정 위해 time 모듈 추가
import random  # 리스트를 무작위로 섞기위해 random 모듈 추가
from typing import MutableSequence

def bubble_sort(ls):
    n = len(ls)  # 배열의 크기를 측정
    # 배열의 크기만큼 반복
    for i in range(n):
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(0, n - i - 1):
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]  # 서로 위치를 변환

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
        bubble_sort(ls)  # 삽입 정렬 실행 시간
        bubble_time = (time.time() - start) * 1000

        time_t = time_t + bubble_time

    time1.append(time_t / 100)

print(time1)
print(len(time1))


