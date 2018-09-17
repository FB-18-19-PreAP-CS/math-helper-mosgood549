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
    '''
    s = (s1+s2+s3)/2
    area = sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print(area)

#def main():
    
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    #main()
    
    