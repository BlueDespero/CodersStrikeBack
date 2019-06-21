import sys
import math

speed = 0
x0 = -1
y0 = -1
last_ch_x=-1
last_ch_y=-1
checkpoint_list = []
list_full = 0
boost = 1
boostable = [0]
where = 0
calculated = 0
distances = []

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in raw_input().split()]
    opponent_x, opponent_y = [int(i) for i in raw_input().split()]

    print_x = next_checkpoint_x
    print_y = next_checkpoint_y

    if (x0>0) and (y0>0):
        speed = math.sqrt(math.pow(x0-x,2)+math.pow(y0-y,2))

    x0=x
    y0=y
    how_many_checkpoints = len(checkpoint_list)

    next_ch=[next_checkpoint_x, next_checkpoint_y]

    if (last_ch_x != next_checkpoint_x) and (list_full == 1):
        where = int((where+1)%how_many_checkpoints)

    if (next_ch in checkpoint_list) and (last_ch_x != next_checkpoint_x and last_ch_y != next_checkpoint_y) and (list_full==0):
        list_full = 1
        boostable = [i for i in range(len(distances)-1) if distances[i]==max(distances)]
        where = int(len(checkpoint_list) - 1)

    if next_ch not in checkpoint_list:
        checkpoint_list.append(next_ch)
        distances.append(next_checkpoint_dist)

    if (last_ch_x != next_checkpoint_x) and (list_full == 1):
        where = int((where+1)%how_many_checkpoints)

    last_ch_x = next_checkpoint_x
    last_ch_y = next_checkpoint_y
    
    if (next_checkpoint_angle > 90) or (next_checkpoint_angle < -90):
        thrust = 0
    else:
        thrust = 100

    thrust = int(thrust)

    if (boost==1 and where == boostable[0] and ((next_checkpoint_angle < 5) and (next_checkpoint_angle>-5)) and list_full == 1):
        thrust = 'BOOST'
        boost = 0

    print (str(print_x) + " " + str(print_y) +" "+ str(thrust))