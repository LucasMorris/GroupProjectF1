import turtle

from model import Car
from view import TrackView

# mainScreen = Tkinter.Tk()
# track = Track.Track()
# track.insertCar(Car.Car())
import tkinter as tk


class Simulator(tk.Frame):
    canvas = None
    master = None
    trackView = None

    def __init__(self, master=None):
        super().__init__(master)
        tk.Frame.__init__(self, master)
        self.master = master

        canvas = tk.Canvas(master=None, width=950, height=800)
        canvas.pack()

        self.buildTrack(canvas)

        self.trackView.insertCar(Car.Car())

        self.trackView.insertCar()


    def buildTrack(self, canvas):
        self.trackView = TrackView.TrackView(canvas)

