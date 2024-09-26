# Bubble sort
def bubble_sort():
    
    vetor = [3,8,7,2,6,1,23,12,4,20,34]
    print(vetor)
    n=len(vetor)
    for i in range(n):
      for j in range(0,n-i-1):
        if vetor[j]>vetor[j+1]:
          aux=vetor[j]
          vetor[j]=vetor[j+1]
          vetor[j+1]=aux
    print(vetor)


# Selection Sort

def selection_sort():

    vetor = [3,8,7,2,6,1]
    print(vetor)
    n=len(vetor)
    
    for i in range(n):
      id_min=i
      for j in range(i+1,n):
        if vetor[id_min]>vetor[j]:
          id_min=j
      aux=vetor[i]
      vetor[i]=vetor[id_min]
      vetor[id_min]=aux
    
    print(vetor)


# Quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)