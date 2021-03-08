from sys import argv


program, *args = argv
if len(args) == 0:
    args.append('')
    args.append('')
if len(args) == 1:
    args.append('')
list_sales = []
with open('bakery.csv', 'r', encoding='utf-8') as file:
    if args[0] == '' and args[1] == '':
        print(file.read())
    if args[0] != '' and args[1] == '':
        line = file.readline()
        while line:
            list_sales.append(line.strip())
            line = file.readline()
        for i in range(int(args[0]) - 1, len(list_sales)):
            print(list_sales[i])
    if args[0] != '' and args[1] != '':
        line = file.readline()
        while line:
            list_sales.append(line.strip())
            line = file.readline()
        for i in range(int(args[0]) - 1, int(args[1])):
            print(list_sales[i])
