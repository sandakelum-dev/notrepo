import glob

url = "https://raw.githubusercontent.com/wijewardhane/notrepo/main/stickers/packs/"

slist = glob.glob("*.webp")

print(slist)

pn  = input("enter pack id")
pname = "pack%s.json"%(pn)
f = open(pname,"a")

stl = ""

for s in slist:
    # print(s)
    stl = stl+'"'+s+'",\n'

f.write('{\n "url":"%s%s/",\n "list":[\n%s\n] \n}'%(url,pn,stl))
f.close()