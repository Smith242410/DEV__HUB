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

