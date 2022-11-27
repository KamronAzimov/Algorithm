def bubbleSort(array: list) -> list:
   for i in range(len(array)):
      for j in range(len(array)-i-1):
         if array[j]>array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
         print(array) 
         
if __name__ == '__main__':
   array = [5, 3, 11, 12, 43, 23, 8, 7, 6]
   print(array)
   bubbleSort(array)