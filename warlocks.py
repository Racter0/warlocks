class Warlock:
    #Hit points
    HP=15
    #simple mind control
    isMaladroit=False
    isAmnesiac=False
    isParalyzed=False
    isAfraid=False

    def parseGestures(self,gestures): #maybe only parse opponent gestures in one fn
        LH=[a for (a,b) in gestures]
        RH=[b for (a,b) in gestures]
        
        #simple mind control
        if LH[-3:]==['F','F','F'] or RH[-3:]=['F','F','F']:
            self.isParalyzed=True
            
        if LH[-3:]==['D','S','F'] or RH[-3:]=['D','S','F']:
            self.isMaladroit=True

        if LH[-3:]==['S','W','D'] or RH[-3:]=['S','W','D']:
            self.isAfraid=True

        if LH[-3:]==['D','P','P'] or RH[-3:]=['D','P','P']:
            self.isAfraid=True



p1=Warlock()

#first pass: read in array of gestures, print out HP and status
#gestures=list of tuples (RH, LH)
gestures=[('F','W'), ('F','W'), ('F', 'P')]

p1.parseGestures(gestures)

print p1.isParalyzed

