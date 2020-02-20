class Geek: 
  
    # Variable defined inside the class. 
    inVar = 'inside_class'
    print("Inside_class2", inVar) 
  
    def access_method(self, myVar): 
        print("Inside_class3", Geek.inVar) 
  
uac = Geek() 
uac.access_method() 