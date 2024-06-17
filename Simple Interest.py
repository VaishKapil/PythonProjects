def simple_interest(p,t,r):
    print("The Principal is",p)
    print("The Time period is",t)
    print("The Rate of interest is",r)
    si=(p*t*r)/100
    print("The simple interest is",si)
    return si

simple_interest(1000,3,10)