from interbotix_xs_modules.arm import InterbotixManipulatorXS
import math

bot = InterbotixManipulatorXS("vx300s", "arm", "gripper")
xo =0
yo=0
try:
    while True:
        x= input("Enter X coordinate")
        y = input("Enter Y coordinate")
        yin = math.atan(y/x)+0.025
        xin = math.sqrt((x**2)+ (y**2))-0.05
        yin = yin - yo
        xin = xin - xo
        bot.arm.set_ee_pose_components(x=xin, z =0.2)
        bot.arm.set_single_joint_position("waist", yin)
        yo= yin
        xo = xin
except KeyboardInterrupt:
    print("Stopping")
finally:
        bot.gripper.close
        bot.arm.go_to_home_pose()
        bot.arm.go_to_sleep_pose()