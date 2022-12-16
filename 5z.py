#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
X = False
Y = False
Z = False
if  (X or Y or Z) == (not X and not Y and not Z) :
    print(True)
else:
    print(False)