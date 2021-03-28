def solution(s):
    clear_string = ""
    contain_upper = False
    substring_list = []

    for char in s:
        if not char.isdigit():
            if char.isupper():
                contain_upper = True
            clear_string += char
            print("clear_str:", clear_string)
        else:
            if clear_string != "" and contain_upper:
                substring_list.append(clear_string)
                contain_upper = False
                clear_string = ""
                print("sub_str:",substring_list)

    return substring_list

s = "a0Bab12cEi%ZXY4xxX"
print(solution(s))
