# thing = int(input("a "))
i=0
h={}
def checkthing(thething):
    if thething % 2 == 0:
        thething = thething/2
    else:
        thething = (thething*3)+1
    return(thething)
x=1
for thing in range(10,100):
    g = thing
    while thing != 1:
        thing=checkthing(thing)
        i+=1
        print(f"{thing} {i}")
    h[g]=i
    i=0
print(h)
print("\n\n")
h = sorted(h.items(), key=lambda x: x[1], reverse=False)
m=0
for i in h:
    m+=1
    print(str(m)+". | "+str(i[0])+" took "+str(i[1])+" moves")