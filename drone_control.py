import python_ardrone.libardrone as libardrone

def main():
    drone = libardrone.ARDrone()
    drone.takeoff()
    running = True
    while 1: # running:
        try:
            """Set to hover between instructions"""
    	    drone.hover()
            """Set the pitch, roll, and yaw"""
	    ## TODO
    	    pitch = 0
    	    roll = 0
	    yaw = 0
	    """Set quitting signal"""
	    quit = 0


	    """Set the ControlVector"""
	    drone.controlVector = [roll, pitch, 0, yaw]
	    drone.vector_move()

        except KeyboardInterrupt:
            drone.land()
            raise
	## TODO Add condition for quiting
	# if quit:
	#    drone.land()
	#    running = False
