
highest_cals = list((0, 0, 0))
current_cals = 0

with open('Day_1_Input.txt') as file:
    for line in file:
        if len(line.strip()) == 0:
            if(current_cals > highest_cals[0]):
                highest_cals.insert(0, current_cals)
                del highest_cals[-1]
                #break
            elif(current_cals > highest_cals[1]):
                highest_cals.insert(1, current_cals)
                del highest_cals[-1]
                #break
            elif(current_cals > highest_cals[2]):
                highest_cals.insert(2, current_cals)
                del highest_cals[-1]
                #break
            current_cals = 0
        else:
            current_cals = current_cals + int(line)

print(highest_cals)
total_cals = highest_cals[0] + highest_cals[1] + highest_cals[2]
print(total_cals)