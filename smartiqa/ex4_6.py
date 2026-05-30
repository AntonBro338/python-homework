def all_eq(lst: list[str]) -> list[str]:
     """"
     >>> all_eq(['a', 'aa', 'aaa', 'aaaa'])
     ['a___', 'aa__', 'aaa_', 'aaaa']
     >>> all_eq([])
     []
     """
     return [item.ljust(len(max(lst, key=lambda x: len(x))), '_') for item in lst]

