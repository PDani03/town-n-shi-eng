import random

def mely():
    inputt=input("Which one? ")
    if inputt=="":
        return 1
    else:
        return int(inputt)


def rand(max):
    return random.randint(1,max)


def item_make_rnd(rng):
    item_type.append(random.randint(0,2))

    if rng == "low":
        item_value.append((random.randint(1,25)/100)+1)

    elif rng=="med":
        item_value.append((random.randint(25,60)/100)+1)

    elif rng=="high":
        item_value.append((random.randint(60,120)/100)+1)

    elif rng=="legendary":
        item_value.append((random.randint(150,221)/100)+1)
    
    item_prefix.append(prefixes[rng])

    item_equip.append(0)


def item_delete(index):
    item_equip.pop(index)
    item_prefix.pop(index)
    item_value.pop(index)
    item_type.pop(index)


def equipped_item_dmg(): 
    if van_itemed():
        for i in range(len(item_equip)):
            if item_equip[i] == 1:

                if item_type[i] == 0:
                    return item_value[i]
                else:
                    return 1
    else:
        return 1

def equipped_item_df():
    if van_itemed():
        for i in range(len(item_equip)):
            if item_equip[i] == 1:

                if item_type[i] == 1:
                    return item_value[i]
                else:
                    return 1
    else:
        return 1

def equipped_item_healing():
    if van_itemed():
        for i in range(len(item_equip)):
            if item_equip[i] == 1:

                if item_type[i] == 2:
                    return item_value[i]
                else:
                    return 1
    else:
        return 1


def upgrade(prefix,index): #monstereknél egy kis chance hogy egyel jobb rarity-t kapjunk

    if prefix=="mid":
        item_prefix[index]="good"
        item_value[index]=(random.randint(25,60)/100)+1

    elif prefix=="good":
        item_prefix[index]="great"
        item_value[index]=(random.randint(60,120)/100)+1

    elif prefix=="great" and rand(2):
        item_prefix[index]="legendary"
        item_value[index]=(random.randint(150,221)/100)+1
    

def money_from_item_sale(itemValue):
    return round(itemValue*9,1)


def van_itemed():
    if len(item_type)!=0:
        return True


def print_items():
    for i in range(len(item_type)):
        if item_equip[i]==1:
            print(">", end=" ")
        print(f"{i+1}. {item_prefix[i]} {types[item_type[i]]}, {item_value[i]} multiplier")


    
item_type=[] #0 sword / 1 shield / 2 heal
item_value=[] #pl ha 1.25 akkor type alapján vagy 1.25-ös szorzó dmg-re, vagy 1.25-ös szorzó df-re
item_equip=[] #0 nincs equippelve / 1 equippelve van
item_prefix=[]

types={
    0:"sword",
    1:"shield",
    2:"salad"
}

prefixes={
    "low":"mid",
    "med":"good",
    "high":"great",
    "legendary":"legendary"
    }



#alap adatok:
'''
money=0
dmg=3
df=3 #defense

wpn_cost=10 #weapon cost
df_cost=10 #armor cost
'''

statok=[]

with open("cuccok.txt","r") as stats:
    for sor in stats:
        sor=sor.strip()
        statok.append(float(sor))

with open("items.txt","r",encoding='utf-8') as items:
    for sor in items:
        adatok=sor.strip().split(",")
        if adatok!=[""]:
            item_type.append(int(adatok[0]))
            item_value.append(float(adatok[1]))
            item_equip.append(int(adatok[2]))
            item_prefix.append(str(adatok[3]))

money=statok[0]
dmg=statok[1]
df=statok[2] #defense

wpn_cost=statok[3] #weapon cost
df_cost=statok[4] #armor cost


