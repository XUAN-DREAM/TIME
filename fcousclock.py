import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print("Focus! Time remaining:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Good work.")

# Call the function with the desired number of minutes
focus_timer(25)  # This will run a focus timer for 25 minutes.
