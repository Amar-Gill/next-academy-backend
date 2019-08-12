
def format_name(first_name, last_name):
    # first_name = first_name.lower()
    # last_name = last_name.lower()
    first_name = first_name[0].upper() + first_name[1:].lower()
    last_name = last_name[0].upper() + last_name[1:].lower()
    return first_name + ' ' + last_name

name = format_name('jOHN', 'lEE')
print(name)