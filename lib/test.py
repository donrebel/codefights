
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)



def quickSortTest():

    def quickSort(alist):
        quickSortHelper(alist, 0, len(alist) - 1)

    def quickSortHelper(alist, first_pos, last_pos):
        if first_pos < last_pos:
            split_pos = partition(alist, first_pos, last_pos)
            quickSortHelper(alist, first_pos, split_pos - 1)
            quickSortHelper(alist, split_pos + 1, last_pos)

    def partition(alist, first_pos, last_pos):
        split_val = alist[first_pos]
        left_mark = first_pos + 1
        right_mark = last_pos
        done = False
        while not done:
            while left_mark <= right_mark and alist[left_mark] <= split_val:
                left_mark += 1
            while right_mark >= left_mark and alist[right_mark] >= split_val:
                right_mark -= 1

            if left_mark > right_mark:
                done = True
            else:
                alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
        alist[first_pos], alist[right_mark] = alist[right_mark], alist[first_pos]

        return right_mark




def mergeSortTest(alist):
    if alist > 1:
        split = len(alist) // 2
        leftpart = alist[:split]
        rightpart = alist[split:]
        mergeSort(leftpart)
        mergeSort(rightpart)

        i = 0
        j = 0
        k = 0
        while i < len(leftpart) and j < len(rightpart):
            if leftpart[i] < rightpart[j]:
                alist[k] = leftpart[i]
                i += 1
            else:
                alist[k] = rightpart[j]
                j += j
            k += 1

        while i < len(leftpart):
            alist[k] = leftpart[i]
            i += 1
            k += 1

        while j < len(rightpart):
            alist[k] = rightpart[j]
            j += 1
            k += 1

print('wwwwwwwwwwwwwwwwwww')
alist = [54, 26, 93, 17, 77, 31, 44, 55, 21]
mergeSortTest(alist)
print(alist)

                                                                                                                                                 