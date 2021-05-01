def find_sites(dna):
    sizes = [4,6,8]
    dna = dna.upper()
    dna = dna.replace('\n','')
    dna = dna.replace('\r','')

    # print(dna)
    inv = {
        'C':'G',
        'G':'C',
        'T':'A',
        'A':'T'
    }
    print('  #      start       end           site    size')
    print('-----------------------------------------------')
    count =1
    for size in sizes:
        for i in range(-size+1,len(dna)+1-size):
            lo = i
            hi = i+size-1

            flag = 1
            while(lo < hi ):
                if(inv[dna[lo]]==dna[hi] and inv[dna[hi]]==dna[lo]):
                    lo+=1
                    hi-=1
                else:
                    flag=0
                    break
            if(flag==1):
                if(i>=0):
                    print("%3d     %5d      %5d       %8s    %4d"%(count, i+1, i+size, dna[i:i+size],size))
                else:
                    k = i+len(dna)+1
                    site = dna[i:]+dna[0:i+size]
                    print("%3d     %5d      %5d       %8s    %4d"%(count, k, i+size, site,size))
                count+=1


# Implemented for circular Sequence
dna_file = open("pbr322dna.txt","r")
dna= dna_file.read()
find_sites(dna)