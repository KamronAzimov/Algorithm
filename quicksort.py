from random import randrange
def qsort(array):
   if len(array)<2:
      return array
   else:
      pivot = array.pop(randrange(len(array)))
      small = [ i for i in array if i <= pivot]
      high = [ i for i in array if i > pivot]
      print(f'{small}+[{pivot}]+{high}]')
      return qsort(small) + [pivot] + qsort(high)

if __name__ == '__main__':
   array1 = [1, 22, 33, 44, 55, 21, 12, 13, 31]
   print(array1)
   print(qsort(array1))
   # array2 = list(range(20))
   # print(array2)
   # print(qsort(array2))

                  