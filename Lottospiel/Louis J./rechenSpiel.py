import random
i=0
a=random.randint(1,20)
b=random.randint(1,20)
c=a*b
print("Wollen sie eine Aufgabe? 1=Ja 0=Nein")
eingabe=input()
antwort=int(eingabe)
if antwort==1:
        print('Die Aufgabe lautet:',a,'*',b,'. Bitte geben sie die Loesung ein! Sie haben 10 Versuche.')
p=0
while antwort==1:
        eingabe=input()
        x=int(eingabe)
        i=i+1
        if x==c:
                p=p+1
                print("Super! ",c," ist die richtige Antwort! Sie haben ",i," Versuche gebraucht. Sie haben schon", p ,"Punkte. Wollen sie eine neue Aufgabe? 1=Ja 0=Nein")
                i=0
                eingabe=input()
                antwort=int(eingabe)
                if antwort==1:
                        a=random.randint(1,20)
                        b=random.randint(1,20)
                        c=a*b
                        print('Die Aufgabe lautet:',a,'*',b,'. Bitte geben sie die Loesung ein! Sie haben 10 Versuche.')
                else:
                        print("Herzlichen Glückwunsch sie haben", p ,"Punkte erreicht!")
        elif x>c:
                print("Schade! ",x," ist zu gross. Versuchs nochmal!")
        else:
                print("Schade! ",x," ist zu klein. Versuchs nochmal!")
        if i==10:
                print("Schade! Sie haben zu viele Versuche gebraucht. Die Loesung ist ",c,". Sie haben", p ,"Punkte erreicht. Wollen sie nochmal spielen? 1=Ja 0=Nein")
                p=0
                i=0
                eingabe=input()
                antwort=int(eingabe)
                if antwort==1:
                        a=random.randint(1,20)
                        b=random.randint(1,20)
                        c=a*b
                        print('Die Aufgabe lautet:',a,'*',b,'. Bitte geben sie die Loesung ein! Sie haben 10 Versuche.')
                
