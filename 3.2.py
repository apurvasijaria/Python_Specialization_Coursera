try:
    hrs = raw_input("Enter Hours:")
    h=float(hrs)
    rate = float(raw_input("Enter rate:"))
    if (h<40.0):
        pay=h*rate
    else:
        pay=40.0*rate +(h-40.0)*rate*1.5

    print pay
except:
    print ('please enter numneri value')
