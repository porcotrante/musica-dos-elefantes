N=input("Digite o número de repetições da música, deverá ser real, positivo e maior doque 1:\n")
while not N.isdigit() or int(N)<=1:
    print("não aceito, tente novamente:")
    N=input("Digite o número de repetições da música, deverá ser real, positivo e maior doque 1:\n")
print("1 elefante incomoda muita gente")
inc="incomodam incomodam"
for i in range (2,(int(N))+1):
    if i%2==0:
        print(i,"elefantes",inc,"muito mais")
    elif i%2==1:
        print(i,"elefantes incomodam muita gente")
    inc+=" incomodam"
    i+=1