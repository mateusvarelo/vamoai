def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3):
        string = ""
        if ( tempo_chegada3 > tempo_chegada2 > tempo_chegada1):
            string = "1 - "+str(tempo_chegada1)+" minutos\n"+"2 - " +str(tempo_chegada2)+" minutos\n" + "3 - "+str(tempo_chegada3)+" minutos\n"
            return string

        elif ( tempo_chegada2 > tempo_chegada3 > tempo_chegada1 ):   
            string = "\n1 - " + str(tempo_chegada1)+" minutos" + " \n2 - " + str(tempo_chegada3)+" minutos" + "\n3 - " + str(tempo_chegada2)+" minutos"
            return string
        
        elif (tempo_chegada1 < tempo_chegada2 > tempo_chegada3): 
            string = "\n1 - " + str(tempo_chegada3)+" minutos" + " \n2 - " + str(tempo_chegada1)+" minutos" + "\n3 - " + str(tempo_chegada2)+" minutos"
            return string
        
        elif (tempo_chegada3 > tempo_chegada1 > tempo_chegada2):
            string = "\n1 - " + str(tempo_chegada2)+" minutos"+ " \n2 - " + str(tempo_chegada1) +" minutos" + "\n3 - " + str(tempo_chegada3)+" minutos"
            return string
        elif (tempo_chegada1  > tempo_chegada3 > tempo_chegada2):
            string = "\n1 - " + str(tempo_chegada2)+" minutos" + " \n2 - " + str(tempo_chegada3)+" minutos" + "\n3 - " + str(tempo_chegada1) +" minutos"
            return string 
        
        elif (tempo_chegada1 < tempo_chegada2 > tempo_chegada3):
            string = "\n1 - " + str(tempo_chegada3)+" minutos" + " \n2 - " + str(tempo_chegada1)+" minutos" + "\n3 - " + str(tempo_chegada2)+" minutos"
            return string    
        elif (tempo_chegada1 > tempo_chegada2 > tempo_chegada3):
            string = "\n1 - " + str(tempo_chegada3)+" minutos" + " \n2 - " + str(tempo_chegada2)+" minutos" + "\n3 - " + str(tempo_chegada1) +" minutos"
            return string
        string = "\n1 - " + str(tempo_chegada1)+" minutos" + " \n2 - " + str(tempo_chegada2)+" minutos" + "\n3 - " + str(tempo_chegada3) +" minutos" 
        return  string 

tempo_chegada1 = 1
tempo_chegada2 = 2
tempo_chegada3 = 3
print (podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3))