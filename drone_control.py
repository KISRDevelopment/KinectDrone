import python_ardrone.libardrone as libardrone

#drone = libardrone.ARDrone()

def main():
#    drone = libardrone.ARDrone()
#    drone.takeoff()
    running = True
    while running:
	"""Set to hover between instructions"""
#	drone.hover()

	#****************************
	# TESTING INPUT
	#****************************
	RAW = [float(x) for x in raw_input("<roll pitch throttle yaw quit>: ").split(" ")]
	
	
        """Set the pitch, roll, and yaw"""
	## TODO this is the point where the kinect and the drone meet
	pitch = 0
	roll = 0
	yaw = 0
	throttle = 0
	"""Set quitting signal"""
	quit = 0

	
	"""Set the ControlVector"""
	print(RAW)#

#	drone.controlVector = RAW[:-1]#[roll, pitch, throttle, yaw]
#	drone.vector_move()

	## TODO Add condition for quiting
	if RAW[-1]: #quit:
	   # drone.land()
	    running = False

if __name__ == '__main__':
	main()
