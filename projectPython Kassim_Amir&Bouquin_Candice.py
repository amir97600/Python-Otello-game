########################################## Librairies #####################################################
from tabulate import tabulate
import time

########################################## Fonctions #####################################################

#Voici la matrice que nous associerons au plateau pour associer les coordonnées et y faire les calculs
def InitialisationPlateau ():
    plateau=[]
    for l in range (8):
        ligne=[]
        for c in range(8):
            ligne.append(0)   
        plateau.append(ligne)
#On place les pions de départ, par convention nous avons choisi la valeur 2 pour un pion rouge et 1 pour un pion vert, la valeur 0 représentant une case vide
    plateau[3][3]=2 
    plateau[3][4]=1
    plateau[4][4]=2
    plateau[4][3]=1
    return plateau

   



#Fonction qui associe la matrice avec son affichage
def Affichage (matrice) :    
    list=[]
    matrix=[]
    #On parcourt ici chaque élément de notre matrice et on regarde quelle valeur est assignée pour chaque élément, par convention 0:case vide, 1:case verte et 2:caserouge
    for ligne in range(8):
        for c in range(8):
            #En fonction de la valeur on ajoute l'affichage de l'élément sur le plateau dans une liste
            if matrice[ligne][c]==1:
                list.append("V")
                continue
            if matrice[ligne][c]==2:
                list.append("R")
                continue
            else:
                list.append("")
        #Lorsque l'on a 8 valeur dans la liste  ajoute ensuite cette liste dans une autre matrice pour l'affichage du plateau, cela représente notre ligne de 8 colonne et on réinitialise la liste (ainsi on ne récupère que des lignes et non la matrice entière dans notre liste)        
        matrix.append(list)
        list=[]
        header=["A","B","C","D","E","F","G","H"]
        index=[1,2,3,4,5,6,7,8]
    print(tabulate(matrix,headers=header,showindex=index,tablefmt="fancy_grid"))



