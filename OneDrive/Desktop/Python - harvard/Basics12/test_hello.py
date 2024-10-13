from hello import hello

def test_hello():
   assert hello("tripti") == "hello tripti"
   assert hello() == "hello world"
   
def test_default():
    for name in ["aanchal" , "tripti" , "ram"]:
        assert hello(name) == f"hello {name}"