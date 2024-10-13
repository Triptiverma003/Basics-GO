from calculator2 import square
import pytest
def main():
  test_calc2()
    
def test_calc2():
    #if square(2)!=4:
     #   print("4 is not square of 2")
    
    #if square(3)!=9:
    #   print("9 is not a square of 3")
    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print("4 was not a square of 2")
    # try:    
    #  assert square(3) == 9
    # except AssertionError:
    #     print("9 was not a square of 3")
    # try:    
    #  assert square(-3) == 9
    # except AssertionError:
    #     print("9 was not a square of -3")
        
    # try:    
    #  assert square(-2) == 4
    # except AssertionError:
    #     print("4 was not a square of -2")
        
# if __name__ == "__main__":
#    main()

    #assert square(3) == 9
    def test_str():
        with pytest.error(TypeError):
            square("cat")