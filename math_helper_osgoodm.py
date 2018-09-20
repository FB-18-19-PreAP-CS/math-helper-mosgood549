from math import *

#function = input("What formula would you like to utilize today? ")

def midpoint(x1,y1,x2,y2):
    ''' prints the midpoint between two coordinates (x1,y1) and (x2,y2)
    
    >>> midpoint(-3,3,5,3)
    (1.0,3.0)
    
    >>> midpoint(6,12,15,17)
    (10.5,14.5)
    
    >>> midpoint(100,-10,26,40)
    (63.0,15.0)
    
    >>> midpoint(3,2,3,0)
    (3.0,1.0)
    
    There cannot be a midpoint between the same points
    >>> midpoint(2,3,2,3)
    Traceback (most recent call last):
        ...
    ValueError: midpoint requires 2 different coordinates
    
    '''
    if x1 == x2 and y1 == y2:
        raise ValueError("midpoint requires 2 different coordinates")
    
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
    
def v_cylinder(r,h):
    '''prints the area for the volume of a cylinder, given the radius (r) and height(h)
    >>> v_cylinder(4,10)
    502.65
    
    >>> v_cylinder(7,2)
    307.88
    
    >>> v_cylinder(2.5,2.5)
    49.09
    
    A cylinder can't have a negative radius length
    >>> v_cylinder(-2, 5)
    Traceback (most recent call last):
        ...
    ValueError: the radius must be positive
    
    A cylinder cannot have a negative height length
    >>> v_cylinder(8,-5)
    Traceback (most recent call last):
        ...
    ValueError: the height must be positive
    
    '''
    if r <= 0:
        raise ValueError("the radius must be positive")
    
    if h <= 0:
        raise ValueError("the height must be positive")
        
    volume_cyl = pi*((r**2)*h)
    v_cyl_round = round(volume_cyl, 2)
    print(v_cyl_round)
    
def v_cone(r, h):
    '''prints the volume of a cone given the radius and the height
    >>> v_cone(4,6)
    100.53
    
    >>> v_cone(7,7)
    359.19
    
    >>> v_cone(100,2)
    20943.95
    
    A cone can't have a negative radius length
    >>> v_cone(-20, 17)
    Traceback (most recent call last):
        ...
    ValueError: the radius must be positive
    
    A cylinder cannot have a negative height length
    >>> v_cone(40,-10)
    Traceback (most recent call last):
        ...
    ValueError: the height must be positive
    
    
    '''
    if r <= 0:
        raise ValueError("the radius must be positive")
    
    if h <= 0:
        raise ValueError("the height must be positive")
    
    volume_cone = pi*((r**2)*(h/3))
    vol_cone_round = round(volume_cone, 2)
    print(vol_cone_round)
    
def sa_sphere(r):
    '''prints the surface area of a cube given the radius

    >>> sa_sphere(2)
    50.27

    >>> sa_sphere(15)
    2827.43
    
    >>> sa_sphere(.5)
    3.14
    
    >>> sa_sphere(21)
    5541.77
    
    The radius of a sphere cannot be negative
    >>> sa_sphere(-7)
    Traceback (most recent call last):
        ...
    ValueError: the radius must be positive
    '''
    
    if r <= 0:
        raise ValueError("the radius must be positive")
    
    sphere_sa = 4*pi*(r**2)
    round_sphere_sa = round(sphere_sa, 2)
    print(round_sphere_sa)
    
#def main():
    
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    #main()
    
