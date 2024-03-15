print("hello world")
# let variable = 21;
name = "Mark"
last_name = "Sanchez"
total = 13.00
age = 40
found = True
# if / else statement
# if(var==var2){
# logic
#}
if age > 35:
    print("you are older")
    print("Time has been good to you")
elif age == 1:
    print("you are young")
else:
    print("you are an adult")

#function
#function say hello(){}

def say_hello():
    print("hello there")

def say_goodbye(name):
    print("Goodbye " + name)

#call a function
say_hello()
say_goodbye("Mark")

#concatenate
print("hello my name is " + name + "and i am " + str(age) +" years old")


#array
#list

colorList = ["white","red","black","blue"]
numberList = ["1,2,3,4,5,6,7,8"]


#add
colorList.append("yellow")


#travel the list
for temp in colorList:
    print(temp)
#for(i=0;color.length;i++) --this is the JavaScript
    #let temp = color[i]
    # console.log(temp)

#dictionary
me ={
    "first_name":"Mark",
    "month":"January",
    "last_name":"Sanchez",
    "age":40
}
print(me["first_name"])

me["age"]=45
me["color"]="Blue"
print(me)