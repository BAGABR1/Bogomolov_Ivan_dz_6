from sys import argv


program, sale = argv
with open('bakery.csv', 'a', encoding='utf-8') as file:
    sale += '\n'
    file.write(str(sale))
