# -*- coding: iso-8859-1 -*-
#Methoden importieren
import Methods27
#Definition von noetigen Variablen

#Lebenspunkte
hp_top = 20
hp = 20

#Skills
magie = 1
fokus = 1
staerke = 10
verteidigung = 0

#Element-skills
feuer = 0
wasser = 0
erde = 0
luft = 0
gravitation = 0
elektro = 0

#Type
atk = False
tnk = False
hlr = False

#Sostiges

#Das Spiel fängt an!
Methods27.Start()

#Die erste Entscheidung
print ('\n \n Der Reiter kommt wieder zu sich. Er fragt sich, wo er ist, wer er ist, und vor allem: Ist er ein Mann (m) oder eine Frau (f)?')
z = raw_input()
person = Methods27.Person(z)
print ('Er überzeugt sich durch einen Griff in die Hose. '+person.personalpronom2+
       ' ist '+person.personalpronom1+' ' +person.geschlecht)

	
	
	
