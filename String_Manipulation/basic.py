## Reverse a string:

def rev_str(str):
    return str[: : -1]  # we can also do the same using reverse function

string = "Rishav"
output = rev_str(string)
print(f"Your reversed string is : {output}")


# Checking if a given string is plaindrome or not

def str_plndrm(str):
    str = str.lower().replace(" " ,"")
    if str == str[: : -1]:
        return True
    else:
        return False
    
string = input("Enter your string : ")
output = str_plndrm(string)
print(output)


# Counting the occurance of a character in a string.

def chr_count(str, chr):
    str = str.lower().replace(" ", "")
    count = str.count(chr)
    return count

string = "my name is rishav kumar"
x = "m"
output = chr_count(string, x)
print(f"The number of {x} in the given string is : {output}")

## Counting the occurance of each character in a given string.

def count_chrs(str):
    str = str.lower().replace(" ","")
    dict = {}
    for chrs in str:
        count = str.count(chrs)
        dict[chrs] = count
    return dict

string = "My name is rishav kumar and I am a student of final year"
output = count_chrs(string)
print(output)

