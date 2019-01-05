# Rezwana Kabita





def minutes_to_miliseconds(minutes_float):
     miliseconds = minutes_float * 60000
     print "miliseconds:", miliseconds



def average_exam_score(exam1,exam2):
    average = (exam1 + exam2)/2
    print ("average:", average)


import math
def roots_of_quadratic(a,b,c):
    d = (b**2) - (4*a*c)

    x = (-b-math.sqrt(d))/(2*a)
    y = (-b+math.sqrt(d))/(2*a)
    print ("roots are:",x, "," ,y, "\n")


def kelvin_to_reamur(k):
    reamur = (k - 273.15) * 0.8
    print ("kelvin", k)


def reamur_to_celcius(k):
    celcius = float(k * 1.25)
    print ("celcius:", celcius)



def count_marble_fit(n):
    vol = n ** 3
    vol_of_marble = (4/3)* math.pi * ((n/4)** 3)
    fit_marble = vol // vol_of_marble
    print ("the number of marble fits in this cube:" , fit_marble)



def Print_output():
   string = "^ - ^ - ^"
   string2 = "i"
   print (string*4, "^")
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string*4,"^"
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string*4,"^"
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string*4,"^"
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string2,"      ",string2,"      ",string2,"      ",string2,"       ",string2
   print string*4,"^"












minutes_to_miliseconds(int(input))
average_exam_score(24,20)
roots_of_quadratic(1,2,1)
kelvin_to_reamur(280)
reamur_to_celcius(280)
count_marble_fit(50)
Print_output()