#début de cacul pour les verts
def calculV(matrice,ligne,colonne):
    changeEtat = 0

    #scan en horizontal
    flagligne = True
    li = dicotraduction[ligne]
    i = dicotraduction[colonne]
    while flagligne == True:
        nbV=0
        nbR=0
        nbZ=0
        for i in range (i,8):
                element = matrice[dicotraduction[ligne]][i]
                if element == 0 and nbV == 1 :
                    nbZ+=1
                if element == 2 and nbV == 1 :
                    elementdébut=i-1
                if element == 1:
                    nbV+=1
                    if nbV == 2 and nbR>=1 and nbZ == 0  :
                        for tl in range (elementdébut,i+1):
                            matrice[dicotraduction[ligne]][tl] = 1
                        print("Bien joue !")
                        changeEtat+=1    
                        break
                if element == 1 and nbV == 1 and nbR == 0  :
                    flagligne=False
                if element == 2 and nbV == 1:
                    nbR+=1
                    continue
                if nbV < 2:
                    flagligne=False


    flagligneG = True
    i = dicotraduction[colonne]
    nbV=0
    nbR=0
    nbZ=0
    while flagligneG == True:
        for i in range(i,-1,-1):
                element = matrice[dicotraduction[ligne]][i]
                if element == 0 and nbV == 1 :
                    nbZ+=1
                if element == 2 and nbV == 1 :
                    elementdébut=i+1
                if element == 1:
                    nbV+=1
                    if nbV == 2 and nbR>=1 and nbZ == 0  :
                        for tl in range (elementdébut,i,-1):
                            matrice[dicotraduction[ligne]][tl] = 1
                        print("Bien joue !")
                        changeEtat+=1    
                        break
                if element == 1 and nbV == 1 and nbR == 0  :
                    flagligneG=False
                if element == 2 and nbV == 1:
                    nbR+=1
                    continue
                if nbV < 2:
                    flagligneG=False
        
    #scan en vertical
    flagCB = True
    nbV2b=0
    nbR2b=0
    nbZ2b=0
    i= dicotraduction[ligne]
    while flagCB == True:
        for i in range (i,8):
            elementC = matrice[i][dicotraduction[colonne]]
            if elementC == 0 and nbV2b == 1 :
                nbZ2b+=1
            if elementC == 2 and nbV2b == 1 :
                elementCdébut=i-1
            if elementC == 1:
                nbV2b+=1
                if nbV2b == 2 and nbR2b>=1 and nbZ2b == 0 :
                    for t in range (elementCdébut,i+1):
                        matrice[t][dicotraduction[colonne]] = 1
                    print("Bien joue !")
                    changeEtat+=1    
                    break
            if elementC == 1 and nbV2b == 1 and nbR2b == 0  :
                flagCB=False
            if elementC == 2 and nbV2b == 1 :
                nbR2b+=1
                continue
            elif elementC == 1 :
                continue
            if nbV2b < 2:
                flagCB=False

    flagCH = True
    nbV2h=0
    nbR2h=0
    nbZ2h=0
    i= dicotraduction[ligne]
    while flagCH == True:
        for i in range (i,-1,-1):
            elementC = matrice[i][dicotraduction[colonne]]
            if elementC == 0 and nbV2h ==1 :
                nbZ2h+=1
            if elementC == 2 and nbV2h == 1 :
                elementCdébut=i+1
            if elementC == 1:
                nbV2h+=1
                if nbV2h == 2 and nbR2h>=1 and nbZ2h == 0 :
                    for t in range (elementCdébut,i,-1):
                        matrice[t][dicotraduction[colonne]] = 1
                    print("Bien joue !")
                    changeEtat+=1 
                    break
            if elementC == 1 and nbV2h == 1 and nbR2h == 0  :
                flagCH=False
            if elementC == 2 and nbV2h ==1 :
                nbR2h+=1
                continue
            if nbV2h < 2:
                flagCH=False

    #scan en diagonale en haut à droite
    flagD_HD = True
    col = dicotraduction[colonne]
    li = dicotraduction[ligne]
        
    while flagD_HD == True :
        nbVD_HD=0
        nbRD_HD=0
        nbZD_HD=0
        listElement=[]
        while 0<=li<=7 and 0<=col<=7 :
            elementD_HD = matrice [li] [col]
            if elementD_HD == 0 and nbVD_HD ==1 :
                nbZD_HD+=1
            if elementD_HD == 2 and nbVD_HD == 1 :
                listElement.append([li,col])
            if elementD_HD == 0:
                li = li-1
                col = col+1
            if elementD_HD == 1:
                nbVD_HD+=1
                li = li-1
                col = col+1
                if nbVD_HD == 2 and nbRD_HD>=1 and nbZD_HD == 0 :
                    flagD_HD=True
                    for l,c in listElement:
                        matrice[l][c] = 1
                    print("Bien joue !")
                    changeEtat+=1    
                    break
            if elementD_HD == 1 and nbVD_HD == 1 and nbRD_HD == 0  :
                flagD_HD=False
            if elementD_HD == 2 and nbVD_HD ==1 :
                nbRD_HD+=1
                li = li-1
                col = col+1
                
            elif elementD_HD == 2 :
                li = li-1
                col = col+1
                
            if nbVD_HD < 2:
                flagD_HD=False
            

     #scan en diagonale en bas à droite
        flagD_BD = True
        col = dicotraduction[colonne]
        li = dicotraduction[ligne]
    
    while flagD_BD == True :
        nbVD_BD=0
        nbRD_BD=0
        nbZD_BD=0
        listElement=[]
        while 0<=li<=7 and 0<=col<=7 :
            elementD_BD = matrice [li] [col]
            if elementD_BD == 0 and nbVD_BD ==1 :
                nbZD_BD+=1
            if elementD_BD == 2 and nbVD_BD == 1 :
                listElement.append([li,col])
            if elementD_BD == 0:
                li = li+1
                col = col+1
            if elementD_BD == 1:
                nbVD_BD+=1
                li = li+1
                col = col+1
                if nbVD_BD == 2 and nbRD_BD>=1 and nbZD_BD == 0 :
                    flagD_BD=True
                    for l,c in listElement:
                        matrice[l][c] = 1
                    print("Bien joue !")
                    changeEtat+=1    
                    break
            if elementD_BD == 1 and nbVD_BD == 1 and nbRD_BD == 0  :
                flagD_BD=False
            if elementD_BD == 2 and nbVD_BD ==1 :
                nbRD_BD+=1
                li = li+1
                col = col+1
                continue
            elif elementD_BD == 2 :
                li = li+1
                col = col+1
                continue
            if nbVD_BD < 2:
                flagD_BD=False
           




    #scan en diagonale en haut à gauche
        flagD_HG = True
        col = dicotraduction[colonne]
        li = dicotraduction[ligne]
    
    while flagD_HG == True :
        nbVD_HG=0
        nbRD_HG=0
        nbZD_HG=0
        listElement=[]
        while 0<=li<=7 and 0<=col<=7 :
            elementD_HG = matrice [li] [col]
            if elementD_HG == 0 and nbVD_HG ==1 :
                nbZD_HG+=1
            if elementD_HG == 2 and nbVD_HG == 1 :
                listElement.append([li,col])
            if elementD_HG == 0:
                li = li-1
                col = col-1
            if elementD_HG == 1:
                nbVD_HG+=1
                li = li-1
                col = col-1
                if nbVD_HG == 2 and nbRD_HG>=1 and nbZD_HG == 0 :
                    flagD_HG=True
                    for l,c in listElement:
                        matrice[l][c] = 1
                    print("Bien joue !")
                    changeEtat+=1    
                    break
            if elementD_HG == 1 and nbVD_HG == 1 and nbRD_HG == 0  :
                flagD_HG=False
            if elementD_HG == 2 and nbVD_HG ==1 :
                nbRD_HG+=1
                li = li-1
                col = col-1
                continue
            elif elementD_HG == 2 :
                li = li-1
                col = col-1
                continue
            if nbVD_HG < 2:
                flagD_HG=False
           

    #scan en diagonale en bas à gauche
        flagD_BG = True
        col = dicotraduction[colonne]
        li = dicotraduction[ligne]
    
    while flagD_BG == True :
        nbVD_BG=0
        nbRD_BG=0
        nbZD_BG=0
        listElement=[]
        while 0<=li<=7 and 0<=col<=7 :
            elementD_BG = matrice [li] [col]
            if elementD_BG == 0 and nbVD_BG ==1 :
                nbZD_BG+=1
            if elementD_BG == 2 and nbVD_BG == 1 :
                listElement.append([li,col])
            if elementD_BG == 0:
                li = li+1
                col = col-1
            if elementD_BG == 1:
                nbVD_BG+=1
                li = li+1
                col = col-1
                if nbVD_BG == 2 and nbRD_BG>=1 and nbZD_BG == 0 :
                    flagD_BG=True
                    for l,c in listElement:
                        matrice[l][c] = 1
                    print("Bien joue !")
                    changeEtat+=1    
                    break
            if elementD_BG == 1 and nbVD_BG == 1 and nbRD_BG == 0  :
                flagD_BG=False
            if elementD_BG == 2 and nbVD_BG ==1 :
                nbRD_BG+=1
                li = li+1
                col = col-1
                continue
            elif elementD_BG == 2 :
                li = li+1
                col = col-1
                continue
            if nbVD_BG < 2:
                flagD_BG=False

    return changeEtat,matrice
    







