
ssn = open("ssn.txt", "w+")

x = range(9)

for a in x:
    for b in x:
        for c in x:
            for d in x:
                for e in x:
                    for f in x:
                        for g in x:
                            for h in x:
                                for i in x:
                                    ssn.write("{}{}{}-{}{}-{}{}{}{}".format(a,b,c,d,e,f,g,h,i)+"\n")