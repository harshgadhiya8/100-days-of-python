''' scope '''

a=1
b=6
def scope():
    global b
    ''' use global keyword when 
    using global variable in local scope'''
    a=2
    b+=1
    print(b)
    print(f"scope {a}")
scope()
print(f"Normal {a}")