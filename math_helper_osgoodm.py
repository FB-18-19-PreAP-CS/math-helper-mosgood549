from math import *

#function = input("What formula would you like to utilize today? ")

def midpoint(x1,y1,x2,y2):
    ''' returns the midpoint between two coordinates (x1,y1) and (x2,y2)
    
    >>> midpoint(-3,3,5,3)
    (1.0,3.0)
    
    >>> midpoint(4,1,10,5)
    (7.0,3.0)
    
    >>> midpoint(-2,5,7,7)
    (2.5,6.0)
    
    '''
    x = (x1+x2)/2
    y = (y1+y2)/2
    print("({},{})".format(x,y))
    
    
def herons_formula(s1,s2,s3):
    '''prints the area of the triangle, given three sides (s1,s2,s3)

    >>> herons_formula(48,26,26)
    240.0
    
    >>> herons_formula(6,8,10)
    24.0
    
    >>> herons_formula(8,15,17)
    60.0
    
    There are no negative triangle lengths
    >>> herons_formula(5,-10,12)
    Traceback (most recent call last):
        ...
    ValueError: sides must be positive
    
    Triangle Inequality Theorem: any two sides must be greater than the third side
    >>> herons_formula(6,2,10)
    Traceback (most recent call last):
        ...
    ValueError: side lengths must agree with Triangle Inequality Theorem
        

    
    '''
    
    if s1 <= 0 or s2 <=0 or s3 <= 0:
        raise ValueError("sides must be positive")
    
    if s1+s2<s3 or s2+s3<s1 or s1+s3<s2:
        raise ValueError("side lengths must agree with Triangle Inequality Theorem")
    
    
    
    
    
    
    
        
    s = (s1+s2+s3)/2
    area = sqrt(s*(s-s1)*(s-s2)*(s-s3))
    r_area = round(area, 3) 
    print(r_area)
    

#def main():
    
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    #main()
    
    