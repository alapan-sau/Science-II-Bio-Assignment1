def mapper(dna, re):
    dna = dna.upper()
    dna = dna.replace("\n", "")
    dna = dna.replace("\r", "")

    re = re.upper()
    cuts = []

    for i in range(-3,len(dna)-3):
        if re == dna[i:i+4]:
            if(i<0):
                cuts.append(dna(len)+i+1)
            else:
                cuts.append(i+1) # for one-based indexing of the end points


    start = []
    end = []
    length = []

    for i in range(0,len(cuts)):
        end.append(cuts[i])
        start.append(cuts[i-1]+1)
        if(cuts[i-1]+1 > cuts[i]):
            length.append(len(dna) - (cuts[i-1] - cuts[i]))
        else:
            length.append(cuts[i] - (cuts[i-1]+1) + 1)


    print(' #    start       end    size')
    for i in range(0,len(length)):
        print("%2d    %5d     %5d   %5d" % (i,start[i], end[i],length[i]))



dna_file = open("./pbr322dna.txt","r")
dna= dna_file.read()
re = 'tcga'
mapper(dna, re)