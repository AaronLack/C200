#All Work Here Is Solely Mine

def windChill(T,V):
   return (35.74 + (.6215*T) - (35.75*V**.16) + (.4275*T*V**.16))
    
print(windChill(25,5))