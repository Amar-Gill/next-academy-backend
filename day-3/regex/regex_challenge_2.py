import re


def has_id(string):
    regex = r"(\d{6}-\d{2}-\d{4})"
    match = re.search(regex, string)
    if match:
        return True
    else:
        return False


# Output
print(has_id("please don't share this: 890414-14-1422"))   # true
print(has_id("please confirm your identity: 234-122-1422"))  # false

print()

def grab_id(string):
    regex = r"(\d{6}-\d{2}-\d{4})"
    match = re.search(regex, string)
    if match:
        return match.group()
    else:
        return 'nil'


# Output
print(grab_id("please don't share this: 890414-14-1422"))   # 890414-14-1422
print(grab_id("please confirm your identity: XXX-XX-1422"))  # nil

print()

def grab_all_ids(string):
    regex = r"(\d{6}-\d{2}-\d{4})"
    match = re.findall(regex, string)
    return match


# Output
# ["890414-14-1422", "900515-14-1092", "950616-12-5414"]
print(grab_all_ids("890414-14-1422, 900515-14-1092, 950616-12-5414"))
print(grab_all_ids("please confirm your identity: XXX-XX-1422"))  # []

print()

def hide_all_ids(string):
    regex = r"(\d{6}-\d{2}-(\d{4}))"
    # matches = re.findall(regex, string)
    # return_array=[]
    # if matches:
    #     for match in matches:
    #         return_array.append(r"******-**-" + match[1])
    #     return return_array
    # else:
    #     return string
    return re.sub(regex, r"******-**-\2", string)


# XXXXXX-XX-1422, XXXXXX-XX-1092, XXXXXX-XX-5414
print(hide_all_ids("890414-14-1422, 900515-14-1092, 950616-12-5414"))
# please confirm your identity: XXX-XX-1422
print(hide_all_ids("please confirm your identity: XXX-XX-1422"))

print()

def format_ids(string):
    regex = r"((\d{6}).?(\d{2}).?(\d{4}))"
    return re.sub(regex,r"\2-\3-\4", string )

print(format_ids("890414.14.1422, 900515141092, 950616-12-5414"))  # 890414-14-1422, 900515-14-1092, 950616-12-5414
print(format_ids("please confirm your identity: 763158581422"))  # please confirm your identity: 763158-58-1422
