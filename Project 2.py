import time
import random
ice_minion=100
ice_dragon=1000
hero_hp=500
Hero_attack=0
ice_minion_attack_dmg=0
ice_dragon_attack_dmg=0
ice_dragon_attack="Icicle spear"
ice_minion_attack="Ice sword"
fire1="Fire breath"
fire2="meteor"
ice1="ice beam"
ice2="snowball meteor"
water1="water spray"
water2="poisionus rain"
print("Welcome to Elemental Dungeons!")
time.sleep(3)
print("You have been assinged a quest to vanquish all dragons from the realm")
time.sleep(3)
boolean=True
while boolean==True:
    Username=input("Enter your Username here: \n")
    Password=input("Enter your Password here: \n")
    if Username=="Slayer5482" and Password=="Password54321":
        boolean=False
    else:
        print("Invalid Entry")
time.sleep(3)

def Character_select():
    Hero=input("Enter your hero: HotDogg, IceCreamm, Fountain: \n")
    if Hero=="HotDogg":
        print("You have selected fire")
        time.sleep(2)
        print("Burn your way to victory")
    elif Hero=="IceCreamm":
        print("You have selected ice")
        time.sleep(2)
        print("Freeze your way to victory")
    elif Hero=="Fountain":
        print("You have selected water type")
        time.sleep(2)
        print("Ride the waves to victory")

print("Hello, you have entered the ice dungeon")
time.sleep(2)
Character_select()
time.sleep(2)

def HottDoggPowers():
    fire1="Fire breath"
    fire2="meteor"
    fire_special="Lava Ketchup"
    fire_summoning="Mini lava dragon"
   
def IceCreammPowers():
    ice1="ice beam"
    ice2="snowball meteor"
    ice_special="wafer cone"
    ice_summoning="ice dragon"
   
def FountainPowers():
    water1="water spray"
    water2="poisionus rain"
    water_special="tsunami"
    water_summoning="water dragon"
   
print("an ice minion is approaching")
time.sleep(2)
print("What attack would you like to use hero")
time.sleep(2)
Hero=input("Enter your hero: HotDogg, IceCreamm, Fountain: \n")
if Hero == "HotDogg":
    HottDoggPowers()
    power_use1=input("Choose your move, Fire breath, Meteor:\n ")
    print("you have used",power_use1)
    if power_use1 == "Fire breath":
        Hero_attack=random.randint(75,125)
        ice_minion=(ice_minion-Hero_attack)
        if ice_minion <= 0:
            print("you have slayed the ice minion")
        else:
            while ice_minion > 0:
                print("The ice minion has", ice_minion,"hp")
                time.sleep(2)
                print("Ice minion has used Ice sword")
                ice_minion_attack_dmg=random.randint(20,55)
                time.sleep(2)
                hero_hp=(hero_hp-ice_minion_attack_dmg)
                print("Your health is",hero_hp)
                Hero_attack=random.randint(75,125)
                ice_minion=(ice_minion-Hero_attack)
                print("You have used", power_use1)
            print("You have slayed the ice minion")
            time.sleep(2)
    elif power_use1 == "Meteor":
        Hero_attack=random.randint(175,225)
        ice_minion=(ice_minion-Hero_attack)
        print("You have slayed the ice minion")
elif Hero == "IceCreamm":
    IceCreammPowers()
    power_use2=input("Choose your move, ice beam, snowball mateor:\n ")
    print("you have used",power_use2)
    if power_use2 == "ice beam":
        Hero_attack=random.randint(30,70)
        ice_minion=(ice_minion-Hero_attack)
        if ice_minion <= 0:
            print("you have slayed the ice minion")
        else:
            while ice_minion > 0:
                print("The ice minion has", ice_minion,"hp")
                time.sleep(2)
                print("Ice minion has used Ice sword")
                ice_minion_attack_dmg=random.randint(20,55)
                time.sleep(2)
                hero_hp=(hero_hp-ice_minion_attack_dmg)
                print("Your health is",hero_hp)
                Hero_attack=random.randint(30,70)
                ice_minion=(ice_minion-Hero_attack)
                print("You have used", power_use2)
            print("You have slayed the ice minion")
            time.sleep(2)
    elif power_use2 == "snowball meteor":
        Hero_attack=random.randint(75,125)
        ice_minion=(ice_minion-Hero_attack)
        if ice_minion <= 0:
            print("you have slayed the ice minion")
        else:
            while ice_minion > 0:
                print("The ice minion has", ice_minion,"hp")
                time.sleep(2)
                print("Ice minion has used Ice sword")
                ice_minion_attack_dmg=random.randint(20,55)
                time.sleep(2)
                hero_hp=(hero_hp-ice_minion_attack_dmg)
                print("Your health is",hero_hp)
                Hero_attack=random.randint(75,125)
                ice_minion=(ice_minion-Hero_attack)
                print("You have used", power_use2)
            print("You have slayed the ice minion")
            time.sleep(2)
        print("You have slayed the ice minion")
elif Hero == "Fountain":
    FountainPowers()
    power_use3=input("Choose your move, water spray, poisionus rain:\n ")
    print("you have used",power_use3)
    if power_use3 == "water spray":
        Hero_attack=random.randint(15,45)
        ice_minion=(ice_minion-Hero_attack)
        if ice_minion <= 0:
            print("you have slayed the ice minion")
        else:
            while ice_minion > 0:
                print("The ice minion has", ice_minion,"hp")
                time.sleep(2)
                print("Ice minion has used Ice sword")
                ice_minion_attack_dmg=random.randint(20,55)
                time.sleep(2)
                hero_hp=(hero_hp-ice_minion_attack_dmg)
                print("Your health is",hero_hp)
                Hero_attack=random.randint(15,45)
                ice_minion=(ice_minion-Hero_attack)
                print("You have used",power_use3)
            print("You have slayed the ice minion")
            time.sleep(2)
    elif power_use3 == "snowball meteor":
        Hero_attack=random.randint(50,75)
        ice_minion=(ice_minion-Hero_attack)
        if ice_minion <= 0:
            print("you have slayed the ice minion")
        else:
            while ice_minion > 0:
                print("The ice minion has", ice_minion,"hp")
                time.sleep(2)
                print("Ice minion has used Ice sword")
                ice_minion_attack_dmg=random.randint(20,55)
                time.sleep(2)
                hero_hp=(hero_hp-ice_minion_attack_dmg)
                print("Your health is",hero_hp)
                Hero_attack=random.randint(50,75)
                ice_minion=(ice_minion-Hero_attack)
                print("You have used", power_use3)
            print("You have slayed the ice minion")
            time.sleep(2)
time.sleep(2)
print("the final boss is aproaching")
time.sleep(2)
print("the final boss is the ice dragon")
if Hero == "HotDogg":
    HottDoggPowers()
    Boss_moves1=input("Choose your move, Lava Ketchup = fire_special \n")
    time.sleep(2)
    print("you have used Lava ketchup")
    time.sleep(2)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("you have succeded in the ice dungeon")
elif Hero == "IceCreamm":
    IceCreammPowers()
    Boss_moves2=input("Choose your move, Strawberry suprise = Ice_special \n")
    time.sleep(2)
    print("you have used Strawberry suprise")
    time.sleep(2)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("you have succeded in the ice dungeon")
elif Hero == "Fountain":
    FountainPowers()
    Boss_moves3=input("Choose your move, Tsunami = Water_special \n")
    time.sleep(2)
    print("you have used Tsunami")
    time.sleep(2)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("you have succeded in the ice dungeon")