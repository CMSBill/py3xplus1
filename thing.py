thing = int(input("a "))
i=0
while thing != 0:
    if thing % 2 == 0:
        # Even 
        thing = thing/2
    else:
        #odd
        thing = (thing*3)+1
    i+=1
    print(f"{thing} {i}")

