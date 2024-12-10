print(len(pts))
    if len(pts) >= 2:  
        i = len(pts)-2
        if pts[i] == center:
            bot.gripper.open()
            bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.16)
            bot.gripper.close()
            bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
            bot.arm.go_to_home_pose()
            bot.arm.go_to_sleep_pose()
            break
    
        else:
            center_prev = pts[i]
            x_p = center_prev[0]
            y_p = center_prev[1]
            x_pcm =(547-x_p)*(0.6/319)-0.075
            y_pcm = (y_p-136)*(0.6/319)+0.05 
            x_pcm = x_pcm - xcm
            y_pcm = y_pcm - ycm
            ang = math.atan(y_pcm/x_pcm)
            bot.arm.set_ee_cartesian_trajectory(x=x_pcm)
            bot.arm.set_single_joint_position("waist",ang ) 
    else:
         yin = math.atan(ycm/xcm)+0.05
         xin = math.sqrt((xcm**2)+ (ycm**2)) - 0.12
         print(yin)
         bot.arm.set_ee_pose_components(x=xin, z =0.2)
         bot.arm.set_single_joint_position("waist", yin)