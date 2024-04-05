import turtle
import math
import sys
import datetime
import time

wn = turtle.Screen()
wn.colormode(255)
start_color = (255, 204, 153)
new_color = start_color
wn.bgcolor(start_color)



second_color_step_size = 4
third_color_step_size = 2

tom = turtle.Turtle()
tom.color(0,0,0)
tom.pensize(10)

#now = datetime.datetime.now()
now = time.ctime()

light_hours = {(255, 204, 153) : "07:00:00", (255, 221, 187) : "08:00:00", (255, 238, 221) : "09:00:00",
                   (255, 255, 255) : "10:00:00", (255, 255, 221) : "11:00:00", (255, 255, 204) : "12:00:00",
                   (255, 255, 187) : "13:00:00", (255, 238, 170) : "14:00:00", (255, 221, 153) : "15:00:00",
                   (255, 204, 136) : "16:00:00", (255, 187, 119) : "17:00:00", (255, 170, 102) : "18:00:00" }

color_slot = 0
target1 = 1
target2 = 2


for i in list(light_hours.keys()):
        if i == new_color:
                #print(light_hours[i])
                continue
#print(new_color)
#in this case, target1 and target2 are both 255
done_all = True
while done_all:
        done_up = True
        while done_up:
                while new_color[1] + second_color_step_size < list(light_hours.keys())[color_slot][target1] + 1:  #begin with list(light_hours.keys())[color_slot][target1] will increment
                        start_color = (start_color[0], start_color[1] + second_color_step_size, start_color[2])
                        #print(start_color)
                        remainder = (list(light_hours.keys())[color_slot][target1]) - start_color[1]
                        #print(remainder)
                        new_color = (start_color[0], start_color[1], start_color[2])
                        print(new_color)
                        wn.bgcolor(new_color)
                        time.sleep(.1)
                        if remainder > 0 and remainder < second_color_step_size:
                                new_color = (start_color[0], start_color[1] + remainder, start_color[2])
                                wn.bgcolor(new_color)
                                time.sleep(.1)
                        else:
                                continue
                        wn.bgcolor(new_color)
                #print(new_color)

                while new_color[2] + third_color_step_size < list(light_hours.keys())[color_slot][target2] + 1:
                        start_color = (start_color[0], new_color[1], start_color[2] + third_color_step_size)
                        #print(start_color)
                        remainder = (list(light_hours.keys())[color_slot][target2]) - start_color[2]
                        #print(remainder)
                        new_color = (start_color[0], start_color[1], start_color[2])
                        print(new_color)
                        wn.bgcolor(new_color)
                        time.sleep(.1)
                        if remainder > 0 and remainder < third_color_step_size:
                                new_color = (start_color[0], start_color[1], start_color[2] + remainder)
                                wn.bgcolor(new_color)
                                time.sleep(.1)
                        else:
                                continue
                        wn.bgcolor(new_color)
                if color_slot < 3:
                        color_slot += 1
                        #print(color_slot)
                else:
                        done_up = False
                #print(new_color)
        
                for i in list(light_hours.keys()):
                        if i == new_color:
                                #print(light_hours[i])
                                continue
        print(new_color)
        print("going up done")
                        
                #done_up = False
        #need two whlie loops running at the same time

        time.sleep(.1)

        '''
        #print(new_color)

        #in this case, target1 is 170 and target2 is 102
        done_down = True
        while done_down:
                while new_color[1] - second_color_step_size >= list(light_hours.keys())[color_slot][target1]:
                        start_color = (new_color[0], new_color[1] - second_color_step_size, new_color[2])
                        #print(start_color)
                        remainder = (abs(list(light_hours.keys())[color_slot][target1]) - start_color[1])
                        #print(remainder)
                        new_color = (start_color[0], start_color[1], start_color[2])
                        #print(new_color)
                        wn.bgcolor(new_color)
                        time.sleep(.1)
                        if remainder > 0:
                                new_color = (start_color[0], start_color[1] - remainder, start_color[2])
                                wn.bgcolor(new_color)
                                time.sleep(.1)
                        else:
                                continue
                        wn.bgcolor(new_color)
                #print(new_color)

                while new_color[2] - third_color_step_size >= list(light_hours.keys())[color_slot][target2]:
                        start_color = (new_color[0], new_color[1], new_color[2] - third_color_step_size)
                        #print(start_color)
                        remainder = (abs(list(light_hours.keys())[color_slot][target2]) - start_color[2])
                        #print(remainder)
                        new_color = (start_color[0], start_color[1], start_color[2])
                        #print(new_color)
                        wn.bgcolor(new_color)
                        time.sleep(.1)
                        if remainder > 0:
                                new_color = (start_color[0], start_color[1], start_color[2] - remainder)
                                wn.bgcolor(new_color)
                                time.sleep(.1)
                        else:
                                continue
                        wn.bgcolor(new_color)
                        
                for i in list(light_hours.keys()):
                        if i == new_color:
                                if i != "10:00:00":
                                        print(light_hours[i])

                if color_slot < len(light_hours) - 1:  
                        color_slot += 1
                        print(color_slot)
                else:
                       done_down = False
                print(new_color)
                for i in list(light_hours.keys()):
                        if i == new_color:
                                print(light_hours[i])
                wn.bgcolor(new_color)
        print("going down done")
'''
        if color_slot == 3: #len(light_hours.keys()) - 1:
                done_all = False

