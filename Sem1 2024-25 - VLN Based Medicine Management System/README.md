This folder contains all the code related to the pipeline of the medicine management system.
To run the pipeline, simply go to the terminal first launch the arm using the command "roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=vx300s" 
then make sure your present working directory is this directory and run this command "sh recorder_script.sh". the pipeline will then wait for you to press the microphone so that the pipeline can begin.

Sample command you can give "Identify the unkown bottle, weigh it and place it on the Monday slot."

List of files:
- ans.py : The final code that is executed on the arm. This script is automatically re-written for every new voice command
- arm_motion.py : This is a reset for the arm, incase it gets stuck in any position, running this script will return it to its sleep pose.
- check_shelf.py : This contains a function check_shelf() which checks the shelf and returns whichever shelf slots are empty
- digits_func.py: This contains a function digit_read() which reads the digits of the 7 segment display weight scale.
- identify_unkown.py: This contains a function identify_new() which can pick up a bottle, put it on the rotating platform, generate a panorama of the label of the bottle and using the VLN find out the name of the medicine.
- name_meds(): Uses the VLN to read text from an input image
- origin_finder(): This contains a function find_aruco_center() which finds teh aruco marker of the weight scale to crop the number on the scale as needed
- origin_realsense(): This contains a function find_origin() which can calculate the origin in pixels from the overhead frame
- prompt.txt: The prompt for chatgpt to generate the code
- realsense_yolo_func.py: This takes the arm to a base pose from which YOLO will be used to detect and find the positions of different bottles on the table
- recorder.py: This script waits for the mic to be active, records audio and saves it.
- robot_func2: This contains the functions pick up() and get_position() which can be used by chatgpt to pick up the bottles
- shelf_aruco.py: This contains a function find_aruco_shelf(image) which takes an input image, finds all the aruco markers in the image.
- shelve_meds.py: This contains a function shelve_meds(day) which puts a bottle on the aruco marker corresponding to the specific day
- Speech_pipe.py : This contains two functions, one to transcribe audio to text, and one to send the text to chatgpt for gpt to write code based on it.
- tts2.py : This contains the function tts which converts any text to speech using the google speech to text module
- weight_check_function.py: This contains the function check_weight() which checks the weight of any bottle.

Attatched is an image of the project system setup
![IMG_20241108_144252 (1)](https://github.com/user-attachments/assets/6474c8b5-2241-4e78-a005-1a258ea65fb4)
