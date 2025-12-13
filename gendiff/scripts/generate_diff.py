from parser import read_file

def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    # пока можно вернуть заглушку или простую разницу
    # далее тут появится построение дерева diff и форматтеры
    dict1, dict2 = dict(data1), dict(data2)
    all_keys = set(dict1) | set(dict2)
    sorted_keys = sorted(all_keys)
    
    res = ''
    
    for key in sorted_keys:
        if key not in dict1:
            res += '+ ' + key + ': ' + str(dict2[key]) + '\n'
        elif key not in dict2:
            res += '- ' + key + ': ' + str(dict1[key]) + '\n'
        else:
            if dict1[key] == dict2[key]:
                res += '  ' + key + ': ' + str(dict1[key]) + '\n'
            else:
                res += '- ' + key + ': ' + str(dict1[key]) + '\n'
                res += '+ ' + key + ': ' + str(dict2[key]) + '\n'
    
    return res
            