#début de cacul pour les rouges
def calculR(matrice,ligne,colonne):
    changeEtat = 0

    #scan en horizontal
    flagligne = True
    while flagligne == True:
        nbRd=0
        nbVd=0
        nbZd=0
        i = dicotraduction [colonne]
        for i in range (i,8):
                element = matrice[dicotraduction[ligne]][i]
                if element == 0 and nbRd ==1 :
                    nbZd+=1
                if element == 1 and nbRd == 1 :
                    elementdébut=i-1
                if element == 2:
                    nbRd+=1
                    if nbRd == 2 and nbVd>=1 and nbZd == 0:
                        # flagligne=True
                        for tl in range (elementdébut,i+1):
                            matrice[dicotraduction[ligne]][tl] = 2
                        print("Bien joue !")
                        changeEtat+=1    
                        break
                if element == 1 and nbVd == 1 and nbRd == 0  :
                    flagligne=False
                if element == 1 and nbRd == 1:
                    nbVd+=1
                    continue
                if nbRd < 2:
                    flagligne=False

    flagligneG = True
    nbRG=0
    nbVG=0
    nbZG=0
    i = dicotraduction[colonne]
    while flagligneG == True:
        for i in range (i,-1,-1):
                element = matrice[dicotraduction[ligne]][i]
                if element == 0 and nbRG ==1 :
                    nbZG+=1
                if element == 1 and nbRG == 1 :
                    elementdébut=i+1
                if element == 2:
                    nbRG+=1
                    if nbRG == 2 and nbVG>=1 and nbZG == 0:
                        # flagligneG=True
                        for tl in range (elementdébut,i,-1):
                            matrice[dicotraduction[ligne]][tl] = 2
                        print("Bien joue !")
                        changeEtat+=1    
                        break
                if element == 1 and nbVG == 1 and nbRG == 0  :
                    flagligneG=False
                if element == 1 and nbRG == 1:
                    nbVG+=1
                    continue
                if nbRG < 2:
                    flagligneG=False


     #scan en vertical
    flagCH = True
    while flagCH == True:
        nbR2=0
        nbV2=0
        nbZ2=0
        i= dicotraduction[ligne]
        for i in range (i,8):
            elementC = matrice[i][dicotraduction[colonne]]
            if elementC == 0 and nbR2 == 1 :
                nbZ2+=1
            if elementC == 1 and nbR2 == 1 :
                elementCdébut=i-1
            if elementC == 2:
                nbR2+=1
                if nbR2 >= 2 and nbV2>=1 and nbZ2 == 0 :
                    for t in range (elementCdébut,i+1):
                        matrice[t][dicotraduction[colonne]] = 2
                    print("Bien joue !")
                    changeEtat+=1    
                    break
            if elementC == 1 and nbV2 == 1 and nbR2 == 0  :
                flagCH=False
            if elementC == 1 and nbR2 ==1 :
                nbV2+=1
                continue
            if nbR2 < 2:
                flagCH=False

    flagCB = True
    nbR2b=0
    nbV2b=0
    nbZ2b=0
    i= dicotraduction[ligne]
    while flagCB == True:
        for i in range (i,-1,-1):
            elementC = matrice[i][dicotraduction[colonne]]
            if elementC == 0 and nbR2b ==1 :
                nbZ2b+=1
            if elementC == 1 and nbR2b == 1 :
                elementCdébut=i+1
            if elementC == 2:
                nbR2b+=1
                if nbR2b == 2 and nbV2b>=1 and nbZ2b == 0 :
                    for t in range (elementCdébut,i,-1):
                        matrice[t][dicotraduction[colonne]] = 2
                    print("Bien joue !")
                    changeEtat+=1    
                    break
            if elementC == 1 and nbV2b == 1 and nbR2b == 0  :
                flagCB=False
            if elementC == 1 and nbR2b ==1 :
                nbV2b+=1
                continue
            if nbR2b < 2:
                flagCB=False

    #scan en diagonale en haut à droite
    flagD_HD = True
    col = dicotraduction[colonne]
    li = dicotraduction[ligne]
    
    while flagD_HD == True :
        nbRD_HD=0
        nbVD_HD=0
        nbZD_HD=0
        listElement=[]
        while 0<=li<=7 and 0<=col<=7 :
            elementD_HD = matrice [li] [col]
            if elementD_HD == 0 and nbRD_HD ==1 :
                nbZD_HD+=1
            if elementD_HD == 1 and nbRD_HD == 1 :
                listElement.append([li,col])
            if elementD_HD == 0:
                li = li-1
                col = col+1
            if elementD_HD == 2:
                nbRD_HD+=1
                if nbRD_HD == 2 and nbVD_HD>=1 and nbZD_HD == 0 :
                    flagD_HD=True
                    for l,c in listElement:
                        matrice[l][c] = 2
                    print("Bien joue !")
                    changeEtat+=1    
                    break
                li = li-1
                col = col+1
            if elementD_HD == 2 and nbRD_HD == 1 and nbVD_HD == 0  :
                flagD_HD=False
            if elementD_HD == 1 and nbRD_HD ==1 :
                nbVD_HD+=1
                li = li-1
                col = col+1
                continue
            elif elementD_HD == 1 :
                li = li-1
                col = col+1
                continue
            if nbRD_HD < 2:
                flagD_HD=False
            
    


     #scan en diagonale en bas à droite
    flagD_BD = True
    col = dicotraduction[colonne]
    li = dicotraduction[ligne]
    
    while flagD_BD == True :
        nbRD_BD=0
        nbVD_BD=0
        nbZD_BD=0
        listElement=[]
        while 0<=li<=7 and 0<=col<=7 :
            elementD_BD = matrice [li] [col]
            if elementD_BD == 0 and nbRD_BD >=1 :
                nbZD_BD+=1
            if elementD_BD == 1 and nbRD_BD == 1 :
                listElement.append([li,col])
            if elementD_BD == 0:
                li = li+1
                col = col+1
            if elementD_BD == 2:
                nbRD_BD+=1
                if nbRD_BD == 2 and nbVD_BD>=1 and nbZD_BD == 0:
                    flagD_BD=True
                    for l,c in listElement:
                        matrice[l][c] = 2
                    print("Bien joue !")
                    changeEtat+=1    
                    break
                li = li+1
                col = col+1
            if elementD_BD == 1 and nbRD_BD ==1 :
                nbVD_BD+=1
                li = li+1
                col = col+1
            elif elementD_BD == 1 :
                li = li+1
                col = col+1
                continue
            if nbRD_BD < 2:
                flagD_BD=False
            
            



    #scan en diagonale en haut à gauche
    flagD_HG = True
    col = dicotraduction[colonne]
    li = dicotraduction[ligne]
    
    while flagD_HG == True :
        nbRD_HG=0
        nbVD_HG=0
        nbZD_HG=0
        listElement=[]
        while 0<=li<=7 and 0<=col<=7 :
            elementD_HG = matrice [li] [col]
            if elementD_HG == 0 and nbRD_HG ==1 :
                nbZD_HG+=1
            if elementD_HG == 1 and nbRD_HG == 1 :
                listElement.append([li,col])
            if elementD_HG == 0:
                li = li-1
                col = col-1
            if elementD_HG == 2:
                nbRD_HG+=1
                if nbRD_HG == 2 and nbVD_HG>=1 and nbZD_HG == 0 :
                    flagD_HG=True
                    for l,c in listElement:
                        matrice[l][c] = 2
                    print("Bien joue !")
                    changeEtat+=1    
                    break
                li = li-1
                col = col-1
            if elementD_HG == 2 and nbRD_HG == 1 and nbVD_HG == 0  :
                flagD_HG=False
            if elementD_HG == 1 and nbRD_HG ==1 :
                nbVD_HG+=1
                li = li-1
                col = col-1
                continue
            elif elementD_HG == 1 :
                li = li-1
                col = col-1
                continue
            if nbRD_HG < 2:
                flagD_HG=False
            
          

    #scan en diagonale en bas à gauche
    flagD_BG = True
    col = dicotraduction[colonne]
    li = dicotraduction[ligne]
    
    while flagD_BG == True :
        nbRD_BG=0
        nbVD_BG=0
        nbZD_BG=0
        listElement=[]
        while 0<=li<=7 and 0<=col<=7 :
            elementD_BG = matrice [li] [col]
            if elementD_BG == 0 and nbRD_BG ==1 :
                nbZD_BG+=1
            if elementD_BG == 1 and nbRD_BG == 1 :
                listElement.append([li,col])
            if elementD_BG == 0:
                li = li+1
                col = col-1
            if elementD_BG == 2:
                nbRD_BG+=1
                if nbRD_BG == 2 and nbVD_BG>=1 and nbZD_BG == 0 :
                    flagD_BG=True
                    for l,c in listElement:
                        matrice[l][c] = 2
                    print("Bien joue !")
                    changeEtat+=1    
                    break
                li = li+1
                col = col-1
            if elementD_BG == 2 and nbRD_BG == 1 and nbVD_BG == 0  :
                flagD_BG=False
            if elementD_BG == 1 and nbRD_BG ==1 :
                nbVD_BG+=1
                li = li+1
                col = col-1
                continue
            elif elementD_BG == 1 :
                li = li+1
                col = col-1
                continue
            if nbRD_BG < 2:
                flagD_BG=False
    return (changeEtat,matrice)


    

    
