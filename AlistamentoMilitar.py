nascimento = int(input("Qual a sua idade: "))
if nascimento <18:
    print("Voce ainda irá se alistar")
    print("Falta ainda {} para voce se alistar".format(18 - nascimento))
elif nascimento == 18:
    print("Esta na hora de se alistar")
else:
    print("Já passou o tempo de voce se alistar")
    print("Já se passaram {} anos para voce se alistar".format(nascimento - 18))