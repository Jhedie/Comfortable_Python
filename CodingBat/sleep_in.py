#Problem Link:  https://codingbat.com/prob/p173401

def sleep_in(weekday, vacation):
  if not(weekday):
    return True
  elif weekday and vacation:
    return True
  return False


'''
def sleep_in(weekday, vacation):
    if not(weekday)  or vacation:
        return True
    else:
        return False
'''
