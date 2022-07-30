import os
import sys

# path = os.walk('.')
# for item in path:
#     print(item)


def list_all_content(path):
    def list_dir(d):
        # global inserted_tab
        nonlocal inserted_tab
        all_content = os.listdir(d)
        for item in all_content:
            current_path = os.path.join(d, item)
            if os.path.isdir(current_path):
                inserted_tab += 1
                print('\t' * inserted_tab, '[folder: ]', item)
                list_dir(current_path)
                inserted_tab -= 1
            else:
                print('\t' * inserted_tab, '  ', '[file: ]', item)
    inserted_tab = 0
    if os.path.exists(path):
        print('\t' * inserted_tab, path)
        list_dir(path)
    else:
        print('path does not exist')
        sys.exit(-1)


if __name__ == '__main__':
    list_all_content('..')
