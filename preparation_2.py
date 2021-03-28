import re

def solution(s):
    clear_string = ""
    contain_upper = False
    substring_list = []


    K = '@'
    s = re.sub(r'\d', K, s)
    print("replaced s:", s)
    substring_list = s.split(K)

    for char in s.strip():
        if not char.isalpha():
            if clear_string != "" and contain_upper:
                substring_list.append(clear_string)
            contain_upper = False
            clear_string = ""
            print("sub_str:", substring_list)
        else:
            clear_string += char
            if char.isupper():
                contain_upper = True
            print("clear_str:", clear_string, ", upper:", contain_upper)

    return substring_list

s = "  a0Babu12cEi%zyx4xxX"
print(solution(s))
