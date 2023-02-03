from math import*
from random import*








while True:
   ik=input("Anna isikukood: ") #str
   if len(ik)!=11:   #ne rovno 11
       print("Liiga palju või liiga vähe sümboleid. Sisesta veel kord: ")
   else:
        print("Isikukoodi kontroll")
        ik_list=list(ik)
        s1=int(ik_list[0]) #"1"->1
        if s1 not in [1,2,3,4,5,6]:
            print("Esimine sümbol ei ole õige!")
        else:
            print("Esimine sümbol on õige")
            y=ik_list[1]+ik_list[2] #aasta
            m=ik_list[3]+ik_list[4] #kuu
            d=ik_list[5]+ik_list[6] #päev
            if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
                print("Sünnipäev ei saa luua")
            else:
                if s1==1 or s1==2:
                    yy="18"
                elif s1==3 or s1==4:
                    yy="19"
                else:
                    yy="20"
                spaev=str(d)+"."+str(m)+"."+str(y) #ei ole ´18..,19,
                print(f"Sünnipäev on {spaev}")
                print({f"Viimane number: {ik_list[-1]}"})
            



            


#--------------------------------------
A= [ 3, 4, -1, 5, 0, 10, -12]
print([A[3]])
#Задание 6: Проверка имени
nfs=input("Введите имя => ")
if nfs.isalpha():
    ght="Здравствуйте " + nfs.capitalize()
    print(ght)
    lok = len(nfs)
    print("В данном имени", lok ,"столько букв")
    fx = "aeiouAEIOU"
    unix = 0
    ufix = 0
    for i in nfs:
        if i in fx:
            unix += 1
        else:
            ufix += 1
    print("В данном имени столько", unix, "гласных и столько",
          ufix, "согласных букв.")

else:
    print("Ошибка")

#-------------------------

#Задание 4: Сортировка
spisok=[-45,74,29,-1,0]
spisok.sort()
print(spisok)
spisok.sort(reverse=True)
print(spisok)



#5





#---------------------------
print("Задание 3")
arvud=[]
kogus=int(input("Kogus: "))
for i in range(kogus):
    arvud.append(randint(-100,100))
print(arvud)
max_arv=max(arvud)
ind=arvud.index(max_arv)
print(ind)
print(max_arv)
max_arv=round(max_arv/kogus,2)
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvud)
#--------------------------

print("Задание 2")
maakonnad=str(input(""))
osa1=[]
osa2=[]
print(maakonnad)
if len(maakonnad)%2==0 and len(maakonnad)>=2:
    n=int(len(maakonnad)/2)
    for i in range(1,n+1):
        osa1.append(maakonnad[i-1])
    for j in range(n+1,len(maakonnad)+1):
        osa2.append(maakonnad[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2)
else:
    print("viga")









print("Задание 2")
maakonnad=["Tln", "Narva", "K-Järve", "Ida-Virumma","Tartu","Tartumaa", "Viljandi", "Pärnumaa"]
osa1=[]
osa2=[]
print(maakonnad)
if len(maakonnad)%2==0 and len(maakonnad)>=2:
    n=int(len(maakonnad)/2)
    for i in range(1,n+1):
        osa1.append(maakonnad[i-1])
    for j in range(n+1,len(maakonnad)+1):
        osa2.append(maakonnad[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2)
else:
    print("viga")




#-------------------------------------------

print("Задание 1")
print()
index=""
maakonnad=["Tln", "Narva", "K-Järve", "Ida-Virumma","Tartu","Tartumaa", "Viljandi", "Pärnumaa", "Saarema"]
while True:
    try:
        index=int(input("Anna index: "))
        if index<99999 and index>10000:
            break
  

    except:
        print("Anna õige index!")
i=index//10000 #1,2,3,4,5,6,7,8,9
print(f"{index} on {maakonnad[i-1]}")
if i in [1,2,3]:
    print("Оставайтесь дома!")
else:
    print("Носите маски!")

