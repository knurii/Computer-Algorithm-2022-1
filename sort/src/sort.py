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