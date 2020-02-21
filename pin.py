pin = open("sixdigitpin.txt", "w+")

x = range(9)

for a in x:
    for b in x:
        for c in x:
            for d in x:
                for e in x:
                    for f in x:
                        pin.write("{}{}{}{}{}{}".format(a,b,c,d,e,f)+"\n")