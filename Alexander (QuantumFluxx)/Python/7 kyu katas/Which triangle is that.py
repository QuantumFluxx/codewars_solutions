def type_of_triangle(a, b, c): 
    tup = (a,b,c)
    triangles = {1: "Equilateral",
                 2: "Isosceles",
                 3: "Scalene"}
    
    if all(isinstance(n, int) for n in tup) and (a+b)>c and (b+c)>a and (a+c)>b:
        msg = triangles.get(len(set(tup))) 
    else:
        msg = "Not a valid triangle"
    
    return msg