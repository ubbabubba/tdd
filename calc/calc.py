# Class
class Calc:
    def add(self,*s):
        return sum(s)

    def mult(self,*s):
        i = 1
        for x in s:
            i= i*x
        return i



