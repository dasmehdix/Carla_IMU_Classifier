# Carla_IMU_Classifier
IMU (Inertial Measurement Unit) sensor data reciever &amp; classifier for CARLA SIMULATOR. In both script, ```Town03``` map chosen. Random spawn at start disabled. You can enable with uncomment this line:

```#spawn_point = random.choice(spawn_points) if spawn_points else carla.Transform()```

## BE CAREFUL
You have to build Carla simulator before use this repo. 

After build, you just have to copy the scripts inside ```{PATH}\CARLA\PythonAPI\examples``` folder.

Also, do not forget to execute carla server where ```{PATH}\CARLA\CARLAUE4.exe``` with ```-carla-server``` argument.

## ```data_reciever.py```
 You can collect IMU (or other sensors depends on your configuration) sensor data via this script. A new argument "name" created, which is the name of driver.

You can use like that:

```python data_reciever.py --filter name --name John29```

The script will save a file named ```"out_John29.csv"``` which includes 6-axis IMU data with a label column fulled with ```John29```

INSTANCE OUT:
class | accelX | accelY | accelZ | gyroX | gyroY | gyroZ
-- | -- | -- | -- | -- | -- | --
John29 | -0.329013 | 1.111466 | 9.943973 | 0.064446 | -0.0759 | -0.095295
John29 | -0.329013 | 1.111466 | 9.943973 | 0.064446 | -0.0759 | -0.095295

An example csv file uploaded here ==> ```examples/out_mehdi.csv```

## ```classifier.py```
You can load & make prediction with trained neural network (tensorflow, ```.h5``` format). The input size of my neural network is (1,20,6)=(Batch, timesteps, features) in my implementation. So, in the line 1074th

```data = np.array(data).reshape(1,20,6)```

I reshaped data into designed neural network's input size. You can change this line for your configuration.

## Requirements
- Python (3.6-3.7)
- tensorflow
- pandas 
- pygame
- carla
- numpy
