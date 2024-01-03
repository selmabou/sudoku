
ListPrincipale =[ 
        ["4","3","5","2","6","9","7","8","1"],
        ["6","8","2","5","7","1","4","9","3"],
        ["1","9","7","8","3","4","5","6","2"],
        ["8","2","6","1","9","5","3","4","7"],
        ["3","7","4","6","8","2","9","1","5"],
        ["9","5","1","7","4","3","6","2","8"],
        ["5","1","9","3","2","6","8","7","4"],
        ["2","4","8","9","5","7","1","3","6"],
        ["7","6","3","4","1","8","2","5","9"],
       ] 
       
for i in range (9):
    for j in range(9):
        print(ListPrincipale[i][j] , end="   ")
    print()

row = int(input("donnez num de row :"))
col = int(input("donnez num de col :"))
number = int(input("---> donnez un nombre (  555 --> sorte!!):"))

    
while number != 555 :
    ListPrincipale[row-1][col-1] = number
    
    row = int(input("donnez num de row :"))
    col = int(input("donnez num de col :"))
    number = int(input("---> donnez un nombre (  555 --> sorte!!):"))   
    
              
    
for i in range (9):
    for j in range(9):
        print(ListPrincipale[i][j] , end="   ")
    print()
    
    
    
#validation :
rowList = []
conteur1 = 0
for i in range(9):
    rowList = ListPrincipale[i]
        
    for j in range(9):
        for k in range(j+1 , 9):
            if rowList[k] == rowList[j]:
                conteur1 += 1
                
                           
if conteur1 != 0 :
    print("invalide row !!") 
else : 
    print("valider row ")                   

conteur2 = 0
for j in range(9):
    colList = []

    for i in range(9):
        colList.append(ListPrincipale[i][j]) 

    for y in range(9):
        for x in range(y+1 , 9):
            if colList[y] == colList[x]:
                conteur2 += 1


if conteur2 != 0 :
    print("invalide col !!")
else :
    print("valider col ")  
    
    
    
#validation de bloc
  
    
conteur3 = 0
for i in range(0,9,3):
    for j in range(0,9,3):
        blocList = []
        
        for x in range(i,i+3):
            for y in range(j,j+3):
                blocList.append(ListPrincipale[x][y])
                
        for k in range(9):
            for s in range(k+1 , 9):
                if blocList[k] == blocList[s]:
                    conteur3 += 1           
   
if conteur3 != 0 :
    print("invalide bloc !!")
else :
    print("valider bloc ")
    

           
                             
    