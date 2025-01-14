thing = int(input("a "))
i=0

def checkthing(thething):
    if thething % 2 == 0:
        # Even 
        thething = thething/2
    else:
        #odd
        thething = (thething*3)+1
    return(thething)

x=3
while x != 0:
    thing=checkthing(thing)
    i+=1
    print(f"{thing} {i}")
    if thing==1:
        x-=1


