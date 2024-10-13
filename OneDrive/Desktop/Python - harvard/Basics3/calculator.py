# Compute the sum
#x = int(input("What is x: "))
#y = int(input("What is y: "))
##z = x + y

# Print the formatted result
##print(f"{z:,}")


def main():
    x = int(input("what is x:"))
    print("square of x is:" , square(x))


def square(n):
    return pow(n , 2)

main()