#Pour le choix des verts
def ChoixVerts(matrice):
    while True:
        print("\nGreenBuddy Choisissez dans quelle case vous voulez-placer votre protéine.\n  Si aucun coup n'est possible, vous pouvez passer votre tour en écrivant non comme colonne.\n" )
        colonne=input("\nQuelle colonne : ")
        nbNon=0
        if colonne == "non":
            nbNon=1
            ligne=0
            colonne=0
            return (ligne,colonne,nbNon)
        ligne=int(input("\nQuelle ligne: "))
        if  matrice[dicotraduction[ligne]][dicotraduction[colonne]]!=0:
            print("\nCette case est déja occupée, choisissez en une autre")
            continue
        else:
            matrice[dicotraduction[ligne]][dicotraduction[colonne]]=1
            (changeEtat,matrice)=calculV(matrice,ligne,colonne)
        if changeEtat !=0  :
                time.sleep(0.585)
                Affichage(matrice)
                break
        elif changeEtat == 0 :
            matrice[dicotraduction[ligne]][dicotraduction[colonne]]=0
            Affichage(matrice)
            print("Vous ne pouvez pas effectuer ce coup !")
        continue
    return (ligne,colonne,nbNon)


#Pour le choix des rouges
def ChoixRouges(matrice):
    while True:
        print("\nRedBuddy Choisissez dans quelle case vous voulez-placer votre protéine.\n Si aucun coup n'est possible, vous pouvez passer votre tour en écrivant non comme colonne.\n ")
        colonne=input("\nQuelle colonne : ")
        nbNon=0
        if colonne == "non":
            nbNon=1
            ligne=0
            colonne=0
            return (ligne,colonne,nbNon)
        ligne=int(input("\nQuelle ligne: "))
        if  matrice[dicotraduction[ligne]][dicotraduction[colonne]]!=0:
            print("\nCette case est déja occupée, choisissez en une autre")
            continue
        else:
            matrice[dicotraduction[ligne]][dicotraduction[colonne]]=2
            (changeEtat,matrice)=calculR(matrice,ligne,colonne)
            if changeEtat !=0  :
                time.sleep(0.585)
                Affichage(matrice)
                break
            elif changeEtat == 0 :
                matrice[dicotraduction[ligne]][dicotraduction[colonne]]=0
                Affichage(matrice)
                print("Vous ne pouvez pas effectuer ce coup !")
            continue
    return (ligne,colonne,nbNon)
    

