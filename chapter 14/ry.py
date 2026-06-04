import shutil

def replace_lines(pattern: str, replacement: str, input_file: str, output_file: str):
   """
   Вторая версия, в интерпритаторе она выдает не понятно что, но зато реально изменяет файл. Первая версия не трогала файл по сути.
   """
   shutil.copyfile(input_file, output_file)
   try:
       with open(input_file, 'r', encoding='utf-8') as file:
           content = file.read()
           modified_content = content.replace(pattern, replacement)
   except Exception(BaseException):
       print('Что-то пошло не так.')
       return None
   with open(output_file, 'w', encoding='utf-8') as file:

        return file.write(modified_content)


replace_lines ('dag', 'dAg', 'input_file.txt', 'output_file.txt')