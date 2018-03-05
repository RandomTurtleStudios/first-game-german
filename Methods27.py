# -*- coding: iso-8859-1 -*-

#import Spiel_1_27

def Start():
    print ('RandomTurtleStudios präsentieren: \n \n')
    print ('Platzhalter!!!! \n \n')
    #Jetzt geht's los
    print ('Kapitel 1: Der Spiegel \n')
    print('Boden; 1365. Ein junger Reisender, reist durch das Land. \
Auf dem Weg nach Garn, der Hauptstadt von Boden. \
Er ist gerade durch das Bergdorf Fettfleck geritten. \
Er sieht die Weinberge, den Fluss, das entfernte Dorf. \
Plötzlich, ein Rumpeln, ein Krachen. \
Schwere Steinbrocken fallen von den umliegenden Bergen auf den Reiter hinab. \
Das Pferd bäumt sich auf, wirft den Reiter ab. \
Er fällt hinab, rollt über den Berg auf den Fluss zu. \
Plötzlich ein Schlag. \
Ein Stück Treibholz hat ihm gegen den Kopf geschlagen. \
Er wird ohnmächtig.')
    return('Funktion erfolgreich')

class Person:
    
    def __init__(self, geschlecht):
        kopf = 'nichts'
        if geschlecht == 'm':
            self.geschlecht = 'Mann'
            self.personalpronom1 = 'ein'
            self.personalpronom2 = 'Er'
            self.kopf = kopf
        elif geschlecht == 'f':
            self.geschlecht = 'Frau'
            self.personalpronom1 = 'eine'
            self.personalpronom2 = 'Sie'
            self.kopf = kopf

    def change_kb(self,new):
        self.kopf = new
        return()
        

    
def Entscheidung_2():
    print Spiel_1_27.person.personalpronom2 + 'schwimmt langsam ans Ufer.'
