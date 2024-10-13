import sys
#if len(sys.argv) < 2:
   # print("Too few argument")
#elif len(sys.argv) >2:
  #  print("Too many arguments")
#else:
 #   print("my name is:" , sys.argv[1])
  
for arg in sys.argv[1:-1]:
    print("hello my name is" , arg)  
