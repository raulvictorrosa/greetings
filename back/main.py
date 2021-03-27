import hug
from hug_middleware_cors import CORSMiddleware
from datetime import datetime, time

def is_time_between(begin_time, end_time, check_time = None):
  # If check time is not given, default to current UTC time
  check_time = check_time or datetime.now().time()
  if begin_time < end_time:
    return check_time >= begin_time and check_time <= end_time
  else: # crosses midnight
    return check_time >= begin_time or check_time <= end_time

api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api, max_age=10))

@hug.get('/')
def home():
  return "Welcome"

@hug.get('/saudacao')
def greeting():
  """Verify what is the current time and return a message to every part of the day."""
  message = ""
  phaseDay = ""
  color = ""
  if is_time_between(time(00, 00), time(5, 59)):
    message = "Boa Madrugada"
    phaseDay = "dawn"
    color = "#616161"

  if is_time_between(time(6, 00), time(11, 59)):
    message = "Bom Dia"
    phaseDay = "day"
    color = "#ffca28"

  if is_time_between(time(12, 00), time(17, 59)):
    message = "Boa Tarde"
    phaseDay = "afternoon"
    color = "#f57c00"

  if is_time_between(time(18, 00), time(23, 59)):
    message = "Boa noite"
    phaseDay = "night"
    color = "#616161"

  return {"message": message, "phaseDay": phaseDay, "color": color}
