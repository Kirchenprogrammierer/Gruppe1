:# Initialisieren
import random
Guthaben = 10
Zwischenstand = []

#Funktionen
def Zahlen_festlegen():
	a = random.randint(0,10)
	b = random.randint(0,10)
	c = random.randint(0,10)
	d = random.randint(0,10)
	richtige_Zahlen = [a,b,c,d]

def Weiter_oder_nicht():
	antwort = int(input("Möchten sie Lotto spielen? 1=Ja 0=Nein"))

def Raten(Zahl):
	gerateneZahl = int(input("Bitte raten sie die  Zahl Nummer ",Zahl," zwischen 0 und 10!")
                           
def Einsatz():
	einsatz = int(input("Sie haben noch ",Guthaben," Euro zur Verfügung. Wie viel wollen sie setzen?"))
	Guthaben = Guthaben-einsatz	

	
def Richtig(Zahl):
	print("Die Zahl Nummer ",Zahl," haben sie richtig geraten!")
	
def Richtig_oder_nicht(Zahl):
	zahl = int(Zahl)
	Raten(Zahl)
	if zahl == 1:
		if gerateneZahl == a:
			Richtig(1)
			weiter = True
		elif a < 0 or a > 10:
			print ("Diese Zahl steht nicht zur Verfügung. Bitte wählen sie eine Zahl zwischen 0 und 10!")
		else:
			print("Tut uns leid sie haben ihren kompletten Einsatz verloren.")
			weiter = False
	elif zahl == 2:
		if gerateneZahl == b:
			Richtig(1)
			weiter = True
		elif b < 0 or b > 10:
			print ("Diese Zahl steht nicht zur Verfügung. Bitte wählen sie eine Zahl zwischen 0 und 10!")
		else:
			print("Tut uns leid sie haben leider nicht den Jackpot gewonnen. Trotzdem haben sie",einsatz*1.125,"Euro gewonnen! Herzlichen Glückwunsch!")
			Guthaben = Guthaben+einsatz*1.125
			weiter = False
	elif zahl == 3:
		if gerateneZahl == c:
			Richtig(1)
			weiter = True
		elif c < 0 or c > 10:
			print ("Diese Zahl steht nicht zur Verfügung. Bitte wählen sie eine Zahl zwischen 0 und 10!")
		else:
			print("Tut uns leid sie haben leider nicht den Jackpot gewonnen. Trotzdem haben sie",Einsatz*1.25,"Euro gewonnen! Herzlichen Glückwunsch!")
			Guthaben = Guthaben+einsatz*1.25
			weiter = False
	elif zahl == 4:
		if gerateneZahl == d:
			Richtig(1)
			print("Jackpot!!! Sie haben",einsatz*2,"Euro gewonnen!!!")
			Guthaben = Guthaben+einsatz*2
			weiter = True
		elif d < 0 or d > 10:
			print ("Diese Zahl steht nicht zur Verfügung. Bitte wählen sie eine Zahl zwischen 0 und 10!")
		else:
			print("Tut uns leid sie haben leider nicht den Jackpot gewonnen. Trotzdem haben sie",einsatz*1.5,"Euro gewonnen! Herzlichen Glückwunsch!")
			Guthaben = Guthaben+einsatz*1.5
			weiter = False
# Hauptcode
Weiter_oder_nicht()

while antwort == 1:
        Einsatz()
	Zahlen_festlegen()
	Richtig_oder_nicht(1)
	if weiter = True:
		Richtig_oder_nicht(2)
	if weiter = True:
		Richtig_oder_nicht(3)
	if weiter = True:
		Richtig_oder_nicht(4)
	Zwischenstand.append(Guthaben)
	Hoechststand = max(Zwischenstand)
	if Guthaben == 0:
		print("Sie haben kein Guthaben mehr zur Verfügung. Ihr Höchststand war: ",Hoechststand," Euro. Versuchen sie es später nochmal.")
		antwort = 0
	else:
		print("Ihr Guthaben beträgt: ",Guthaben," Euro.")
		Weiter_oder_nicht()

if Guthaben !=0:
	print ("Sie haben das Spiel mit ",Guthaben," Euro beendet. Ihr Hoechststand war ",Hoechststand," Euro. Bis zum nächsten Mal")
