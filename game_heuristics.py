import sys
import math
from time import time


Hardcoded_values = {
    'Boost_angle':1,
    'Checkpoint_break_multiplier':2,
    'First_lap_break_multiplier':3,
    'Speed_multiplier': 3,
    'Drift_angle':6,
    'Drift_speed':40,
    'Minimal_drifting_speed':60,
    'Boost_at_start':0
}


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

    def simple_distance(self,O1, O2):
        return math.sqrt((O1[0] - O2[0])*(O1[0] - O2[0]) + (O1[1] - O2[1])*(O1[1] - O2[1]))

    def vector_length(self, vector):
        return math.sqrt((vector[0]*vector[0] + vector[1]*vector[1]))


class Planner():

    def __init__(self):
        self.info = Game_info()
        self.Pod_1 = Pod(0,0)


    def calculate_thrust(self):
        thrust = 100
        if -18 < self.Pod_1.angle < 18:
            if (-Hardcoded_values['Boost_angle'] < self.Pod_1.angle < Hardcoded_values['Boost_angle']
                and ([self.info.next_checkpoint_x, self.info.next_checkpoint_y] == self.info.best_boost_moment or Hardcoded_values['Boost_at_start'])):
                    return "BOOST"
        else:
            thrust*= max(min((1 - abs(self.Pod_1.angle)/90), 1), 0)

        if self.info.all_checkpoints_in_list==1:
            thrust*= max(min((self.info.next_checkpoint_distance/(Checkpoint.radius*Hardcoded_values['Checkpoint_break_multiplier'])), 1), 0)
        else:
            thrust*= max(min((self.info.next_checkpoint_distance/(Checkpoint.radius*Hardcoded_values['First_lap_break_multiplier'])), 1), 0)
        
        return int(thrust)

    def turn(self):
        while True:
            if (self.info.time_passed_in_round() > 70):

                thrust = " "+str(self.calculate_thrust())

                if ((Geometrics.vector_length(self, self.Pod_1.speed)*Hardcoded_values['Speed_multiplier'] > self.info.next_checkpoint_distance 
                    and self.info.all_checkpoints_in_list==1
                    and -Hardcoded_values['Drift_angle'] < self.Pod_1.angle < Hardcoded_values['Drift_angle'])
                    or self.Pod_1.drifting == 1):

                        index = self.info.list_of_checkpoints.index([next_checkpoint_x,next_checkpoint_y])
                        next_x, next_y = self.info.list_of_checkpoints[(index+1)%self.info.amount_of_checkpoints]
                        self.Pod_1.drifting = 1
                        if (Hardcoded_values['Minimal_drifting_speed'] > Geometrics.vector_length(self, self.Pod_1.speed)):
                            self.Pod_1.drifting = 0
                        print(str(next_x) + " " + str(next_y) + " "+str(Hardcoded_values['Drift_speed']))
                else: 
                    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + thrust)
                break
        

class Game_info():
    
    def __init__(self):
        self.list_of_checkpoints = []
        self.round_start_time = 0
        self.all_checkpoints_in_list = 0
        self.amount_of_checkpoints = 0
        self.best_boost_moment = [0,0]
        
        self.next_checkpoint_x = 0
        self.next_checkpoint_y = 0
        self.next_checkpoint_distance = 100

    def get_round_start_time(self):
        self.round_start_time = int(round(time()*1000))

    def get_current_time(self):
        return int(round(time()*1000))

    def time_passed_in_round(self):
        return self.get_current_time() - self.round_start_time

    def update_distance(self,distance):
        self.next_checkpoint_distance = distance

    def update_checkpoints(self, check):

        if (check not in self.list_of_checkpoints 
            and check[0]!= self.next_checkpoint_x 
            and check[1]!=self.next_checkpoint_y):
                self.list_of_checkpoints.append(check)
                self.next_checkpoint_x = check[0]
                self.next_checkpoint_y = check[1]
        elif (check[0] != self.next_checkpoint_x 
            and check[1]!=self.next_checkpoint_y 
            and self.all_checkpoints_in_list == 0):
                self.all_checkpoints_in_list = 1
                self.amount_of_checkpoints = len(self.list_of_checkpoints)
                self.find_best_boost_moment()
        else:
            self.next_checkpoint_x = check[0]
            self.next_checkpoint_y = check[1]

    def find_best_boost_moment(self):
        distances = [[Geometrics.simple_distance(self, self.list_of_checkpoints[x], self.list_of_checkpoints[(x+1)%self.amount_of_checkpoints]),x] for x in range(self.amount_of_checkpoints)]
        distances = sorted(distances, reverse=1)
        self.best_boost_moment = self.list_of_checkpoints[((distances[0][1]+1)%self.amount_of_checkpoints)]


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
        self.drifting = 0
        self.speed = [0,0]

        self.next_checkpoint = [0,0]

        self.boost_used = 0

    def update_pod(self,x,y, angle):
        self.update_angle(angle)
        self.update_speed(x,y)
        self.update_position(x,y)

    def update_angle(self, angle):
        self.angle = angle

    def update_speed(self,x,y):
        self.speed = [x - self.x, y - self.y]

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def update_checkpoints(self, check):
        if self.next_checkpoint!=check:
            self.drifting = 0
            self.next_checkpoint = check

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

    Agent.Pod_1.update_pod(x,y,next_checkpoint_angle)    
    Agent.Pod_1.update_checkpoints([next_checkpoint_x,next_checkpoint_y])

    Agent.info.update_checkpoints([next_checkpoint_x,next_checkpoint_y])
    Agent.info.update_distance(next_checkpoint_dist)

    Agent.turn()


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
