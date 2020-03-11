#/usr/bin/python3

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
def analyze(args, correct, rcvdList):
  #Busca si el comando ya está en list
  if(args[0] in rcvdList):
    args[0] = correct
    execute(args)
  else:
    #Si no está, le pregunta al usuario wdym y lo guarda (o no)
    answer = input(f"Did you mean '{correct}'? [Y/n]: ")
    if(answer):
      answer = answer.lower()
    if(not answer or answer[0] == 'y'):
      print("Ok! I'll remember that!")
      rcvdList.append(args[0])
      args[0] = correct
      execute(args)
    elif(answer[0] == 'n'):
      print("Ok then!")
    else:
      print("I'll take that as a NO...")
    return rcvdList
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
#-------------------------------------------

def writeFile(lsList, dfList, pingList):
  content = ""
  i = 0
  for i in range(len(lsList)):
    #print(f" lsList in {i} is {lsList[i]}")
    if(lsList[i] != ""):
      content += lsList[i]
      if(i + 1 < len(lsList)):
        content += "|"
  content += "#"
  i = 0
  for i in range(len(dfList)):
    #print(f" dfList in {i} is {dfList[i]}")
    if(dfList[i] != ""):
      content += dfList[i]
      if(i + 1 < len(dfList)):
        content += "|"
  content += "#"
  i = 0
  for i in range(len(pingList)):
    #print(f" pingList in {i} is {pingList[i]}")
    if(pingList[i] != ""):
      content += pingList[i]
      if(i + 1 < len(pingList)):
        content += "|"
  #print(content)
  file = open("filiberto.txt","w+")
  file.write(content)
  file.close()
#-------------------------------------------

def main():
  lsList = []
  dfList = []
  pingList = []
  alive = True
  content = ""
  try:
    #Si el archivo existe, lo lee
    file = open("filiberto.txt","r")
    content = file.readline()
    file.close()
    #print(content)
    arrayContent = content.split("#")
    lsList = arrayContent[0].split("|")
    dfList = arrayContent[1].split("|")
    pingList = arrayContent[2].split("|")
  except IOError:
    #Si el archivo no existe, lo crea
    file = open("filiberto.txt","w+")
    file.close()
  path = getPath()
  while alive:
    command = input(f"{path}:> ")
    if(re.match(r'^[eE][xX][iI][tT]$',command)):
      print("See you later!")
      #Escribir las sugerencias guardadas en un archivo txt
      writeFile(lsList, dfList, pingList)
      alive = False
    elif(command):
      args = command.split()
      if(len(args) > 0):
        if(args[0] == "ls" or args[0] == "df" or args[0] == "ping"):
          execute(args)
        else:
          if(re.match(r'^[jklñ{][asdf]$',args[0])):
            #evaluar ls
            print(lsList)
            analyze(args,"ls",lsList)
            print(lsList)
          elif(re.match(r'^[asdfg][sdfgh]$',args[0])):
            #evaluar df
            analyze(args,"df",dfList)
          elif(re.match(r'^[iop][yuiop][vbnm,][dfghj]$', args[0])):
            #evaluar ping
            analyze(args,"ping",pingList)
          else:
            print("We really don't know what you mean... :s")
      else:
        print("We really don't know what you mean... :s")        
#-----------------------------------------    
    
if '__main__' == __name__:
  main()