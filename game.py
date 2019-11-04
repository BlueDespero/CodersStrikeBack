import sys
import math
from time import time


class Geometrics():
    
    def collision_pod_pod(self,P1,P2):
        if (self.distance(P1,P2)<=P1.radius*2):
            return 1
        return 0

    def collision_checkpoint_pod(self,P1,C):
        if (self.distance(P1,C)<=C.radius):
            return 1
        return 0

    def distance(self,O1, O2):
        return math.sqrt((O1.x - O2.x)*(O1.x - O2.x) + (O1.y - O2.y)*(O1.y - O2.y))


class Planner():

    def __init__(self):
        self.info = Game_info()

        self.Pod_1 = Pod(0,0)
        self.Pod_2 = Pod(0,0)

        self.Oponent_1 = Pod(0,0)
        self.Oponent_2 = Pod(0,0)

    def simple_approach(self):
        pass

    def turn(self):
        while True:
            if (self.info.time_passed_in_round() > 70):
                print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " 100")
                break
        

class Game_info():
    
    def __init__(self):
        self.list_of_checkpoints = []
        self.round_start_time = 0

    def get_round_start_time(self):
        self.round_start_time = int(round(time()*1000))

    def get_current_time(self):
        return int(round(time()*1000))

    def time_passed_in_round(self):
        return self.get_current_time() - self.round_start_time


class Checkpoint():

    radius = 600
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Pod():

    radius = 400
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0

        self.current_targegt_checkpoint = []
        self.boost_used = 0

    def update_position(self, x, y):
        self.x = x
        self.y = y

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop

Info_storage = Game_info()
Agent = Planner()

while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    Agent.info.get_round_start_time()
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    Agent.Pod_1.update_position(x,y)

    Agent.turn()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
