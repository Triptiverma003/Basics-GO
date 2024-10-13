class vault:
    def __init__(self , galleons = 0, knuts =0 ,sickuls=0):
        self.galleons = galleons
        self.knuts = knuts
        self.sickuls =sickuls
    def __str__(self):
        return f"{self.galleons} galleons , {self.knuts} knuts , {self.sickuls} sickuls"    

potter = vault(100 , 50 ,25)
print(potter)