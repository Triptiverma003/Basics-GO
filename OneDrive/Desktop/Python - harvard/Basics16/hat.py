import random
class Hat:
    houses = ["faridabad" , "noida" , "delhi"]
    @classmethod
    def sort(cls,name):
        print(name ,"is in" , random.choice(cls.houses))
    
Hat.sort("harry")
