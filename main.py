# import the necessary packages
from __future__ import print_function
from view.login import LoginGUI
from view.employee import EmployeeGUI
from imutils.video import VideoStream
import argparse
import time
from tkinter import *

root = Tk()
login = LoginGUI(root)
root.mainloop()
