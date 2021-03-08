def reader():
    dict_file = {}
    with open('users.csv', 'r', encoding='utf-8') as file_1:
        with open('hobby.csv', 'r', encoding='utf-8') as file_2:
            content_1 = file_1.readlines()
            content_2 = file_2.readlines()
            list_1 = ([i.replace('\r', '').replace('\n', '') for i in content_1])
            list_2 = ([i.replace('\r', '').replace('\n', '') for i in content_2])
            if len(list_2) > len(list_1):
                return 1
            if len(list_1) > len(list_2):
                for i in range(len(content_2)):
                    dict_file[list_1[i]] = list_2[i]
                for i in range(len(list_2), len(list_1)):
                    dict_file[list_1[i]] = None
            else:
                for i in range(len(content_1)):
                    dict_file[list_1[i]] = list_2[i]
    with open('dict.csv', 'w+', encoding='utf-8') as f:
        f.write(str(dict_file))
        f.seek(0)
        print(f.read())


reader()
