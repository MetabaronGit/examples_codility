# ze stringu vybrat nejdelší substring obsahující alespoň 1 velké písmeno
# substring nesmí obsahovat čísla
# Např: string = a0Bab -> Bab

def solution(s):
    clear_string = ""
    contain_upper = False
    substring_list = []

    for char in s:
        if not char.isdigit() and char.isalpha():
            clear_string += char
            if char.upper():
                contain_upper = True
        else:
            if clear_string != "" and contain_upper:
                substring_list.append(clear_string)
                contain_upper = False
                clear_string = ""

    print(substring_list)
    result = ""
    for item in substring_list:
        if len(result) < len(item):
            result = item

    return result


S = "a0Bab1n%lk"
print(solution(S))