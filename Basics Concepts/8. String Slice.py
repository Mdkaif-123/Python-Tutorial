name = "Harry"
print(name[0:3]) # from 0 to 2 index not 3
print(name[ : 4]) # auto 0 at beginning 
print(name[ 1: ]) # auto len at last
print(name[-4:-2]) 
# this is  something like 
print(name[len(name)-4:len(name)-2]) 