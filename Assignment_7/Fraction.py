import math


class Fraction:

    def __init__(self,numerator,denumerator):
        self.numerator=numerator
        self.denumerator=denumerator


    def __add__(self,fraction):
        
                
       return self.simplify_fraction(Fraction(self.numerator*fraction.denumerator + self.denumerator*fraction.numerator, self.denumerator*fraction.denumerator))


    
    def __sub__(self,fraction):
     
       return self.simplify_fraction(Fraction(self.numerator*fraction.denumerator - self.denumerator*fraction.numerator, self.denumerator*fraction.denumerator))
        

    def __mul__(self,fraction):

        return self.simplify_fraction(Fraction(self.numerator*fraction.numerator,self.denumerator*fraction.denumerator))

    def __truediv__(self,fraction):

        return Fraction(self.numerator*fraction.denumerator,self.denumerator*fraction.numerator)
    def __str__(self):
        return str( self.numerator)+"/"+str(self.denumerator)


    def simplify_fraction(self,fraction):

       
        common_divisor = math.gcd(fraction.numerator, fraction.denumerator)
        (reduced_num, reduced_den) = (fraction.numerator / common_divisor, fraction.denumerator / common_divisor)
    

        if reduced_den == 1:
            fraction.numerator=reduced_num
            return fraction
        elif common_divisor == 1:
            return fraction
        else:
            fraction.numerator=reduced_num
            fraction.denumerator=reduced_den
            return fraction


num=Fraction(3,3)

num2=Fraction(4,6)

print(num+num2)