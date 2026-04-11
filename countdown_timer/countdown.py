import time
def countdown(minutes=0):
    """
    parameter: Minute
    printed: overwritten the previous timer with end="\r"
    convert the minutes into seconds
    and print 
    decrease the time by -1 after the program sleep for 1 second
    """
    total_time = minutes * 60
    while total_time > 0:
        m = total_time // 60
        s = total_time % 60
        print(f"{m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        total_time -= 1
if __name__ == "__countdown__":
    countdown()