from typing import Iterator

def sum_five(it: Iterator[int]) -> int:
   """Функция складывает первые 5 элементов последовательности
   >>> sum_five([1, 2, 3, 4])
   10
   >>> sum_five([1, 2, 3, 4, 5, 1000])
   15
   >>> sum_five((x*x for x in range(1, 1000000000)))
   55
   """
   total = 0
   for index, item in enumerate(it):
       total += item
       if index == 4:
           break
   return total

print (sum_five([x*x for x in range(1, 1000000000)]))
