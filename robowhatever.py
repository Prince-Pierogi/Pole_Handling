import sys
import time

sys.path.append('unitree_legged_sdk/lib/python/arm64')
import robot_interface as sdk

## comm.h

HIGHLEVEL = 0xee

rate = 500 # 500hz
dt = 1.0 / rate # time between commands

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

    for i in range(2000):
        udp.Recv()
        udp.GetRecv()
        print(state.motorState[0].temperature)
        udp.SetSend(cmd)
        udp.Send()
        time.sleep(dt)

   main()