turtle.done()

#color_slot = 0

#Need to assign target variables, say maybe target1 and target2?
#Lets say list(light_hours.keys())[0] -> list(light_hours.keys())[i + 1] -> i should probably be = target1/2



'''
for i in range(10):
        new_color = (start_color[0], start_color[1] + color_step_size * i, start_color[2] + color_step_size * i)
        if new_color[1] < 255 and new_color[2] < 255:
        wn.bgcolor(new_color)
'''
'''
while True:
        for i in range(10):
        new_color = (start_color[0], start_color[1] + color_step_size * i, start_color[2] + color_step_size * i)
        if new_color[1] < 255 and new_color[2] < 255:
                tom.color(new_color)
                tom.forward(100)
                tom.right(90)
        for i in range(10):
        if new_color[1] <= 249 and new_color[2] <= 198:
                tom.color(start_color[0], 249 - color_step_size * i, 198 - color_step_size * i)
                tom.forward(100)
                tom.right(90)
'''
'''
while True:
        for i in range(10):
        new_color = (start_color[0], start_color[1] + color_step_size * i, start_color[2] + color_step_size * i)
        if new_color[1] < 255 and new_color[2] < 255:
                wn.bgcolor(new_color)
                time.sleep(.1)
        for i in range(10):
        if new_color[1] <= 249 and new_color[2] <= 198:
                wn.bgcolor(start_color[0], 249 - color_step_size * i, 198 - color_step_size * i)
                time.sleep(.1)
'''
'''
while True:
        for i in range(len(list(light_hours.keys()))):
        new_color = (list(light_hours.keys())[i][0], list(light_hours.keys())[i][1] + color_step_size * i, list(light_hours.keys())[i][2] + color_step_size * i)
        if new_color[1] <= 255:
                if new_color[2] <= 255:
                wn.bgcolor(new_color)
                time.sleep(.3)
                print(list(light_hours.values())[i])
##    for i in range(len(list(light_hours.keys()))):
##        if new_color[1] <= 249 and new_color[2] <= 198:
##            wn.bgcolor(start_color[0], 249 - color_step_size * i, 198 - color_step_size * i)
##            time.sleep(.1)
'''
#Here is a not-really-functional, basic version of the algorithm I want.
#Unfortunately, I will have to hard code each hours progress according to a specific pace.
#Rather than second and third _color_step_size, there would be different step sizes for each hour.
#Each hour needs a hard limit, set by the keys in light_hours. The progress from Hour A -> Hour B will be different every hour.
#Rather than range(len(list(light_hours.keys())), the range would be the mathematical perfect number of steps to get to the next color (hour).
'''
done = True
while done:
        for i in range(360):
        if new_color[1] < 221:
                start_color = (start_color[0], start_color[1] + second_color_step_size * i, start_color[2])
                new_color = (start_color[0], start_color[1], start_color[2])
                #increase stcolor 1
                #elif check stcolor 2
        elif new_color[2] < 187:
                start_color = (start_color[0], start_color[1], start_color[2] + second_color_step_size * i)
                new_color = (start_color[0], start_color[1], start_color[2])
                #increase stcolor 2
                #elif color 2 => 187
        elif new_color[2] >= 187:
                continue
                #stop increasing stcolor 2
                #else
        elif new_color[1] >= 221:
                #stop increasing stcolor 1
                continue
                wn.bgcolor(new_color)
                time.sleep(.3)
                print(new_color)
        done = False
        #you must get out of this loop / continue to the next one /
        #this should be the code for one hour increasing?
        #do this 12 more times (decreasing when necessary)

'''


'''
                #increase stcolor 1
                #elif check stcolor 2
        elif new_color[2] < 255:
                start_color = (start_color[0], start_color[1], start_color[2] + third_color_step_size)
                new_color = (start_color[0], start_color[1], start_color[2])
                wn.bgcolor(new_color)
                #increase stcolor 2
                #elif color 2 => 187
        elif new_color[2] >= 255:
                continue
                #stop increasing stcolor 2
                #else
        elif new_color[1] >= 255:
                #stop increasing stcolor 1
                continue
        wn.bgcolor(new_color)
        time.sleep(.01)

        for i in range(360):
        if new_color[1] >= 170:
                start_color = (start_color[0], start_color[1] - second_color_step_size, start_color[2])
                new_color = (start_color[0], start_color[1], start_color[2])
                wn.bgcolor(new_color)
                #increase stcolor 1
                #elif check stcolor 2
        elif new_color[2] >= 102:
                start_color = (start_color[0], start_color[1], start_color[2] - third_color_step_size)
                new_color = (start_color[0], start_color[1], start_color[2])
                wn.bgcolor(new_color)
                #increase stcolor 2
                #elif color 2 => 187
        elif new_color[2] < 102:
                continue
                #stop increasing stcolor 2
                #else
        elif new_color[1] < 170:
                #stop increasing stcolor 1
                continue
'''
        
##    for i in range(360):
##        temp_color = new_color
##        new_color = (start_color[0], start_color[1] - second_color_step_size * i, start_color[2] - third_color_step_size * i)
##        if temp_color[1] >= 204:
##            if temp_color[2] >= 153:
##                wn.bgcolor(new_color)
##                time.sleep(.3)
##                print(new_color)
        
        


