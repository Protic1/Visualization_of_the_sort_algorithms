import random

list = []
for x in range(1,101):
    list.append(x)

random.shuffle(list)


def Selection_Sort(list):
    for i in range(len(list)):

        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j

        list[i], list[min] = list[min], list[i]
    return list

def Bubble_Sort(list):
    for i in range(len(list)-1):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def Insertion_Sort(list):
    for i in range(len(list)):
        key = list[i]

        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j = j - 1
            print(list)
        list[j+1] = key
        print(list)
    return list



i = 0
solved = False
key = list[i]
j = i - 1
def insertion(list):
    global i,key,j,solved
    if i <= len(list):
        if j >=0 and key < list[j]:
            list[j+1] = list[j]
            j = j - 1
        else:
            if i < (len(list) - 1):
                i += 1
                list[j + 1] = key
                key = list[i]
                j = i - 1
            else:
                solved = True

    else:
        solved = True




