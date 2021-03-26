import hug
from datetime import datetime, time

def is_time_between(begin_time, end_time, check_time=None):
  # If check time is not given, default to current UTC time
  check_time = check_time or datetime.now().time()
  if begin_time < end_time:
      return check_time >= begin_time and check_time <= end_time
  else: # crosses midnight
      return check_time >= begin_time or check_time <= end_time

@hug.get('/')
def home():
  return "Welcome"

@hug.get('/gretting')
def gretting():
  """Verify what is the current time and return a message to every part of the day."""
  message = ""
  if is_time_between(time(00,00), time(5,59)):
    message = "Boa Madrugada"

  if is_time_between(time(6,00), time(11,59)):
    message = "Bom Dia"

  if is_time_between(time(12,00), time(17,59)):
    message = "Boa Tarde"

  if is_time_between(time(18,00), time(23,59)):
    message = "Boa noite"

  return {"message": message}
