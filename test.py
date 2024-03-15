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
print("hello my name is " + name + "and i have " + str(age) +" years old")














# function say_hello(){}

def say_hello():
    print("hello there")

    def say_goodbye(name):
        print("Goodbye " + name)

    