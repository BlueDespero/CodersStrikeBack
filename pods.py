import numpy as np

class Pod():

    def __init__(self, coords, checkpoints):
        self.x, self.y = coords
        self.pod_size = 20
        self.speed = 6
        self.direction = [1,0]
        self.checkpoints = checkpoints
        self.current_checkpoint = 1

    def possition_change(self):
        self.x, self.y = (self.direction[0]*self.speed + self.x), (self.direction[1]*self.speed + self.y)

    def get_xy_chp(self):
        return self.checkpoints[self.current_checkpoint]

    def vec_length(self, vector):
        return np.sqrt((vector[0]*vector[0])+(vector[1]*vector[1]))

    def vector_between_pod_chp(self):
        return [self.checkpoints[self.current_checkpoint][0] - self.x, self.checkpoints[self.current_checkpoint][1] - self.y]

    def new_way(self):
        pod_checkpoint_vector = self.vector_between_pod_chp()
        dot_product = np.dot(self.direction, pod_checkpoint_vector)
        cosine = dot_product/(self.vec_length(self.direction)*self.vec_length(pod_checkpoint_vector))
        angle = np.rad2deg(np.arccos(cosine))*np.sign(dot_product)

        print(angle)


    def change_direction(self, angle = 0):
        pass

    def move(self):
        self.change_direction(self.new_way())
        self.possition_change()