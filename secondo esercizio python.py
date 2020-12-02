Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("questo programma conta quante volte la a è all'interno di una parola ")
domanda = input("\nvuoi cominciare (si\no) ")

if(domanda == "no" or domanda == "No"):
   print ("Ok, grazie del tuo tempo alla prossima ")
   exit
elif(domanda == "si" or domanda == "Si"):
   print("Ok, allora scrivi una parola")
else:
  print("Scusa non ho capito")
  exit
  
a = input()
conta = 0

for x in a:
  if x =="a":

    conta=conta+1
print(conta)