#def main():
 #   column(3)

#def column(height):
 #   print ('#\n' * height , end = "" )
    
#main()

def main():
    brick(3)

def brick (size):
    for i in range(size):
        for j in range(size):
            print('#' , end = '')
        print()
    print()

main()    