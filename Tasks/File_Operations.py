with open('file.txt', 'r') as file:
 content = file.read()
 print(content)

 with open('file.txt', 'w') as file:
  file.write('Hello, DevOps!')
