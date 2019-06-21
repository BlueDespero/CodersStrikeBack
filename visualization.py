from tkinter import *
from PIL import Image, ImageDraw, ImageTk
from pods import Pod
import random
import math
from custom import tools

class Window(Frame):

    def __init__(self):
        super().__init__()
        self.pod_list = []
        self.checkpoints = []
        self.done = 0
        self.initialize_checkpoints()
        self.initialize_pods()
        self.init_window()

    def distance(self,a,b):
        a_x, a_y = a
        b_x, b_y = b
        dist = math.sqrt((a_x-b_x)*(a_x-b_x) + (a_y-b_y)*(a_y-b_y))
        return dist

    def draw_board(self):

        canvas = Image.new('RGBA',(tools["board_size_x"], tools["board_size_y"]))
        drawing = ImageDraw.Draw(canvas,'RGBA')

        for e in range(len(self.checkpoints)):
            x,y = self.checkpoints[e]

            if e == 1:
                drawing.ellipse(((x-tools["checkpoint_radius"], y-tools["checkpoint_radius"]), (x+tools["checkpoint_radius"],y+tools["checkpoint_radius"])), fill=(0,255,0))
            else:
                drawing.ellipse(((x-tools["checkpoint_radius"], y-tools["checkpoint_radius"]), (x+tools["checkpoint_radius"],y+tools["checkpoint_radius"])), fill=(0,0,255))

            #drawing.ellipse(((x-tools["checkpoint_radius"], y-tools["checkpoint_radius"]), (x+tools["checkpoint_radius"],y+tools["checkpoint_radius"])), fill=(0,0,255))

        for e in self.pod_list:
            x = e.x
            y = e.y
            drawing.ellipse(((x-tools["pod_radius"], y-tools["pod_radius"]), (x+tools["pod_radius"],y+tools["pod_radius"])), fill=(255,0,0))

        return canvas

    def initialize_checkpoints(self):
        checkpoint_list = []
        while len(checkpoint_list) < tools["hm_checkpoints"]:
            x = random.randint(100, tools["board_size_x"]-100)
            y = random.randint(100, tools["board_size_y"]-100)
            coords = [x,y]
            correct = 1

            for c in checkpoint_list:
                if self.distance(coords,c) < 100:
                    correct = 0
                    break
            if correct == 1:
                checkpoint_list.append(coords)

        self.checkpoints = checkpoint_list

    def initialize_pods(self):
        chp_x, chp_y = self.checkpoints[0]
        st_points_list = [[chp_x-tools["pod_radius"],chp_y+tools["pod_radius"]],
        [chp_x+tools["pod_radius"],chp_y-tools["pod_radius"]], 
        [chp_x+tools["pod_radius"],chp_y+tools["pod_radius"]], 
        [chp_x-tools["pod_radius"],chp_y-tools["pod_radius"]]]

        for p in range(tools["hm_pods"]):
            self.pod_list.append(Pod(st_points_list[p], self.checkpoints))

    def update_image(self, board):
        new_board = self.draw_board()
        new_board = ImageTk.PhotoImage(new_board)
        board.configure(image = new_board)
        board.image = new_board
        self.update()
        self.update_idletasks()

    def play(self, b_board):
        for pod in self.pod_list:
            pod.move()
        self.update_image(b_board)

    def init_window(self):
        self.master.title('CodersSB')
        self.pack(fill = BOTH, expand = 1)
        self.columnconfigure(0, weight = 6)
        self.rowconfigure(0,weight = 1)

        main_f = Frame(self, bg = "GREY")
        main_f.grid(column = 0, row = 0, sticky = (N,S,E,W))
        self.update()

        board_img = self.draw_board()
        board_handle = ImageTk.PhotoImage(board_img)
        b_board = Label(main_f, image = board_handle)
        b_board.image = board_handle
        b_board.place(x=0,y=0)

        while not self.done:
            self.play(b_board)

if __name__ == '__main__':
    root = Tk()
    root.geometry("2400x1600")
    app = Window()
    root.mainloop()