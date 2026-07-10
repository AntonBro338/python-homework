import shutil

def replace_lines(pattern: str, replacement: str, input_file: str, output_file: str):
   """
   >>> replace_lines ('dag', 'dAg', 'input_file.txt', 'output_file.txt')
   'book\\n***START OF THE PROJECT\\nlook\\ndAg\\ndog bag\\n\\nbog\\nvog\\ngl hf\\nU2\\n***END OF THE PROJECT\\ngg\\nwp'
   """
   try:
       with open(input_file, 'r') as file:
        content = file.read()
   except IOError:
       print('Что-то пошло не так.')
       return None
   with open(output_file, 'w') as final_fail:
       if pattern in content:
           final_fail.write (content.replace(pattern, replacement))
           return content.replace(pattern, replacement)
       else:
           print ("Нет такой буквы!")
           return None


replace_lines ('dag', 'dAg', 'input_file.txt', 'output_file.txt')