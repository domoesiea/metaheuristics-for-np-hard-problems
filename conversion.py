import sys


if len(sys.argv) < 3:
    print("Il manque des arguments")
else:
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    file.close()
    n, m = int(lines[0].split()[0]), int(lines[0].split()[1])
    print(n,m)

    c=[]
    v=[]
    for i in range(1,n+1):
        c.append(int(lines[i].split()[1]))
        v.append([])


    for i in range(n+1,len(lines)):
        v[int(lines[i].split()[0])].append(int(lines[i].split()[1]))
        if(int(lines[i].split()[0]) not in v[int(lines[i].split()[1])]):
            v[int(lines[i].split()[1])].append(int(lines[i].split()[0]))
    print(v[-1])

    with open(sys.argv[2], 'w') as file:
        file.write("Maximize\n")
        file.write("z: ")
        for i in range(0,len(c)):
            if(i!=len(c)-1):
                file.write(str(c[i])+" x"+str(i)+" + ")
            else:
                file.write(str(c[i])+" x"+str(i)+"\n")
        file.write("Subject To\n")  
        index=[]
        for i in range(len(c)):
            for j in range(len(c)):
                if(j not in v[i] and j>i):
                    file.write("x"+str(i)+" + "+"x"+str(j)+" <= 1\n")
                    
        file.write("Binaries\n")  
        for i in range(0,len(c)):
            file.write("x"+str(i)+"\n")
        file.write("End")
