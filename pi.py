# Initilize denominator 
k = 1
  
# Initilize sum 
s = 0
  
for i in range(10000000): 
  
    # even index elements are positive 
    if i % 2.0 == 0: 
        s += 4.0/k 
    else: 
  
        # odd index elements are negative 
        s -= 4.0/k 
  
    # denominator is odd 
    k += 2.0
      
print(s) 
