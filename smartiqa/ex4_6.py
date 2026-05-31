def all_eq(lst: list[str]) -> list[str]:
     """"
     >>> all_eq(['a', 'aa', 'aaa', 'aaaa'])
     ['a___', 'aa__', 'aaa_', 'aaaa']
     >>> all_eq([])
     []
     """
     if not lst: # not lst - список пустой
          return []

     max_len = len(max(lst, key=len))
     return [item.ljust(max_len, '_') for item in lst] #почему-то не работает с [] если переменная есть


