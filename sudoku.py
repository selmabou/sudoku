# for i in range(0,9):
#     print(" ",i, end="")
# for i in range (0,9):
#     print("") 
#     print(i, end="")
#     for j in range (0,9):
#         print(" - ", end="")




# def sudoku(row, col, number):
#     for i in range(0,9):
#         print(" ",i, end="")
#     for i in range (0,9):
#         for j in range(0,9):
#             if i == row and j == col:
#                 print(f"{number}", end="")
#             else:
#                 print(" ", end="")

#         print("") 
#         print(i, end="")
       

# sudoku(2,5,8)


ListPrincipale =[]
for i in range (9) :
    ListSecondaire = []
    for i in range(9):
        ListSecondaire.append("-")
    ListPrincipale.append(ListSecondaire)    
        
        
for i in range (9):
    for j in range(9):
        print(ListPrincipale[i][j] , end="   ")
    print()

row = int(input("donnez num de row :"))
col = int(input("donnez num de col :"))
number = int(input("donnez un nombre :"))

ListPrincipale[row-1][col-1] = number
for i in range (9):
    for j in range(9):
        print(ListPrincipale[i][j] , end="   ")
    print()

























































