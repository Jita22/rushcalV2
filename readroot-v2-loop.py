# Read the input files from the iplist.txt
ipfile = open('iplist.txt', 'r')
inpaths = ipfile.readlines()
for line in inpaths:
    inpath = line.strip()
    print(inpath)
    exec(open("readroot-v2.py").read())