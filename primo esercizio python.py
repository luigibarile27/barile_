Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nome = input("Come ti chiami?  ")
print("Ciao " + nome)

risposta_scelta = input("\nVuoi affittare un motorino? (Si/No) ")




if(risposta_scelta == "no" or risposta_scelta == "No"):
   print ("Ok, grazie del tuo tempo alla prossima ")
   exit
elif(risposta_scelta == "si" or risposta_scelta == "Si"):
   print("Ok, allora incominciamo subito")
else:
  print("Scusa non ho capito")
  exit
risposta_scelta2 = input("per quanti giorni??    (1,2,3,4) ")
if(risposta_scelta2 == "1"):
  print("per un giorno sono 45€")
if(risposta_scelta2 == "2"):
  print("per due giorni sono 80€")
if(risposta_scelta2 == "3"):
  print("per tre giorni sono 120")
if(risposta_scelta2 == "4"):
  print("per quattro giorni sono 160€")
if(risposta_scelta2 == "5"):
  print("non ho capito")
else:
  print("ogni giorno extra 40€")
  
input()
print("grazie e arrivederci")