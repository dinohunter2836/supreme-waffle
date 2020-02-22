import re
import argparse


def word_count(path):
    with open(path) as file:
        text = file.read()
    arr = re.split(r'\W', text)
    word_dict = dict()
    for index in range(0, len(arr)):
        if arr[index] == '':
            continue
        if arr[index] in word_dict:
            word_dict[arr[index]] += 1
        else:
            word_dict[arr[index]] = 1
    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, min(10, len(sorted_dict))):
        print(sorted_dict[i][0], end=' ')
    print("\n")


def qsort(arr, left, right):
    middle = arr[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while arr[i] < middle:
            i += 1
        while arr[j] > middle:
            j -= 1
        if i <= j:
            p = arr[i]
            arr[i] = arr[j]
            arr[j] = p
            i += 1
            j -= 1
    if i < right:
        qsort(arr, i, right)
    if j > left:
        qsort(arr, left, j)


def merge_sort(arr):
    if len(arr) > 1:
        middle = (len(arr) - 1) // 2
        arr1 = merge_sort(arr[slice(0, middle + 1)])
        arr2 = merge_sort(arr[slice(middle + 1, len(arr))])
        return merge(arr1, arr2)
    else:
        return arr


def merge(arr1, arr2):
    i = 0
    j = 0
    arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr


def fibonacci(path):
    with open(path) as file:
        n = int(file.read().split()[0])
    gen = fibonacci_generator()
    for i in range(n):
        print(next(gen))


def fibonacci_generator():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        c = a + b
        a = b
        b = c
        yield c


def quick_sort(path):
    with open(path) as f:
        arr = list(map(int, f.read().split()))
    qsort(arr, 0, len(arr) - 1)
    print(arr)


def merge_sorted(path):
    with open(path) as f:
        arr = list(map(int, f.read().split()))
    print(merge_sort(arr))


functions = {
    'text_stats': word_count,
    'qsort': quick_sort,
    'merge_sort': merge_sorted,
    'fibonacci': fibonacci
}

parser = argparse.ArgumentParser(description="Choose a function to execute")
parser.add_argument('file_path', help="input file")
parser.add_argument('func', help='choose function to execute', choices=functions.keys())
args = parser.parse_args()
func = functions[args.func]
func(args.file_path)
