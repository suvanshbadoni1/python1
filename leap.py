n=int(input())
def leap():
    if n >=1900 :
        if ( (n%100)==0 or  (n%4==0)) :
            return True
        else :
            return False
print(leap())
     
