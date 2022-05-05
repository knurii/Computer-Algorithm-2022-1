import time  # 시간 측정 위해 time 모듈 추가
import random  # 리스트를 무작위로 섞기위해 random 모듈 추가
from typing import MutableSequence

# 선택 정렬
def sel_sort(a):
    n = len(a)

    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

# 삽입 정렬
def insertion_sort(ls):
    for i in range(1, len(ls)):
        j = i - 1
        key = ls[i]
        while ls[j] > key and j >= 0:
            ls[j+1] = ls[j]
            j = j -1
        ls[j+1] = key
    return ls

# 퀵 정렬
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

# 버블 정렬
def bubble_sort(ls):
    n = len(ls)  # 배열의 크기를 측정
    # 배열의 크기만큼 반복
    for i in range(n):
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(0, n - i - 1):
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]  # 서로 위치를 변환

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

ls = [] #빈 리스트 생성
for i in range(5, 21):
    print(f'입력 갯수 : {i-4}개')
    n = 2 ** i
    ls.append(n)
    random.shuffle(ls)  # 정렬하기 전 무작위로 섞기
    ls2 = ls[:] # 퀵 정렬에 사용할 리스트
    ls3 = ls[:] # 버블 정렬에 사용할 리스트
    ls4 = ls[:] # 삽입 정렬에 사용할 리스트
    ls5 = ls[:] # 셸 정렬에 사용할 리스트
    ls6 = ls[:] # 힙 정렬에 사용할 리스트


    print(f'정렬 전 리스트 :{ls}')

    start = time.time()
    sel_sort(ls)  # 선택 정렬 실행 시간
    sel_time = (time.time() - start) * 1000

    start = time.time()
    quick_sort(ls2)  # 퀵 정렬 실행 시간
    quick_time = (time.time() - start) * 1000

    start = time.time()
    bubble_sort(ls3)  # 버블 정렬 실행 시간
    bubble_time = (time.time() - start) * 1000

    start = time.time()
    insertion_sort(ls4)  # 버블 정렬 실행 시간
    insertion_time = (time.time() - start) * 1000

    start = time.time()
    shell_sort(ls5)  # 버블 정렬 실행 시간
    shell_time = (time.time() - start) * 1000

    start = time.time()
    heap_sort(ls)  # 힙 정렬 실행 시간
    heap_time = (time.time() - start) * 1000

    print(f'정렬 후 리스트 : {ls}\n')

    print(f'1. 선택 정렬 실행시간: {sel_time:.10f }ms')
    print(f'2. 퀵 정렬 실행시간: {quick_time:.10f }ms')
    print(f'3. 버블 정렬 실행시간: {bubble_time:.10f }ms')
    print(f'4. 삽입 정렬 실행시간: {insertion_time:.10f }ms')
    print(f'5. 셸 정렬 실행시간: {shell_time:.10f }ms')
    print(f'6. 힙 정렬 실행시간: {heap_time:.10f }ms\n\n')