from djitellopy import tello
from time import sleep

beef = tello.Tello()
beef.connect()
print(beef.get_battery())

beef.takeoff()

# Starting point
beef.move_up(80)
beef.move_forward(500)
sleep(.5)

# Turning into "Must fly zone"
beef.rotate_counter_clockwise(90)
beef.move_forward(300)
sleep(.5)

# Going back to start
beef.rotate_counter_clockwise(90)
beef.move_forward(500)
sleep(.5)

# on spot
beef.rotate_counter_clockwise(90)
beef.move_forward(300)
beef.rotate_counter_clockwise(90)

# stop flying
sleep(.5)

beef.land()

