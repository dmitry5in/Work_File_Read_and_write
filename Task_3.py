import os


def add_txt_file():
    file_list = [x for x in os.listdir() if x.endswith(".txt")]
    return file_list


def sort_file():
    list_file = add_txt_file()
    new_list = []
    for file in list_file:
        with open(file, "r", encoding='utf-8') as read_file:
            dict_list = {}
            lines = read_file.readlines()
            dict_list["name_file"] = file
            dict_list["count"] = len(lines)
            dict_list["data"] = lines
            new_list.append(dict_list)
    new_list = sorted(new_list, key=lambda k: k['count'])

    for item in new_list:
        with open('new_file.txt', "a", encoding='utf-8') as new_f:
            new_f.writelines(item['name_file'] + '\n')
            new_f.writelines(str(item['count']) + '\n')
            s = "".join(item['data'])
            new_f.writelines(str(s) + '\n')
            new_f.writelines('\n')

    some_text = "Завершено"
    return some_text


print(sort_file())