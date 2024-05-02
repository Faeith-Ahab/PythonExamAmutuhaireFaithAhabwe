# a ) i)

def grade_student(python_mark):


    if python_mark == int(python_mark):
        pass
    else:
            print('invalid input')
    if python_mark>=90 and python_mark<=100 and python_mark:
        print(f" Grade is A ")
        
    elif python_mark>=80 and python_mark<=89:
        print(f" Grade is B ")
        
    elif python_mark>=70 and python_mark<=79:
        print(f" Grade is C ")
        
    elif python_mark>=60 and python_mark<=69:
        print(f" Grade is D ")
        
    elif python_mark>=50 and python_mark<=59:
        print(f" Grade is E ")
        
    else:
        print(f"Fail ")
    
    
grade_student(40)
grade_student(80)
grade_student(100)



# a) ii) 

def convertTemperature():

    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius ")

    option = int(input("Select your choice (1 or 2): "))

    if option == 1:
        celsius =  float(input("Enter temperature in Celsius value: "))
        fahrenheit  = (9/5 * celsius) + 32
        print(f"{celsius}° C is equal to {fahrenheit}°F")

    elif option == 2:
        fahrenheit =  float(input("Enter temperature in Fahrenheit value: "))
        celsius  = 5/9 * (fahrenheit -32 )
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Error: Invalid option!") 
convertTemperature()   



# b ) i)

base = int(input('Input base of the triangle: '))
height = int(input('Enter the height of the triangle: '))

def areaOfTriangle(b,h):

    area = (1/2) * b * h

    print(int(area))

areaOfTriangle(base,height)



#  b ) ii)

def sum_this_list():

    listed = [9,2,3,5,8]
    sum = 0

    for l in listed:
        sum += l
    print( str(sum))  
    
sum_this_list()


