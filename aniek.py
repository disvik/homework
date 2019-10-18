# -*- coding: utf-8 -*-
from datetime import datetime

try:
    file = open("ai183.txt", "r")
except IOError:
    print("File doesn't exist...")
    exit()

second_number, colon = False, False
array = []

while True:
    itrtr = file.read(1)

    if not itrtr:
        break

    if itrtr == "1":
        check = file.read(1)
        if check == "6":
            second_number = True
            itrtr = file.read(1)

        if itrtr == ":":
            colon = True
    # по достижению совпаденя ряда признаков(число и последующее двоеточие) берём урода после
    if second_number == True and colon == True:
        file.seek(file.tell() + 1)
        itrtr = file.read(1)

        while itrtr != "}":
            array.append(itrtr)
            itrtr = file.read(1)
        break

file.close()

merge_sort_array, quick_sort_array, heap_sort_array = [], [], []

for i in range(len(array)):
    merge_sort_array.append(array[i])
    quick_sort_array.append(array[i])
    heap_sort_array.append(array[i])

start_time = datetime.now()

def merge_sort(merge_sort_array):
    if len(merge_sort_array) > 1:
        mid = len(merge_sort_array) // 2
        left_half = merge_sort_array[:mid]
        right_half = merge_sort_array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merge_sort_array[k] = left_half[i]
                i += 1
            else:
                merge_sort_array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            merge_sort_array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            merge_sort_array[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(quick_sort_array):
    less, equal, greater = [], [], []

    if len(quick_sort_array) > 1:
        pivot = quick_sort_array[0]
        for x in quick_sort_array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return quick_sort_array


def heap_sort(array_heap_sort):
    def sift_down(parent, limit):
        item = array_heap_sort[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and array_heap_sort[child] < array_heap_sort[child + 1]:
                child += 1
            if item < array_heap_sort[child]:
                array_heap_sort[parent] = array_heap_sort[child]
                parent = child
            else:
                break
        array_heap_sort[parent] = item

    length = len(array_heap_sort)
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    for index in range(length - 1, 0, -1):
        array_heap_sort[0], array_heap_sort[index] = array_heap_sort[index], array_heap_sort[0]
        sift_down(0, index)


start_time = datetime.now()
merge_sort(merge_sort_array)
end_time = datetime.now()
print("Merge sort:", merge_sort_array)
print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()
end_time = datetime.now()
print("Quick sort:", quick_sort(quick_sort_array))
print('Duration: {}'.format(end_time - start_time))

start_time = datetime.now()
heap_sort(heap_sort_array)
end_time = datetime.now()
print("Heap sort:", heap_sort_array)
print('Duration: {}'.format(end_time - start_time))