def menu():
    print("Choix 1 : Lancer la partie")
    print ("Choix 2 : Voir les règles du jeu")
    print ("Choix 3 : Quitter le jeu")     


def regles():
    print("\nRègles du jeu de Moriarty : \n\nQuand une ou plusieurs proteines inhibees (pions verts) sont encadrees par 2 proteines activees (pions rouges), elles deviennent actives, c'est à dire que leur couleur passe du vert au rouge.")
    print("\nInversement, un ou plusieurs pions verts encadres par 2 pions rouges deviennent verts. Le gagnant est celui qui possède le plus de pions de sa couleur à la fin de la partie. La partie s'achève lorsqu'il n'y a plus de coups possibles.")
    print("\nMouvement des pions : \n\nOn ne peut jouer un coup que si le pion joué vient entourer un pion ou une rangée de pions rivaux. Le joueur place un pion sur une case adjacente à un pion de couleur opposée, de telle sorte qu'un ou plusieurs pions de l'adversaire se retrouvent pris en tenaille entre 2 pions de sa propre couleur (le pion qu'il vient de poser et un pion déjà sur le plateau). Les pions encadrés sont alors retournés et prennent la couleur de celui qui vient de jouer.")
    print("\nFin de la Partie : \n\nLa partie se termine généralement lorsque la grille est remplie mais elle peut aussi se terminer lorsqu'aucun coup n'est possible pour les deux joueurs. \n\n")

