#!/usr/bin/python3
""" adds all arguments to python list and then saves them """

import sys
save_to_json_file = __import__('7-save_to_json_file).save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    count = 0
    try:
        data = load_from_json_file("add_item.json")
    except:
        my_list = []
        f = open("add_item.json", 'w+')
        save_to_json_file(my_list, "add_item.json")
        f.close()

    data = load_from_json_file("add_item.json")
    for arg in sys.argv:
        if count == 0:
            pass
            count += 1
        else:
            data.append(arg)
    save_to_json_file(data, "add_item.json")
