## Reversing  a string without any function.

def str_rev(strng):
    str_list = list(strng)  # Convert string to a list
    start = 0
    end = len(str_list) - 1

    while start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        start += 1
        end -= 1

    reversed_str = ''.join(str_list)  # Convert list back to string
    return reversed_str

string = "Rishav"
output = str_rev(string)
print(f"Your reversed string is: {output}")



def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
        print(reversed_string)
    return reversed_string


string = "Rishav"
output = reverse_string(string)
print(f"Your reversed string is: {output}")