#And the winner is
def winner (matrice) :
    nbC = 0
    nbR = 0
    for c in range(8):
        for l in range(8):
            element = matrice[c][l]
            if element == 1 :
                nbC+=1
            if element == 2 :
                nbR+=1
    if nbC > nbR :
        print (" \n Fin de la partie \n\nAnd the winner is GrennBuddy avec un nombre de %d pions et RedBuddy n'a que %d pions ! \n"%(nbC,nbR))
    if nbR > nbC :
        print (" \n Fin de la partie \n\nAnd the winner is RedBuddy avec un nombre de %d pions et GreenBuddy n'a que %d pions ! \n"%(nbR,nbC))
    return matrice
            



########################################## Programme principal #####################################################
print("Bonjour bienvenue dans Moriarty le jeu qui va te carry ! \n Appuyez sur une touche pour lancer le jeu ")

#Variables
dicotraduction={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,1:0,2:1,3:2,4:3,5:4,6:5,7:6,8:7}

#Ici il faut que l'utilisateur appuie sur une touche pour que le jeu se lance
touche=input()
plateau=InitialisationPlateau()
reponse = 0


#Ici, c'est la gestion du menu
while reponse!=3 : 
    menu()
    reponse=int(input())
    if reponse==1 : 
        Affichage (plateau)
        n=1
        while n<31:
            print("tour n° ",n)
            (ligne,colonne,nbNonV)=ChoixVerts(plateau)
            (ligne,colonne,nbNonR)=ChoixRouges(plateau)
            if nbNonR == 1 and nbNonV == 1:
                break
            n=n+1
        winner(plateau)
        plateau=InitialisationPlateau()
            
    elif reponse==2:
        regles()
        continue
    elif reponse==3:
        print("Ciao !")
    else:
        print("choix incorrect")


