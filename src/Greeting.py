import datetime
import getpass

def dayportion(datetime) :
  hour = datetime.hour
  if hour < 12 :
    return "Good morning"
  elif hour >= 12 and hour < 16 :
    return "Good afternoon"
  else:
    return "Good evening"

def greeting() :
  welcome = dayportion(datetime.datetime.now())
  user = getpass.getuser().title()
  print(f"{welcome} {user}.")
  print()