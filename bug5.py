def is_valid_char(c):
    if c == 'a' or 'b':
        return True
    return False

print(is_valid_char('a'))

#or thiis program
def is_valid_char(c):
    return c in ('a', 'b')
print(is_valid_char('j'))
# b is truthy why