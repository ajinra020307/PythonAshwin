
#read the file

file = open('document.txt','r')
content = file.read()
newString = ''
# change a to b.
for x in range(0,len(content)):
    
    if content[x] == 'a':
        newString = newString + 'b'
    else:
        newString = newString + content[x]    
# write the file

file = open('document.txt','w')
file.write(newString)


