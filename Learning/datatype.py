#LIST
#list are mutable 
#slicing 
numbers = [10, 20, 30, 40, 50, 60]
new_numbers = numbers[2: 5]
print(new_numbers)
#append is used to add at the end of the list
#Tuples 
#tuples are immutable
numbers = (10, 20, 30, 40, 50, 60)
new_numbers = numbers[2: 5]
print(new_numbers)
#STRING
#Replacing a character
animal = "Rat"

new_animal = "C" + animal[1: ]
print(new_animal)
#DICTIONARIES 
dic = {
    1:"Haaland",
    2:"Yamal",
    3:'Rafa'
    
}
for i in dic:
    values = dic[i]
    print(f"{i}-> {values} ")


    #SET
    domestic_animals = {'dog', 'cat', 'elephant'}
wild_animals = {'lion', 'tiger', 'elephant'}

# union of sets
animals = domestic_animals | wild_animals #| is union & is intersection
print(animals)

#Conversion of data type 
#list() converts to list 
number = list({1,2,3})
print(number)
#same for tuple is tuple()
#dict() for dictionary
#set() for set
def user_define():
    number =input("Enter what you want to store").split()
    se = input("What data type do you want ? (set|list|tuple|dict)")
    if se == 'set':
        n = set(number)
        print(n)
    elif se =='list':
         n = list(number)
         print(n)
    elif se == 'tuple':
        n = tuple(number)
        print(n)
    elif se == 'dict':
        values = input("Enter Values for keys for dict (separated by space): ").split()
        n = dict(zip(number, values))
        print(n)
    else:
        print("error")
           

user_define()

######