while True:

    hp=100

    with open("cuccok.txt","w") as stats:
        print(money, file=stats)
        print(dmg, file=stats)
        print(df, file=stats)
        print(wpn_cost, file=stats)
        print(df_cost, file=stats)
    
    with open("items.txt","w",encoding='utf-8') as items:
        for i in range(len(item_type)):
            print(item_type[i],",",item_value[i],",",item_equip[i],","+item_prefix[i], file=items)

    print()
    print("Everything saved, health restored!")
    print()
    print("Gold:",money)
    print("-------Town-------")
    print("1. Shop")
    print("2. Items")
    print("3. Adventure")
    print("4. Exit")
    valasztas=mely()
    print()

    if valasztas==4:
        exit()

    elif valasztas==1:
        bolt=True

        while bolt:
            print("-------Shop--------")
            print("Gold:",money)
            print(f"1. weapon upgrade, costs {wpn_cost} gold")
            print(f"2. Armor upgrade, costs {df_cost} gold")
            print("3. Sell")
            print("4. Back")
            valasztas=mely()
            print()

            if valasztas==1:
                if money>=wpn_cost:
                    dmg+=0.4
                    money=round(money-wpn_cost,1)
                    wpn_cost=round(wpn_cost*1.4,1)
                    print("weapon upgraded! Current damage:",dmg, end="")
                    input()
                    print()
                else:
                    input("Not enough money!")
                    print()
            
            elif valasztas==2:
                if money>=df_cost:
                    df+=0.4
                    money=round(money-df_cost,1)
                    df_cost=round(df_cost*1.4,1)
                    print("Páncél upgraded! Current defense:",df, end="")
                    input()
                    print()
                else:
                    input("Not enough money!")
                    print()
            
            elif valasztas==3:

                if van_itemed():
                    print_items()
                    
                    eladni=input("Which one?(press enter if none of them)")
                    if eladni!="":
                        eladni= int(eladni)-1

                        print(f"\Are you sure you want to sell your {item_prefix[eladni]} { types[ item_type[ eladni]]} for {money_from_item_sale(item_value[eladni])} gold?", end=" ")
                        if input("(y/n) ")=="y":
                            money+=round( money_from_item_sale(item_value[eladni]) ,1)
                            item_delete(eladni)
                    print()

                else:
                    input("You don't have any items to sell.")

            else:
                bolt=False


    elif valasztas==2:

        if van_itemed():
            print_items()

            equip_which=mely()-1

            for i in range(len(item_equip)):
                item_equip[i]=0

            item_equip[equip_which]=1
        
        else:
            input("You don't have any items.")


    elif valasztas==3:
        kaland=True
        harc=True

        diff=0

        hely=random.choice(["forest","cave"])

        print("You wander a little, and walk into a",hely+".")

        while kaland:
            
            #-------------------------------------------------------------------------------------#
            #kaland kezdete!!! / gameplay loop

            ossz_enemy=random.randint(diff+1, 3+diff) #hány enemy lesz


            most_enemy=[]
            while len(most_enemy)<ossz_enemy:
                if diff==0:
                    most_enemy.append("goblin")
                else:
                    if rand(10-diff)==1 or rand(10-diff)==2:
                        most_enemy.append("bandit")
                        #meg kell csinálni hogy 10(vagy 9 idk) legyen a max deepness!!(diff)
                        #megvan csinalva
                    else:
                        most_enemy.append("goblin")

            most_enemy.append("Elmenekülés")
                        

            while len(most_enemy)>1:

                print("You look around. You see some enemies:")
                for i in range(len(most_enemy)):
                    print(str(i+1)+".",most_enemy[i])
                #print(str(len(most_enemy)+1)+".","Elmenekülés")

                harcolni=mely()-1
                print()

                ##### enemy statok beállítása #####
                if most_enemy[harcolni]=="goblin":
                    enemy_hp=20
                    enemy_dmg=10
                    enemy_rng="low"
                    hit="goblin"

                elif most_enemy[harcolni]=="bandit":
                    enemy_hp=30
                    enemy_dmg=15
                    enemy_rng="med"
                    hit="bandit"
                ##### enemy statok beállítása #####
                else:
                    input("You got away.")
                    print()
                    kaland=False
                    harc=False
                    break
                
                enemy_hp=enemy_hp*(diff+1)*0.6
                enemy_dmg=enemy_dmg*(diff+1)*0.6

                while harc:
                    
                    most_df=df #csak azért kell ide is hogy rendesen lehessen védekezni

                    print("----"+most_enemy[harcolni],"fight----")
                    print(most_enemy[harcolni],"'s health:",round(enemy_hp,1))
                    print("your health:",round(hp,1))
                    print()
                    print("1. Attack")
                    print("2. Defend")
                    valasztas=mely()
                    print()

                    if valasztas==1:

                        most_dmg=round(random.uniform(dmg-1,dmg+1),1)
                        if van_itemed():
                            most_dmg=most_dmg*equipped_item_dmg()

                        enemy_hp=enemy_hp-most_dmg
                        print("You hit the",hit+"! It's hp was reduced by",round(most_dmg,1),"points!", end="")
                        input()

                        if enemy_hp<=0:
                            '''
                            money_aq=random.randint(money_aq-5,money_aq+5)
                            money=money+money_aq
                            print("You killed the enemy, és kaptál",money_aq,"aranyat!", end="")
                            '''
                            if rand(3)!=3:
                                print("You killed the enemy.", end="")
                            else:
                                print("You killed the enemy, and you saw an item on the floor!", end="")
                                input()
                                print("You got a ", end="")

                                item_make_rnd(enemy_rng)
                                if rand(4)==1:
                                    upgrade(item_prefix[-1],-1)
                                print(item_prefix[-1],types[item_type[-1]], end="")
                                print("!", end="")
                            
                            input()
                            print()
                            most_enemy.pop(harcolni)
                            break

                    else:
                        #most_df=most_df*1.5
                        if van_itemed():
                            most_df=most_df*equipped_item_df()

                        healing=3
                        
                        healing=healing*equipped_item_healing()
                        hp+=healing
                        if most_df!=most_df*equipped_item_df():
                            print("You put your shield in front of you, sturdying your defense!")
                        input(f"You had enough time to eat, restoring {healing} health points!")
                    

                    sebzodes=round(random.uniform(enemy_dmg-1,enemy_dmg+1),1)-most_df
                    if sebzodes<0:
                        sebzodes=0
                    hp=hp-sebzodes

                    print("The",most_enemy[harcolni]+"hit you, and you suffered",round(sebzodes,1),"damage!", end="")
                    input()
                    print()

                    if hp<=0:
                        input("You died. Everything you did'nt bring back to the town was lost.")
                        exit() 
            

            if kaland==True:
                if diff>=9:
                    input("You reached the end, and went back to the town.")
                    kaland=False
                    harc=False
                elif input("Go back to town, or continue?(t/c) ")=="v":
                    input("You went back to the town.")
                    kaland=False
                    harc=False
                else:
                    diff+=1
                    print()
