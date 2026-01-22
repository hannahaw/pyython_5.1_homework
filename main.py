import string
import keyword

name = input()
is_valid = True

if name in keyword.kwlist:
    is_valid = False
elif len(name) > 0 and name[0].isdigit():
    is_valid = False
elif name != name.lower():
    is_valid = False
elif ' ' in name:
    is_valid = False
elif name.count('_') == len(name) and len(name) > 1:
    is_valid = False
else:
    for char in name:
        if char in string.punctuation and char != '_':
            is_valid = False
            break

print(is_valid)
