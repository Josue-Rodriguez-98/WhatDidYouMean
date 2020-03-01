#!/usr/bin/python3

# -----------------------------------------------------------
# Proyecto I de Sistemas Inteligentes
# Did you mean...?
# Desarrollado por Josué Rodríguez (11641196)
# Comandos implementados: ls, df, ping
# -----------------------------------------------------------

import subprocess as sp
import re
import os

#Bloque de código que ejecuta el comando
def execute(args):
  try:
    #print("trying...")
    if(args[0] == "ping" and len(args) == 2):
      args = [args[0],"-c","4",args[1]]
    sp.call(args)
  except:
    #print("failing...")
    print(f"Command '{args}' not defined")
#----------------------------------------

#Bloque de código que analiza la entrada erronea
def analyze(args, correct, list):
  #Busca si el comando ya está en lsList
  if(args[0] in list):
    args[0] = correct
    execute(args)
  else:
    #Si no está, le pregunta al usuario wdym y lo guarda (o no)
    answer = input(f"Command {args[0]} not found\nDid you mean '{correct}'[Y/n]: ")
    if(answer):
      answer = answer.lower()
    if(not answer or answer[0] == 'y'):
      print("Ok! I'll remember that!")
      list.append(args[0])
      #for tries in list:
      #  print(tries)
      args[0] = correct
      execute(args)
    elif(answer[0] == 'n'):
      print("Ok then!")
    else:
      print("I'll take that as a NO...")
    return list
#------------------------------------------

def getPath():
  currentPath = os.getcwd()[1:].split("/")
  newPath = []
  retVal = ""
  for path in currentPath:
    #print(path)
    if(path != "home"):
      newPath.append(path)
  for path in newPath:
    if(path == currentPath[1]):
      retVal = path + ":~"
    else:
      retVal += "/" + path
  return retVal
  

def main():
  lsList = []
  dfList = []
  pingList = []
  alive = True
  path = getPath()
  while alive:
    command = input(f"{path}:> ")
    if(re.match(r'^[eE][xX][iI][tT]$',command)):
      print("See you later!")
      alive = False
    elif(command):
      args = command.split()
      if(args[0] == "ls" or args[0] == "df" or args[0] == "ping"):
        execute(args)
      else:
        if(re.match(r'^[jklñ{][asdf]$',args[0])):
          #evaluar ls
          analyze(args,"ls",lsList)
        elif(re.match(r'^[asdfg][sdfgh]$',args[0])):
          #evaluar df
          analyze(args,"df",dfList)
        elif(re.match(r'^[iop][yuiop][vbnm,][dfghj]$', args[0])):
          #evaluar ping
          analyze(args,"ping",pingList)
        else:
          print("We really don't know what you mean... :s")
#-----------------------------------------    
    
if '__main__' == __name__:
  main()