
def validation(valList):
    for i in range(9):
            for j in range(i+1 , 9):
                if valList[i] == valList[j]:
                    return False
               
    return True
                
                
                
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
number = int(input("---> donnez un nombre (  555 --> stop!!):"))

    
while number != 555 :
    ListPrincipale[row-1][col-1] = str(number)
    
    row = int(input("donnez num de row :"))
    col = int(input("donnez num de col :"))
    number = int(input("---> donnez un nombre (  555 --> stop!!):"))   
    
              
    
for i in range (9):
    for j in range(9):
        print(ListPrincipale[i][j] , end="   ")
    print()
    
    
    
#validation :
#validation de row
rowList = []
conteur1 = 0
for i in range(9):
    rowList = ListPrincipale[i]
        
    if validation(rowList):
        conteur1 += 1
        
                
                           
if conteur1 != 9 :
    print("invalide row !!") 
else : 
    print("valider row ")                   
                

#validation de col 
conteur2 = 0
for i in range(9):
    colList = []
    for j in range (9):
        colList.append(ListPrincipale[i][j]) 
         
    if validation(colList) :
        conteur2 += 1


if conteur2 != 9 :
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
                
        if validation(blocList):
            conteur3 += 1           
   
if conteur3 != 9 :
    print("invalide bloc !!")
else :
    print("valider bloc ")
    
    

           
                             
