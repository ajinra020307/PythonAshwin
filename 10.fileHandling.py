
# read

file = open('sample.txt','r')
content = file.read()

print(content)

# create a mew file and write into it

file2 = open('hello.txt','w+')
file2.write('Hello world')

