class Poly():
    def __init__(self,*args):
        self.coeff=list(args)
    
    def __add__(self,other):
        max_poly=max(len(self.coeff),len(other.coeff))

        self.coeff=[0]*(max_poly-len(self.coeff))+self.coeff
        self.coeff=[0]*(max_poly-len(other.coeff))+other.coeff
        
        results=[i+j for i,j in zip(self.coeff,other.coeff)]
       
        return Poly(*results)
        
        
        
    def __repr__(self):
        return f"Poly({', '.join(map(str,self.coeff))})"
            

if __name__ == '__main__':
    a = Poly(1,2,3)  
    b = Poly(1,0,1,1,2,3)
    c=Poly(1,1,1,1,1,1,1)
    d = a+b+c 
    c=a+b
    print(c) 
    print(d)