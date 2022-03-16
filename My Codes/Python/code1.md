Let's start with something easy

So this code will remove items(strings or integars) from a list

First, We defined the lists:

array_str = ["Dave", "Sam", "Lionel", "Drake"]
array_int = [1, 2, 3, 4]

Sencond, Define a function for the string list, make it print the list and ask for the user's input:

def remove_str(arr):
    print(arr)
    val = input("Select the item you want to remove>>> ")

Third, Check if the the user's is in the list:
If the input isn't in the list, have it print an error message
If it is in the list, have it remove it from the list using the "remove()" function, print the new array and a line break:

if val not in arr:
        print("Input not in array\n")
    else:
        arr.remove(val)
        print(arr)
        print("\n")

Fourth, Define a funtion for the integar list, now, this last part is similar to the third part, but, we'll use the "int()" while using the "remove()" function: 

arr.remove(int(val))

The reason is because if you don't use it, the remove function would not be able to find the inputed value cause if the "input()" function is used, whatever is inputed is taken as a string not as an integar

Lastly, call the functions with the corresponding values:

remove_str(array_str)
remove_int(array_int)

So the full code is:

array_str = ["Dave", "Sam", "Lionel", "Drake"]
array_int = [1, 2, 3, 4]

def remove_str(arr):
    print(arr)
    val = input("Select the item you want to remove>>> ")
    if val not in arr:
        print("Input not in array\n")
    else:
        arr.remove(val)
        print(arr)
        print("\n")
    
    
def remove_int(arr):
    print(arr)
    val = input("Select the item you want to remove>>> ")
    if int(val) not in arr:
        print("Input not in array")
    else:
        arr.remove(int(val))
        print(arr)
        print("\n")
        
        
remove_str(array_str)
remove_int(array_int)

Hope it was helpful.
Thanks for reading!!!