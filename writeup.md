## Project: Estimation
### Saminda Abeyruwan

### Specification

* Provide a Writeup / README that includes all the rubric points and how you addressed each one.

__Completed__.

* Determine the standard deviation of the measurement noise of both GPS X data and Accelerometer X data.

__Completed__. _estimation.py_ contains code that estimate the standard deviation. MeasuredStdDev_GPSPosXY = 0.71647547, and
MeasuredStdDev_AccelXY = 0.50877271

* Implement a better rate gyro attitude integration scheme in the _UpdateFromIMU()_ function.

__Completed__.

* Implement all of the elements of the prediction step for the estimator.

__Completed__.

* Implement the magnetometer update.

__Completed__.

* Implement the GPS update.

__Completed__.

* Meet the performance criteria of each step.

__Completed__.

* De-tune your controller to successfully fly the final desired box trajectory with your estimator and realistic sensors.

__Completed__. I have  replaced the controller, _QuadController.cpp_, and the parameters, _QuadControlParams.txt_, developed in [project 3](https://github.com/samindaa/FCND-Controls-CPP)
in the current code base. It turns out to be that the parameters work out of the box. 

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/tO5c7eisGFk/0.jpg)](https://www.youtube.com/watch?v=tO5c7eisGFk)