import threading

from view import TrackView

import tkinter as tk


class Simulator(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.frame = tk.Frame.__init__(self, master)
        self.master = master
        self.trackView = None

        canvas = tk.Canvas(master=None, width=950, height=800)

        canvas.grid(row=1, column=0, columnspan=5, rowspan=5, padx=5, pady=5)

        quitButton = tk.Button(master,
                               text="Quit",
                               fg="red",
                               command=master.destroy)

        quitButton.grid(row=0, column=0)

        startStopButton = tk.Button(master,
                                    text="Start",
                                    fg="red",
                                    command=self.startStopSim)

        startStopButton.grid(row=0, column=1)

        self.buildTrack(canvas)

        self.trackView.insertCar()

        soft = tk.Button(master,
                         text="S",
                         fg="black",
                         bg="red",
                         command=lambda: self.trackView.updateCarSpeed(9))

        soft.grid(row=6, column=2, padx=5, pady=5)

        medium = tk.Button(master,
                           text="M",
                           fg="black",
                           bg="yellow",
                           command=lambda: self.trackView.updateCarSpeed(2.5))

        medium.grid(row=6, column=3, padx=5, pady=5)

        hard = tk.Button(master,
                         text="H",
                         fg="black",
                         bg="white",
                         command=lambda: self.trackView.updateCarSpeed(1))

        hard.grid(row=6, column=4, padx=5, pady=5)


    def buildTrack(self, canvas):
        self.trackView = TrackView.TrackView(canvas)

    def startStopSim(self):
        if not self.trackView.isCarOnTrack:
            self.trackView.isCarOnTrack = True
            self.trackView.driveCar()
