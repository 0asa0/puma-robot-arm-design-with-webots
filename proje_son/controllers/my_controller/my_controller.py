from controller import Robot
import math
import random

robot = Robot()
timestep = 64

waist = robot.getDevice("motor")
shoulder = robot.getDevice("motor1")
elbow = robot.getDevice("motor2")
wrist1 = robot.getDevice("motor3")
wrist2 = robot.getDevice("motor4")

waist_sensor = waist.getPositionSensor()
waist_sensor.enable(timestep)
shoulder_sensor = shoulder.getPositionSensor()
shoulder_sensor.enable(timestep)
elbow_sensor = elbow.getPositionSensor()
elbow_sensor.enable(timestep)
wrist1_sensor = wrist1.getPositionSensor()
wrist1_sensor.enable(timestep)
wrist2_sensor = wrist2.getPositionSensor()
wrist2_sensor.enable(timestep)


# Obtain and enable the GPS sensor
gps_sensor = robot.getDevice("gps")
gps_sensor.enable(timestep)

waist.setPosition(float('inf'))
shoulder.setPosition(float('inf'))
elbow.setPosition(float('inf'))
wrist1.setPosition(float('inf'))
wrist2.setPosition(float('inf'))

waist.setVelocity(0.0)
shoulder.setVelocity(0.0)
elbow.setVelocity(0.0)
wrist1.setVelocity(0.0)
wrist2.setVelocity(0.0)

def move(joint, target_angle, velocity=2.0, tolerance=0.01):
    target_angle = math.radians(target_angle)
    joint.setPosition(target_angle)
    joint.setVelocity(velocity)
    while robot.step(timestep) != -1:
        current_angle = joint.getPositionSensor().getValue()
        error = target_angle - current_angle

        gps_position = gps_sensor.getValues()
        print(f"GPS position: x={gps_position[0]}, y={gps_position[1]}, z={gps_position[2]}")
        save_gps_data(gps_position)
        
        if abs(error) <= tolerance:
            joint.setVelocity(0.0)
            break
            
def save_gps_data(gps_data):
    with open("gps_data.txt", 'a') as file:
        file.write(",".join(map(str, gps_data)) + "\n")

def rotate_waist():
    move(waist, 360, 3)
    move(waist, 0, 3)

k = 0
elbow_angle = 0
waist_angle = 0
shoulder_down_angle = math.radians(95)
shoulder_up_angle = math.radians(43)
initial_shoulder_angle = 0

waist_step = math.radians(12)
shoulder_step = 0.1
k = 1
####################################################
while robot.step(timestep) != -1 and k < 31:
    waist_angle += waist_step
    waist.setPosition(waist_angle)
    gps_position = gps_sensor.getValues()
    print(f"GPS position: x={gps_position[0]}, y={gps_position[1]}, z={gps_position[2]}")
    save_gps_data(gps_position)
   
    k = k+1
    
    while abs(shoulder_sensor.getValue() - shoulder_down_angle) > 0.01:
        shoulder.setVelocity(2.0)
        shoulder.setPosition(shoulder_down_angle)
        robot.step(timestep)
        gps_position = gps_sensor.getValues()
        print(f"GPS position: x={gps_position[0]}, y={gps_position[1]}, z={gps_position[2]}")
        save_gps_data(gps_position)
    while abs(shoulder_sensor.getValue() - initial_shoulder_angle) > 0.01:
        shoulder.setVelocity(2.0)
        shoulder.setPosition(initial_shoulder_angle)
        robot.step(timestep)
        gps_position = gps_sensor.getValues()
        print(f"GPS position: x={gps_position[0]}, y={gps_position[1]}, z={gps_position[2]}")
        save_gps_data(gps_position)

    while abs(shoulder_sensor.getValue() - (-shoulder_up_angle)) > 0.01:
        shoulder.setVelocity(2.0)
        shoulder.setPosition(-shoulder_up_angle)
        robot.step(timestep)
        gps_position = gps_sensor.getValues()
        print(f"GPS position: x={gps_position[0]}, y={gps_position[1]}, z={gps_position[2]}")
        save_gps_data(gps_position)
    while abs(shoulder_sensor.getValue() - initial_shoulder_angle) > 0.01:
        shoulder.setVelocity(2.0)
        shoulder.setPosition(initial_shoulder_angle)
        robot.step(timestep)
        gps_position = gps_sensor.getValues()
        print(f"GPS position: x={gps_position[0]}, y={gps_position[1]}, z={gps_position[2]}")
        save_gps_data(gps_position)

    for _ in range(int(500 / timestep)):  
        if robot.step(timestep) == -1:
            break

    waist.setVelocity(0.0)
    shoulder.setVelocity(0.0)
    
    for _ in range(int(500 / timestep)):  
        if robot.step(timestep) == -1:
            break

    waist.setVelocity(2.0)
    shoulder.setVelocity(1.0)

while robot.step(timestep) != -1:
    random_elbow_angle = random.uniform(-180, 180)
    random_shoulder_angle = random.uniform(-43, 223)
    random_wrist2_angle = random.uniform(-100, 100)
    random_wrist1_angle = random.uniform(0, 360)
    
    #move(wrist2,random_wrist2_angle,5)
    #move(wrist1,random_wrist1_angle,7)
    move(elbow, random_elbow_angle)
    move(shoulder, random_shoulder_angle)
    
    rotate_waist()

    
        





    
    
    
    
    
    
