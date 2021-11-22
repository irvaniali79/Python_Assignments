class Complex:
    def __init__(self,real,imagein) :
        self.real=real
        self.imagein=imagein

    def __add__(self,complex):
        
                
        return Complex(self.real+complex.real, self.imagein+complex.imagein)



    def __sub__(self,complex):
        
        return Complex(self.real-complex.real, self.imagein-complex.imagein)
        

    def __mul__(self,complex):

        return Complex(self.real*complex.real+self.imagein*complex.imagein, \
                        self.imagein*complex.real+self.real*complex.imagein)

    def __str__(self):
        Str=""
        if(self.imagein<0):
            Str=f"{self.imagein}"
        elif self.imagein==0:
            Str=""
        else:
            Str=f"+ {self.imagein}"
        return str(self.real)+Str