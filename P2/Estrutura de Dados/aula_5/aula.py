def bubble_sort(vetor):
	n = len(vetor)
	
	for i in range(n):
	
		for j in range(0, n - i - 1):
		
			if vetor[j] > vetor[j + 1]:
				temp = vetor[j]
				vetor[j] = vetor[j + 1]
				vetor[j + 1] = temp
				
	return vetor

def selection_sort(vetor):
	n = len(vetor)
	
	for i in range(n):
		id_minimo = i
		for j in range(i + 1, n):
			if vetor[id_minimo] > vetor[j]:
				id_minimo = j
		temp = vetor[i]
		vetor[i] - vetor[id_minimo]
		vetor[id_minimo] = temp
	return vetor

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
