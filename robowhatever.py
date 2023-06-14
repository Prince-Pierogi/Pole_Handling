import sys
import time
import math

sys.path.append('unitree_legged_sdk/lib/python/arm64')
import robot_interface as sdk

## comm.h

HIGHLEVEL = 0xee

rate = 500 # 500hz
dt = 1.0 / rate # time between commands

def temp_code_hole(cmd, udp):
    for i in range(int(1/dt)):
        cmd.euler = [0.3, -0.3, 0.0] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(1/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [-0.3, -0.3, 0.0] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    cmd.bodyHeight = -0.1

    for i in range(int(0.3/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, 0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.3/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, -0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.3/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, 0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.3/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, -0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.3/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, 0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.3/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, -0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.3/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, 0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.3/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, -0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.2, 0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, -0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.2, 0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, -0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.2, 0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.3, -0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, -0.2, -0.3] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, 0.0, 0.0] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)


    for i in range(int(1/dt)):
        cmd.mode = 2 # Active stand
        cmd.velocity = [0.0, 5.0] #down
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

def main():
    udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.123.220", 8082)

    cmd = sdk.HighCmd()
    state = sdk.HighState()
    udp.InitCmdData(cmd)

    cmd.mode = 0
    cmd.gaitType = 0
    cmd.speedLevel = 0
    cmd.footRaiseHeight = 0
    cmd.bodyHeight = 0
    cmd.euler = [0, 0, 0]
    cmd.velocity = [0, 0]
    cmd.yawSpeed = 0.0
    cmd.reserve = 0


    for i in range (int(3.5/dt)):
        cmd.mode = 6 # stand
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(1/dt)):
        cmd.mode = 1
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(2/dt)):
        cmd.mode = 2  # Walking left
        cmd.velocity = [0.0, 0.6] #left
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(2/dt)):
        cmd.mode = 2  # Walking right
        cmd.velocity = [0.0, -0.6] #left
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(0.5/dt)):
        cmd.mode = 2  # Walking in place
        cmd.velocity = [0.0, 0.0] #left
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(2.3/dt)):
        cmd.mode = 2 #turning left 90-deg
        cmd.yawSpeed = 0.75
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(0.5/dt)):
        cmd.mode = 2 #pausing
        cmd.yawSpeed = 0.0
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(6/dt)):
        tz = math.sin(i/75)* -0.15 - 0.05
        ry = math.cos(i/75)* 0.3
        cmd.mode = 1 # Worm
        cmd.euler = [0.0, ry, 0.0] # Down
        cmd.bodyHeight = tz
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    cmd.euler = [0.0, 0.0, 0.0] # Down
    cmd.bodyHeight = 0.0

    for i in range (int(0.5/dt)):
        cmd.mode = 2 #paused
        cmd.yawSpeed = 0.0
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(2.3/dt)):
        cmd.mode = 2 #turning left 90-deg
        cmd.yawSpeed = 0.75
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(0.5/dt)):
        cmd.mode = 2 #pausing
        cmd.yawSpeed = 0.0
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(5/dt)):
        tz = math.sin(i/75)* -0.15 - 0.05
        ry = math.cos(i/75)* 0.3
        cmd.mode = 1 #
        cmd.euler = [0.0, 0.0, ry] # shake dog tails
        cmd.bodyHeight = tz
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    cmd.euler = [0.0, 0.0, 0.0] # Down
    cmd.bodyHeight = 0.0

    for i in range (int(4.4/dt)):
        cmd.mode = 2 #turning left 1800-deg
        cmd.yawSpeed = 0.75
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(1/dt)):
        cmd.mode = 2 #pausing
        cmd.yawSpeed = 0.0
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(2/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, 0.3, 0.2] #down
        cmd.bodyHeight = -0.1
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range(int(1/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, 0.1, 0.0] #down
        cmd.bodyHeight = 0.0
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)


    for i in range(int(1/dt)):
        cmd.mode = 1 # Active stand
        cmd.euler = [0.0, 0.3, -0.2] #down
        cmd.bodyHeight = -0.1
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    cmd.euler = [0.0, 0.0, 0.0] # Down
    cmd.bodyHeight = 0.0


###################################x





    for i in range (int(0.1/dt)):
        cmd.mode = 2 #turning around
        cmd.yawSpeed = 0.0
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(0.5/dt)):
        cmd.mode = 1 # stand
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)




    for i in range (int(2/dt)):
        cmd.mode = 6 # stand
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

    for i in range (int(2/dt)):
        cmd.mode = 5 # lay
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

main()

