import python_ardrone.libardrone as libardrone

drone = libardrone.ARDrone()

def main():
    drone = libardrone.ARDrone()
    drone.takeoff()
    running = True
    while running:
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

	## TODO Add condition for quiting
	# if quit:
	#    drone.land()
	#    running = False
