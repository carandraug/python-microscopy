#import all the stuff to make this work
from PYME.Acquire.protocol import *

#define a list of tasks, where T(when, what, *args) creates a new task
#when is the frame number, what is a function to be called, and *args are any
#additional arguments
taskList = [
T(20, Ex, 'scope.cam.compT.laserPowers[0] = 1'),
T(201, MainFrame.pan_spool.OnBAnalyse, None)
]

#must be defined for protocol to be discovered
PROTOCOL = TaskListProtocol(taskList)