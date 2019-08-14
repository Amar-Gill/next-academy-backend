import re

def hide_serial(string):
    regex = r"(\d+)-(\d+)-(\d+)"
    return re.sub(regex, r"******-**-\3", string)

print(hide_serial("123456-12-1234"))   # XXXXXX-XX-1234

def hide_digits(string):
    regex = r"(\d+)"
    match = re.search(regex,string)
    replacement_string = r"*"*len(match.group(1))
    return re.sub(regex, replacement_string, string)

print(hide_digits("You have 100000 dollars"))   # You have --- dollars

def hide_last_four(string):
    regex = r"(\d+)-(\d+)-(\d+)"
    matches = re.finditer(regex, string)
    matches = re.findall(regex, string)
    revised_string = r""
    for index, match in enumerate(matches):
        if index == len(matches)-1:
            revised_string = revised_string + match[1] + '-' + match[2] + '-****'
        else:
            revised_string = revised_string + match[1] + '-' + match[2] + '-****, '

    print(revised_string)

# print(hide_last_four("12-34-5678, 90-80-7012, 45-65-1234"))  # 12-34-****, 90-80-****, 45-65-****
hide_last_four("12-34-5678, 90-80-7012, 45-65-1234")  # 12-34-****, 90-80-****, 45-65-****