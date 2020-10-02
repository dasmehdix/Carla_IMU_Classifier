import setup_path 
import airsim
import pandas as pd
import cv2 #conda install opencv
import time
import argparse
argparser = argparse.ArgumentParser(
    description='Airsim')
argparser.add_argument(
    '--name',
    default="mehdi",
    type=str,
    help='Name Of Player')
args = argparser.parse_args()
# connect to the AirSim simulator 
client = airsim.CarClient()
client.confirmConnection()
car_controls = airsim.CarControls()

start = time.time()
print("Time,Speed,Gear,PX,PY,PZ,OW,OX,OY,OZ")
data = pd.DataFrame()
# monitor car state while you drive it manually.
try:
    while (1):
        # get state of the car
        car_state = client.getCarState()
        pos = car_state.kinematics_estimated.position
        orientation = car_state.kinematics_estimated.orientation
        milliseconds = (time.time() - start) * 1000
        """print("%s,%d,%d,%f,%f,%f,%f,%f,%f,%f" % \
        (milliseconds, car_state.speed, car_state.gear, pos.x_val, pos.y_val, pos.z_val, 
            orientation.w_val, orientation.x_val, orientation.y_val, orientation.z_val))"""
        imu_data = client.getImuData(imu_name = "", vehicle_name="")
        #print(type(imu_data))
        low_data = {"accelX":imu_data.angular_velocity.x_val,
                    "accelY":imu_data.angular_velocity.y_val,
                    "accelZ":imu_data.angular_velocity.z_val,
                    "linearAcX":imu_data.linear_acceleration.x_val, 
                    "linearAcY":imu_data.linear_acceleration.y_val, 
                    "linearAcZ":imu_data.linear_acceleration.z_val,
                    "orientX":imu_data.orientation.x_val, 
                    "orientY":imu_data.orientation.y_val, 
                    "orientZ":imu_data.orientation.z_val,
                    "class":str(args.name)}
        print(low_data)
        data = data.append(low_data, ignore_index=True)
except KeyboardInterrupt:
    data.to_csv('output_{}.csv'.format(str(args.name)))
    print('CSV saved for {}'.format(str(args.name)))
    pass