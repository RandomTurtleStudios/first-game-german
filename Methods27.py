# -*- coding: iso-8859-1 -*-

#import Spiel_1_27

def Start():
    print ('RandomTurtleStudios pr�sentieren: \n \n')
    print ('Platzhalter!!!! \n \n')
    #Jetzt geht's los
    print ('Kapitel 1: Der Spiegel \n')
    print('Boden; 1365. Ein junger Reisender, reist durch das Land. \
Auf dem Weg nach Garn, der Hauptstadt von Boden. \
Er ist gerade durch das Bergdorf Fettfleck geritten. \
Er sieht die Weinberge, den Fluss, das entfernte Dorf. \
Pl�tzlich, ein Rumpeln, ein Krachen. \
Schwere Steinbrocken fallen von den umliegenden Bergen auf den Reiter hinab. \
Das Pferd b�umt sich auf, wirft den Reiter ab. \
Er f�llt hinab, rollt �ber den Berg auf den Fluss zu. \
Pl�tzlich ein Schlag. \
Ein St�ck Treibholz hat ihm gegen den Kopf geschlagen. \
Er wird ohnm�chtig.')
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
    print '{}'
