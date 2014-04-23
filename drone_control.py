import python_ardrone.libardrone as libardrone
#from kinect_socket import Kinect_sock

def main():
    drone = libardrone.ARDrone()
    drone.takeoff()
    while 1: # running:
        try:
            """Set to hover between instructions"""
            drone.hover()
            """Set the pitch, roll, and yaw"""
            ## TODO
    	    pitch = 0
    	    roll = 0
            yaw = 0
            drone.controlVector = [roll, pitch, 0, yaw]
            drone.vector_move()

        except KeyboardInterrupt:
            drone.land()
            break
	## TODO Add condition for quiting
	# if quit:
	#    drone.land()
	#    running = False
if __name__ == '__main__':
    main()
