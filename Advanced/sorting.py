#This is some sorting that I have had on my white board and it is time to put in my github
#You could use sort() and sorted() but lets say you want create your own sorting

def bubble(list_a):
    index_len = len(list_a)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, index_len): #This is setting the range from 0 to what ever the length of the list is minus 1 so it knows how many iterations are needed in the for loop
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a

print(bubble([19,2,25,4,2]))


def sorting(x):
    for i in range(0, len(x)-1):
        for j in range(0, len(x)-1):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    return(x)

arr2 = [-1, 22, -9, 3/2, 44]
arr = [4, 3, 2, 8, -1, 24]

print(sorting(arr2))