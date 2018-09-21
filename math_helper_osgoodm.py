from math import *
from time import sleep

#function = input("What formula would you like to utilize today? ")

def midpoint(x1,y1,x2,y2):
    ''' prints the midpoint between two coordinates (x1,y1) and (x2,y2)
    
    >>> midpoint(-3,3,5,3)
    The midpoint between (-3,3) and (5,3) is (1.0,3.0)
    
    >>> midpoint(6,12,15,17)
    The midpoint between (6,12) and (15,17) is (10.5,14.5)
    
    >>> midpoint(100,-10,26,40)
    The midpoint between (100,-10) and (26,40) is (63.0,15.0)
    
    >>> midpoint(3,2,3,0)
    The midpoint between (3,2) and (3,0) is (3.0,1.0)
    
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
    print("The midpoint between ({},{}) and ({},{}) is ({},{})".format(x1,y1,x2,y2,x,y))
    
    
def herons_formula(s1,s2,s3):
    '''prints the area of the triangle, given three sides (s1,s2,s3)
    >>> herons_formula(48,26,26)
    The area of the triangle is 240.0
    
    >>> herons_formula(6,8,10)
    The area of the triangle is 24.0
    
    >>> herons_formula(8,15,17)
    The area of the triangle is 60.0
    
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
    
    >>> herons_formula(1,2,3)
    Traceback (most recent call last):
        ...
    ValueError: side lengths must agree with Triangle Inequality Theorem
        
    '''
    
    if s1 <= 0 or s2 <=0 or s3 <= 0:
        raise ValueError("sides must be positive")
    
    if s1+s2<=s3 or s2+s3<=s1 or s1+s3<=s2:
        raise ValueError("side lengths must agree with Triangle Inequality Theorem")
    
    s = (s1+s2+s3)/2
    area = sqrt(s*(s-s1)*(s-s2)*(s-s3))
    r_area = round(area, 3) 
    print("The area of the triangle is {}" .format(r_area))
    
def v_cylinder(r,h):
    '''prints the area for the volume of a cylinder, given the radius (r) and height(h)
    >>> v_cylinder(4,10)
    The volume of the Cylinder is 502.65
    
    >>> v_cylinder(7,2)
    The volume of the Cylinder is 307.88
    
    >>> v_cylinder(2.5,2.5)
    The volume of the Cylinder is 49.09
    
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
    print("The volume of the Cylinder is {}".format(v_cyl_round))
    
def v_cone(r, h):
    '''prints the volume of a cone given the radius and the height
    >>> v_cone(4,6)
    The volume of the cone is 100.53
    
    >>> v_cone(7,7)
    The volume of the cone is 359.19
    
    >>> v_cone(100,2)
    The volume of the cone is 20943.95
    
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
    print("The volume of the cone is {}".format(vol_cone_round))
    
def sa_sphere(r):
    '''prints the surface area of a cube given the radius
    >>> sa_sphere(2)
    The surface area of the sphere is 50.27
    >>> sa_sphere(15)
    The surface area of the sphere is 2827.43
    
    >>> sa_sphere(.5)
    The surface area of the sphere is 3.14
    
    >>> sa_sphere(21)
    The surface area of the sphere is 5541.77
    
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
    print("The surface area of the sphere is {}".format(round_sphere_sa))
    
def midpoint_calc():
    x1 = float(input("What is your first x-coordinate? " ))
    y1 = float(input("What is your first y-coordinate? " ))
    x2 = float(input("What is your second x-coordinate? " ))
    y2 = float(input("What is your second y-coordinate? " ))
    
    midpoint(x1,y1,x2,y2)
    sleep(2)
    print()
    
def herons_calc():
    s1 = float(input("What is the length of the first side? "))
    s2 = float(input("What is the length of the second side? "))
    s3 = float(input("What is the length of the third side? "))
    
    herons_formula(s1,s2,s3)
    sleep(2)
    print()

def vol_cyl_calc():
    r = float(input("What is the length of the radius? "))
    h = float(input("What is the height? "))
    
    v_cylinder(r,h)
    sleep(2)
    print()

def vol_cone_calc():
    r = float(input("What is the length of the radius? "))
    h = float(input("What is height? "))
    
    v_cone(r,h)
    sleep(2)
    print()
    
def sa_sphere_calc():
    r = float(input("What is the length of the radius? "))
    
    sa_sphere(r)
    sleep(2)
    print()
    
    
    
def main():
    while True:
        print("Hello, welcome to the math helper!")
        print("(a) Midpoint Formula")
        print("(b) Heron's Formula")
        print("(c) Volume of a Cylinder")
        print("(d) Volume of a Cone")
        print("(e) Surface area of a Sphere")
        print("-Type 'exit' if you would like to leave the program")
        function = input("What formula would you like to use today? ")
        
        if function == "a":
            midpoint_calc()
            
        elif function == "b":
            herons_calc()
            
        elif function == "c":
            vol_cyl_calc()
            
        elif function == "d":
            vol_cone_calc()
            
        elif function == "e":
            sa_sphere_calc()
            
        elif function == "exit":
            break
            
    
        
        

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()
    

