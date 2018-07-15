    
import re
myfile = open("C:\\Users\\Admin\\Desktop\\Sample1.log")
#print(myfile.read())
#index_count=0
d={}
for i in myfile.readlines():
    #print(i)
    ip = re.findall( '[0-9]+(?:\.[0-9]+){3}', i )
    sec=re.findall('[0-9]+[m][s]',i)
    key=''.join(ip)
    value=''.join(sec)
    #re.findall( r'\d+(?:\.\d+){3}'
    #print(key,value)
    #print(re.findall('[0-9]+[m][s]',i))
    #if re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)",i):
    #print("d{3}.d{2}.d{2,3}.d{2,3}",i)
    #index_count += 1
    #print(''.join(*match))
    # m = re.match(r"(\d+)\.(\d+)", "24.1632")
    if key in d:
        d[key].append(int(value.replace('ms','')))
    else:
        d[key]=[int(value.replace('ms',''))]
print(d)
for key,items in d.items():
    sumtotal=0
    for item in items:
        sumtotal=sumtotal+item
    print(key,sumtotal)



