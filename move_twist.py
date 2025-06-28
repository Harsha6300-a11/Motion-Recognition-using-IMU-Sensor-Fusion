import os          #OS is needed for creating a directory in python and saving that file in local PC and in this file all the data will be recorded
import time        #time is needed for recording values and saving data file with recorded time becuase it will have unique time in files
import numpy as np #the data that recorded will be converted into numpy array and saved into file
from sensehat import Sensehat #in this API the accelerromter and gyrometer works


sense = Sensehat()

Label= "move_twist" #This recording will be stored on this file
save_dir="D/intelliget robotics/First sem/Embedded Systems/record_motion/"{Label}
os.mkdir(save_dir,exist_ok=True) #This will create file in that path

#Time_delay
Samples = 20
Freq = 50
Delay=1.0/Freq

#Logic

try:
    while(1):
        print("press enter to record data for {Label}",format(Label))
        data=[]#storirng the data in this list
        for _ in range(Samples):
            acc=sense.get_acceleraometer_raw()
            gyro=sense.get_gyrometer_raw()
            sample=[acc['x'],acc['y'],acc['z'],gyro['x'],gyro['y'],gyro['z']]
            data.append(sample)
            time.delay(Delay)
            timestamp=int(time.time())
            np.save("{save_dir}/{Label}_{timestamp}.npy",np.array(data))
            print("saved {Label}_{timestamp}.npy")


except Keyboard Interrupt:
    print("Recording stopped")
