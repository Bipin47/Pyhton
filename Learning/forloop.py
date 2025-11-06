name  = input('Enter your name: ')
i =0

for item in name:
    i = i+1
print(f"your name contains {i} letters ")


#list = ['name','location']
alist = ['python','java','c++','html','c#']
total = 0
for i in alist:
    total = total+1
    if i == ' java':
        continue
    elif i =='c#':
        print(f"C# is at {total} number in a list")
    
