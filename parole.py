
stringa = input("Scrivi una parola --> ")
lista_lettere = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
stringa = list(stringa.upper())
for lettera in lista_lettere:
    if stringa.count(lettera) > 0:
        print(lettera, " : " ,stringa.count(lettera))


alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("scrivi ora una parola che vuoi sapere il numer di lettere complessivo.")
stringa = input()
conta = 0

for lettera in alfabeto:
     for x in stringa:
          if lettera ==x:
             conta=conta+1
print(conta)

 