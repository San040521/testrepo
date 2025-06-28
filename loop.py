smallest = None 
largest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print("Invalid input")
        
    if largest is None or n > largest:
        largest = n
        
    if smallest is None or n < smallest:
        smallest = n
        
print("Maximum is", largest)
print("Minimum is", smallest)
