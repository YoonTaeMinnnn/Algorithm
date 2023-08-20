from math import gcd

#gcd : 최대공약수 

def solution(arrayA, arrayB):
    answer = 0
    
    def GCD(array):
        com = 0
        for i in array:
          com = gcd(com, i)
        return com
    
    def com_gcd(array, com):
        for i in array:
            if i % com == 0:
                break
        else:
            return com
        return 0
                
        
    a_gcd, b_gcd = GCD(arrayA), GCD(arrayB)
    
    return max(com_gcd(arrayB, a_gcd), com_gcd(arrayA, b_gcd))
     
 
