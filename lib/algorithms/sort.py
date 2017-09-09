def mergeSortTest(alist):
    if len(alist) > 1:
        split = len(alist) // 2
        leftpart = alist[:split]
        rightpart = alist[split:]
        mergeSortTest(leftpart)
        mergeSortTest(rightpart)

        i = 0
        j = 0
        k = 0
        while i < len(leftpart) and j < len(rightpart):
            if leftpart[i] < rightpart[j]:
                alist[k] = leftpart[i]
                i += 1
            else:
                alist[k] = rightpart[j]
                j += 1
            k += 1

        while i < len(leftpart):
            alist[k] = leftpart[i]
            i += 1
            k += 1

        while j < len(rightpart):
            alist[k] = rightpart[j]
            j += 1
            k += 1



def mergeSort(alist):
    if len(alist) > 1:
        print('Split: ', alist)
        mid_pos = len(alist) // 2
        left_part = alist[:mid_pos]
        right_part = alist[mid_pos:]

        mergeSort(left_part)
        mergeSort(right_part)
        i,j,k = 0,0,0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                alist[k] = left_part[i]
                i += 1
            else:
                alist[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            alist[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            alist[k] = right_part[j]
            j += 1
            k += 1
        print('Merge: ', alist)

def quickSort(alist):

    def partition(alist, start_pos, end_pos):
        split_val = alist[start_pos]
        first_pos = start_pos + 1
        last_pos = end_pos
        done = False

        while not done:
            while first_pos <= last_pos and alist[first_pos] <= split_val:
                first_pos += 1
            while last_pos >= first_pos and alist[last_pos] >= split_val:
                last_pos -= 1

            if first_pos > last_pos:
                done = True
            else:
                alist[first_pos], alist[last_pos] = alist[last_pos], alist[first_pos]

        alist[start_pos],alist[last_pos] = alist[last_pos], alist[start_pos]

        return last_pos

    def quickSortHelper(alist, start_pos, end_pos):
        if start_pos < end_pos:
            split_pos = partition(alist, start_pos, end_pos)
            quickSortHelper(alist, start_pos, split_pos - 1)
            quickSortHelper(alist, split_pos + 1, end_pos)


    quickSortHelper(alist, 0, len(alist) - 1)



print('wwwwwwwwwwwwwwwwwww')
alist = [54, 26, 93, 17, 77, 31, 44, 55, 21]
mergeSortTest(alist)
print(alist)