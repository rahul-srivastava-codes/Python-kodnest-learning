# addition in scripting style
print("Hello world")
a = 1
b=56;
print(a+b);

# 1)python is dynamically typed language as programmer do not have to mention the data type
'''
above see multiple line comment
data type allocated  by python 
based on value stored into 
variable
'''
# 2) It is most concise programming language means in minimum words we will do maximum task

# addition in procedural style
def add(a,b):
  print(a+b);

add(10,20);

# addition in OOPs style
class add:
  def add(self,a,b):
    print("Addition is:", a+b)

d1 = add();
d1.add(10,20);

print('A')
print('B')

# do you want to print in same line ?
print('A' , end='-')
print('B')