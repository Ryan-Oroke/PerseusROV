import readchar
from adafruit_servokit import ServoKit

ENABLED = False;

ud_servo = 3;
ud_throttle_step = 1;
ud_throttle = 0;
ud_throttle_max = 170;
ud_throttle_min = 0;

lm_servo = 1;
rm_servo = 2;
fb_throttle_step = 3;
fb_throttle = 0;
turn_throttle = 0;
turn_throttle_abs_max = 120;
turn_throttle_step = 3;
fb_throttle_min = 0;
fb_throttle_max = 150;
lm_throttle_max = 170;
lm_throttle_min = 0;
rm_throttle_max = 170;
tm_throttle_min = 0;

kit = ServoKit(channels=16)

while(1):
	# Read Keys ------------------------------------------------

	key = readchar.readkey();

	# Non-Kinetic Control Keys ----------------------------------

	if(key == "e"):
		# Enable Key
		print("Enabled");
		ENABLED = True

	elif(key == "d"):
		#Disable Key
		print("Disabled");
		kit.servo[ud_servo].angle = 0;
		kit.servo[lm_servo].angle = 0;
		kit.servo[rm_servo].angle = 0;
		ENABLED = False

	elif(key == "q" or key == "c" or key == "x" or key == "z"):
		print("Execution Terminated by '"+key+"'");
		kit.servo[ud_servo].angle = 0;
		kit.servo[rm_servo].angle = 0;
		kit.servo[lm_servo].angle = 0;
		exit()

	# Motor Control Keys -----------------------------------------

	if(ENABLED):
		# Check the terminal for a key press
		#key = readchar.readkey();
		#print(key);

		# Determine what to do based on the key input

		# Numbered Keys
		if(key == "1" or key == "9"):
			# Dive Key
			print("Sinking:", ud_throttle);
			if( ud_throttle < ud_throttle_max ):
				ud_throttle += ud_throttle_step

		elif(key == "2"):
			# Down Key
			print("Slower Forward:", fb_throttle);
			if(fb_throttle > fb_throttle_min):
				fb_throttle -= fb_throttle_step

		elif(key == "3"):
			# Toggle Light
			print("Toggled Light: OFF");

		elif(key == "4"):
			# Left Key
			print("Turning More Left:", turn_throttle)
			if(turn_throttle > -1*turn_throttle_abs_max):
				turn_throttle -= turn_throttle_step;

		elif(key == "5"):
			# Stop Turning
			print("Stop Turning & Advancing");
			fb_throttle = 0;
			turn_throttle = 0;
			lm_throttle = 0;
			rm_throttle = 0;

		elif(key == "6"):
			# Right Key
			print("Turning More Right:", turn_throttle);
			if(turn_throttle < turn_throttle_abs_max):
				turn_throttle += turn_throttle_step;

		elif(key == "7"):
			# Rising Key
			print("Rising:", ud_throttle);
			if(ud_throttle > ud_throttle_min):
				ud_throttle -= ud_throttle_step

		elif(key == "8"):
			# Faster Key
			print("Forward Faster:", fb_throttle);
			if(fb_throttle < fb_throttle_max):
				fb_throttle += fb_throttle_step

		# Set the motor speeds
		
		lm_throttle = fb_throttle + turn_throttle
		rm_throttle = fb_throttle - turn_throttle
		if(ud_throttle >= 0):
			kit.servo[ud_servo].angle = ud_throttle
		if(lm_throttle >= 0):
			kit.servo[lm_servo].angle = lm_throttle 
		if(rm_throttle >= 0):
			kit.servo[rm_servo].angle = rm_throttle


	
