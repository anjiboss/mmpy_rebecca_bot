# import the time module
import time
from datetime import timedelta
  
def get_sec(prompt: str, command):
  time = prompt.split(command + " ")
  if len(time) < 1:
    return False
  time = time[1]
  time = time.split("h")
  min = 0
  hour = 0
  if len(time) > 1 :
    hour = time[0]
  time = time[0].split("m")
  if len(time) > 1 :
    min = time[0]
  min = int(min)
  hour = int(hour)
  time_in_sec = timedelta(hours=hour, minutes=min)
  return time_in_sec.seconds

