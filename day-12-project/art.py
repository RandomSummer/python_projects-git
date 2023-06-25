import pyfiglet as pf

def ascii_art():
  result = pf.figlet_format("Guess the number", font="alphabet")
  return result

finale = ascii_art()