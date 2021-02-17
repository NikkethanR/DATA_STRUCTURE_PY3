#Bubble Sort 
def bubble_sort(elements):
  size = len(elements)
  for j in range(size-1):
    swapped = False #swapped element is set to false
    for i in range(size-1-j):
      if elements[i]>elements[i+1]:
        elements[i],elements[i+1]=elements[i+1],elements[i]
        print(elements)
        swapped = True
        #if the list is already sorted the the loop will break
    if not swapped:
      break

elements=[5,9,7,4,18,25,1,15]
bubble_sort(elements)
print(elements)