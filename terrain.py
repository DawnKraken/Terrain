#these are the functions that will be used
#climbing gear, magic (attackmagic, healmagic, slowfall, sneakymagic, light), spear, bow, arrow(expensive), stealth kit, disguise kit, chainmail, healthpotions,
stats = ["start",[],100,[],[],3,3,3,3]
GreaterLocation = "start"
#^location, inventory, gold, treasures, knowledge, hp, maxhp, mp, maxmp
inputy = None
AreaCheck = None
import random
import time

def checkinventory():
    print("Inventory: " + stats[1])
    print("Gold: " + stats[2])
    print(AreaCheck)

shop1stock = [1,1,1,1,1,1,1,1,15,1,1,5,5]
shop1items = ["ClimbingGear","AttackSpell","HealSpell","SlowFall","StealthSpell","LightSpell","Axe","Bow","Arrow","StealthKit","DisguiseKit","HealthPot", "MagicPot"]
shop1price = [20,10,20,15,15,10,5,10,3,15,5,5,5]

print("{0:15} | {1:4} | {2:4}".format("Item","Num","Price"))
print("{0:15} | {1:4} | {2:4}".format(shop1items[0],shop1stock[0],shop1price[0]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[1],shop1stock[1],shop1price[1]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[2],shop1stock[2],shop1price[2]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[3],shop1stock[3],shop1price[3]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[4],shop1stock[4],shop1price[4]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[5],shop1stock[5],shop1price[5]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[6],shop1stock[6],shop1price[6]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[7],shop1stock[7],shop1price[7]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[8],shop1stock[8],shop1price[8]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[9],shop1stock[9],shop1price[9]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[10],shop1stock[10],shop1price[10]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[11],shop1stock[11],shop1price[11]))
print("{0:15} | {1:4} | {2:4}".format(shop1items[12],shop1stock[12],shop1price[12]))
print("Gold: " + str(stats[2]))
inputy = input("What would you like to buy?")
TrueVar = True
while GreaterLocation == "start":
    if inputy == shop1items[0] and shop1stock[0] >= 1 and stats[2] >= shop1price[0]:
        stats[1].append(shop1items[0])
        shop1stock[0] = shop1stock[0] - 1
        stats[2] = stats[2] - shop1price[0]
    elif inputy == shop1items[1] and shop1stock[1] >= 1 and stats[2] >= shop1price[1]:
        stats[1].append(shop1items[1])
        shop1stock[1] = shop1stock[1] - 1
        stats[2] = stats[2] - shop1price[1]
    elif inputy == shop1items[2] and shop1stock[2] >= 1 and stats[2] >= shop1price[2]:
        stats[1].append(shop1items[2])
        shop1stock[2] = shop1stock[2] - 1
        stats[2] = stats[2] - shop1price[2]
    elif inputy == shop1items[3] and shop1stock[3] >= 1 and stats[2] >= shop1price[3]:
        stats[1].append(shop1items[3])
        shop1stock[3] = shop1stock[3] - 1
        stats[2] = stats[2] - shop1price[3]
    elif inputy == shop1items[4] and shop1stock[4] >= 1 and stats[2] >= shop1price[4]:
        stats[1].append(shop1items[4])
        shop1stock[4] = shop1stock[4] - 1
        stats[2] = stats[2] - shop1price[4]
    elif inputy == shop1items[5] and shop1stock[5] >= 1 and stats[2] >= shop1price[5]:
        stats[1].append(shop1items[5])
        shop1stock[5] = shop1stock[5] - 1
        stats[2] = stats[2] - shop1price[5]
    elif inputy == shop1items[6] and shop1stock[6] >= 1 and stats[2] >= shop1price[6]:
        stats[1].append(shop1items[6])
        shop1stock[6] = shop1stock[6] - 1
        stats[2] = stats[2] - shop1price[6]
    elif inputy == shop1items[7] and shop1stock[7] >= 1 and stats[2] >= shop1price[7]:
        stats[1].append(shop1items[7])
        shop1stock[7] = shop1stock[7] - 1
        stats[2] = stats[2] - shop1price[7]
    elif inputy == shop1items[8] and shop1stock[8] >= 1 and stats[2] >= shop1price[8]:
        stats[1].append(shop1items[8])
        shop1stock[8] = shop1stock[8] - 1
        stats[2] = stats[2] - shop1price[8]
    elif inputy == shop1items[9] and shop1stock[9] >= 1 and stats[2] >= shop1price[9]:
        stats[1].append(shop1items[9])
        shop1stock[9] = shop1stock[9] - 1
        stats[2] = stats[2] - shop1price[9]
    elif inputy == shop1items[10] and shop1stock[10] >= 1 and stats[2] >= shop1price[10]:
        stats[1].append(shop1items[10])
        shop1stock[10] = shop1stock[10] - 1
        stats[2] = stats[2] - shop1price[10]
    elif inputy == shop1items[11] and shop1stock[11] >= 1 and stats[2] >= shop1price[11]:
        stats[1].append(shop1items[11])
        shop1stock[11] = shop1stock[11] - 1
        stats[2] = stats[2] - shop1price[11]
    elif inputy == shop1items[12] and shop1stock[12] >= 1 and stats[2] >= shop1price[12]:
        stats[1].append(shop1items[12])
        shop1stock[12] = shop1stock[12] - 1
        stats[2] = stats[2] - shop1price[12]
    elif inputy == "help":
        print("You can always leave the shop, you know...")
    elif inputy == "n" or "leave" or "LEAVE" or "Leave" or "N" or "North" or "north" or "NORTH":
        GreaterLocation = "forest"
        stats[0] = "forest_entrance"
        break
    else:
        print("Sorry, you can't do that.")
    print("Inventory: " + str(stats[1]))
    print("Gold: " + str(stats[2]))

#torch, pickaxe, spare rope, healthpot, magicpot, repairspell, explosionspell
def shop2():
    shop2stock = [1,1,1,5,5,1,1]
    shop2items = ["Lamp", "Pickaxe", "SpareRope", "HealthPot", "MagicPot", "RepairSpell", "ExplosionSpell"]
    shop2price = [10, 10, 10, 5, 5, 10, 15]
    print("{0:15} | {1:4} | {2:4}".format("Item", "Num", "Price"))
    print("{0:15} | {1:4} | {2:4}".format(shop2items[0], shop2stock[0], shop2price[0]))
    print("{0:15} | {1:4} | {2:4}".format(shop2items[1], shop2stock[1], shop2price[1]))
    print("{0:15} | {1:4} | {2:4}".format(shop2items[2], shop2stock[2], shop2price[2]))
    print("{0:15} | {1:4} | {2:4}".format(shop2items[3], shop2stock[3], shop2price[3]))
    print("{0:15} | {1:4} | {2:4}".format(shop2items[4], shop2stock[4], shop2price[4]))
    print("{0:15} | {1:4} | {2:4}".format(shop2items[5], shop2stock[5], shop2price[5]))
    print("{0:15} | {1:4} | {2:4}".format(shop2items[6], shop2stock[6], shop2price[6]))
    inputy = input("What would you like to buy?")
    TrueVar = True
    while TrueVar == True:
        if inputy == "leave" or "exit" or "Leave" or "Exit" or "LEAVE" or "EXIT" or "e" or "east" or "E" or "EAST" or "East":
            stats[0] = "cliff_above"
            break
        elif inputy == shop2items[0] and shop2stock[0] >= 1 and stats[2] >= shop2price[0]:
            stats[1].append(shop2items[0])
            shop2stock[0] = shop2stock - 1
            stats[2] = stats[2] - shop2price[0]
        elif inputy == shop2items[1] and shop2stock[1] >= 1 and stats[2] >= shop2price[1]:
            stats[1].append(shop2items[1])
            shop2stock[1] = shop2stock - 1
            stats[2] = stats[2] - shop2price[1]
        elif inputy == shop2items[2] and shop2stock[2] >= 1 and stats[2] >= shop2price[2]:
            stats[1].append(shop2items[2])
            shop2stock[2] = shop2stock - 1
            stats[2] = stats[2] - shop2price[2]
        elif inputy == shop2items[3] and shop2stock[3] >= 1 and stats[2] >= shop2price[3]:
            stats[1].append(shop2items[3])
            shop2stock[3] = shop2stock - 1
            stats[2] = stats[2] - shop2price[3]
        elif inputy == shop2items[4] and shop2stock[4] >= 1 and stats[2] >= shop2price[4]:
            stats[1].append(shop2items[4])
            shop2stock[4] = shop2stock - 1
            stats[2] = stats[2] - shop2price[4]
        elif inputy == shop2items[5] and shop2stock[5] >= 1 and stats[2] >= shop2price[5]:
            stats[1].append(shop2items[5])
            shop2stock[5] = shop2stock - 1
            stats[2] = stats[2] - shop2price[5]
        elif inputy == shop2items[6] and shop2stock[6] >= 1 and stats[2] >= shop2price[6]:
            stats[1].append(shop2items[6])
            shop2stock[6] = shop2stock - 1
            stats[2] = stats[2] - shop2price[6]
def gameover():
    print("GAME OVER")
    time.sleep(2)
    print("Closing in")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Goodbye.")
    time.sleep(0.5)
    exit()

forest_entered = True
while GreaterLocation == "forest":
    while str(stats[0]) == "forest_entrance" and forest_entered == True:
        print("You are in a forest. To the north is a cliff, about 20 feet tall.")
        inputy = input("What will you do?")
        if inputy == "n" or "N" or "north" or "NORTH" or "North":
            randy = random.randint(1,20)
            if stats[1].count("ClimbingGear") >= 1:
                randy = randy + 5
            if randy >= 8:
                print("You got up over the ledge.")
                stats[0] = "cliff_above"
            elif randy < 8:
                print("You fall onto some rocks and injure yourself, losing 1hp.")
                stats[5] = stats[5] - 1
            else:
                print("Sorry, you can't do that here.")
    while str(stats[0]) == "cliff_above":
        if str(stats[0]) == "cliff_above":
            AreaCheck = "You are in a forest. You feel as though this is a crossroads for your journey. To the north is a big tree, to the wst is a cabin-shop, and to the east is a cave."
            inputy = input("To the west is a cabin-shop, to the east is a cave, and to the north is a very big tree. Where will you go?")
            if inputy == "W" or "w" or "west" or "West" or "WEST" or "cabin" or "Cabin" or "CABIN" or "Cabin-Shop" or "cabin-shop" or "CABIN-SHOP" or "cabinshop" or "Cabinshop" or "CABINSHOP":
                shop2()
            elif inputy == "n" or "N" or "north" or "North" or "NORTH":
                stats[0] = "floor1start"
                GreaterLocation = "tree"
            elif inputy == "e" or "E" or "East" or "east" or 'EAST':
                stats[0] = "cave_start"
                GreaterLocation = "cave"
        else:
            print("Sorry, you can't do that here.")

while GreaterLocation == "cave":
    rubble = False
    boarded = True
    while str(stats[0]) == "cave_entrance":
        AreaCheck = "The room is empty, aside for the description provided."
        inputy = input("The cave collapses, but you manage to escape the rubble. To the east is a tunnel.")
        if inputy == "e" or "E" or "east" or "East" or "EAST":
            str(stats[0]) == "cave_barren_1"
        else:
            print("Sorry, you can't do that here.")
    while str(stats[0]) == "cave_barren_1":
        inputy = input("To the north is a chasm, and to the northeast is a boarded up tunnel.")
        if inputy == "n" or "N" or "north" or "North" or "NORTH":
            stats[0] = "chasm_bridge"
        elif inputy == "ne" or "NE" or "northeast" or "Northeast" or "NORTHEAST" and stats[1].count("Axe") >= 1 and boarded == True:
            stats[0] = "boarded_tunnel"
            boarded = False
            print("You hack open the boards with your axe. To the north")
        elif inputy == "ne" or "NE" or "northeast" or "Northeast" or "NORTHEAST" and boarded == False:
            print("You go through to a crossroads of sorts. To the south is some rubble, and to the north is what appears to be a crossroads.")
            stats[0] = "boarded_tunnel"
        elif inputy == "ne" or "NE" or "northeast" or "Northeast" or "NORTHEAST" and stats[1].count("Axe") < 1 and boarded == True:
            print("Sorry, you need something to remove the boards first.")
        else:
            print("Sorry, you can't do that here.")
    while str(stats[0]) == "chasm_bridge":
        bridgerepaired = False
        if bridgerepaired == False:
            inputy = input("You see a great chasm to the north, about 20 feet wide. There is a broken bridge in the middle.")
        elif bridgerepaired == True:
            inputy = input("You see a great chasm to the north, about 20 feet wide. There is a bridge in the middle.")
        treasurecounty1 = 0
        if inputy == "jump" or "Jump" or "JUMP" or "n" or "N" or "north" or "North" or "NORTH" and stats[1].count("SlowFall") >= 1 and stats[7] >= 1:
            print("You fall, but manage to survive by casting a spell of slow falling.")
            stats[7] = stats[7] - 1
            stats[1] = "secret_tunnel"
        elif inputy == "Jump" or "Jump" or "JUMP" or "n" or "N" or "NORTH" or "North" or "NORTH" and stats[1].count("SlowFall") < 1:
            print("You fall to your death.")
            gameover()
        elif inputy == "RepairSpell" and stats[1].count("RepairSpell") == 1 and bridgerepaired == False and stats[7] >= 1:
            stats[7] = stats[7] - 1
            bridgerepaired = True
        elif inputy == "n" or "N" or "North" or "north" or "NORTH" and bridgerepaired == True:
            stats[0] = "bridge_across"
        elif inputy == "w" or "W" or "west" or "West" or "WEST" and treasurecounty1 == 0:
            print("Sorry, you can't do that here.")
            treasurecounty1 = treasurecounty1 + 1
        elif inputy == "w" or "W" or "west" or "West" or "WEST" and treasurecounty1 == 1:
            print("No seriously, you can't do that here.")
            treasurecounty1 = treasurecounty1 + 1
        elif inputy == "w" or "W" or "west" or "West" or "WEST" and treasurecounty1 == 2:
            print("I said stop trying to go west, there's nothing there.")
            treasurecounty1 = treasurecounty1 + 1
        elif inputy == "w" or "W" or "west" or "West" or "WEST" and treasurecounty1 == 3:
            print("The wall collapses from you bashing your head in, revealing a pearl necklace.")
            stats[3].append("pearl_necklace")
        else:
            print("Sorry, you can't do that here.")
    while str(stats[0]) == "secret_tunnel":
        print("You take a tunnel passage that leads to the beginning of the cave, finding some scattered coins along the way.")
        stats[2] = stats[2] + 50
        stats[0] = "cave_entrance"
    while str(stats[0]) == "bridge_across":
        inputy = input("To the east is what appears to be a crossroads. To the south is the bridge by which you got here.")
        if inputy == "s" or "S" or "south" or "SOUTH" or "South":
            stats[0] = "chasm_bridge"
        elif inputy == "e" or "E" or "east" or "East" or "EAST":
            stats[0] = "crossroads"
        else:
            print("Sorry, you can't do that here.")
    while str(stats[0]) == "crossroads":
        if boarded == True:
            inputy = input("To the north is PROGRESS. To the west is the other side of the bridge. To the south is a boarded up tunnel.")
        elif boarded == False:
            inputy = input("To the north is PROGRESS. TO the west is the other side of the bridge. To the south is a tunnel, filled with broken wood.")
        if inputy == "n" or "N" or "North" or "NORTH" or "north":
            GreaterLocation == "dark_lands"
            stats[0] = "dark_lands_entrance"
        elif inputy == "w" or "W" or "west" or "West" or "WEST":
            stats[0] = "bridge_across"
        elif inputy == "s" or "S" or "South" or "SOUTH" or "south":
            if boarded == False:
                stats[0] = "boarded_tunnel"
            elif boarded == True and stats[1].count("Axe") < 1:
                print("It's boarded up.")
            elif boarded == True and stats[1].count("Axe") >= 1:
                print("You hack away at the boards, destroying them.")
                boarded = False
                stats[0] = "boarded_tunnel"
    while str(stats[0]) == "boarded_tunnel":
        Areacheck = "You are in a tunnel. To the north is a crossroads, and to the south is some rubble"
        inputy = input("You are in a tunnel. To the north is a crossroads, and to the south is some rubble")
        if inputy == "n" or "N" or "north" or "North" or "NORTH":
            stats[0] = "crossroads"
        elif inputy == "s" or "S" or "south" or "SOUTH" or "South":
            stats[0] = "rubble"
    while str(stats[0]) == "rubble":
        inputy = input("You see a pile of rubble. You could dig through it, but it'd likely by a waste of time. To the north is a tunnel.")
        if inputy == "n" or "N" or "north" or "North" or "NORTH":
            stats[0] = "boarded_tunnel"
        elif inputy == "check" or "Check" or "CHECK":
            checkinventory()
        elif inputy == "dig" or "Dig" or "DIG":
            randy = random.int(1,100)
            if randy == 100:
                stats[3].append("emerald_ring")
            elif randy < 100:
                print("You couldn't find anything in the rubble.")
        else:
            print("Sorry, you can't do that here.")
def darklands():
    print("WIP, please download new from github if available")
def tree():
    bushesburnt = False
    foundsapphire = False
    while GreaterLocation == "tree":
        while str(stats[0]) == "floor1start":
            inputy = input("You are at the base of the tree. To the northwest is a passage, and another one lies to the east.")
            if inputy == "nw" or "Northwest" or "NW" or "NORTHWEST" or "northwest":
                stats[0] = "floor1-1"
            elif inputy == "e" or "E" or "east" or "East" or "EAST":
                stats[0] = "floor1-3"
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "floor1-1":
            inputy == "You are in an empty room. To the south is another empty room. To the northeast is what appears to be a three-way crossroads."
            if inputy == "s" or "S" or "south" or "South" or "SOUTH":
                stats[0] = "floor1-2"
            elif inputy == "ne" or "NE" or "Northeast" or "NORTHEAST" or "northeast":
                stats[0] = "floor1-5"
            elif inputy == "se" or "SE" or "southeast" or "Southeast" or "SOUTHEAST":
                stats[0] = "floor1start"
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "floor1-2":
            inputy = input("You are in a furnished room. To the north is the way you came in.")
            if inputy == "n" or "N" or "north" or "North" or "NORTH":
                stats[0] = "floor1-1"
            elif inputy == "e" or "E" or "east" or "East" or "EAST" and foundsapphire == False:
                stats[3].append("sapphire")
                print("You found a sapphire in a closet.")
                foundsapphire = True
            elif inputy == "e" or "E" or "east" or "East" or "EAST" and foundsapphire == True:
                print("You check the closet. It's full of rotting clothes.")
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "floor1-3":
            inputy = input("You are in a dirty room. To the north is another passage, and to the west is the way you came in.")
            if inputy == "w" or "W" or "west" or "West" or "WEST":
                stats[0] = "floor1start"
            elif inputy == "n" or "N" or "north" or "North" or "NORTH":
                stats[0] = "floor1-4"
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "floor1-4":
            inputy = input("To the south is a dirty room. To the east is another passage.")
            if inputy == "s" or "S" or "south" or "South" or "SOUTH":
                stats[0] = "floor1-3"
            elif inputy == "w" or "W" or "west" or "West" or "WEST":
                stats[0] = "floor1-5"
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "floor1-5":
            inputy = input("You are in a hallway, with a ladder on the north end. To the east is an empty room, and to the west is a dirty room.")
            if inputy == "n" or "N" or "north" or "North" or "NORTH":
                stats[0] = "ladder1"
            elif inputy == "e" or "E" or "east" or "East" or "EAST":
                stats[0] = "floor1-4"
            elif inputy == "w" or "W" or "west" or "West" or "WEST":
                stats[0] = "floor1-1"
        while str(stats[0]) == "ladder1":
            inputy = input("You are at the foot of a ladder.")
            if inputy == "u" or "U" or "up" or "Up" or "UP":
                stats[0] = "floor2start"
            elif inputy == "s" or "S" or "south" or "South" or "SOUTH":
                stats[0] = "floor1-5"
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "floor2start":
            if bushesburnt == False:
                inputy = input("To the south is another ladder, but the path is blocked by a prickly bush. The floor is tightly grown and the bushes are thick, so it seems ARSON is the only way forward")
            elif bushesburnt == True:
                inputy = input("To the south is another ladder. To the north is the ladder going down.")
            if inputy == "d" or "D" or "down" or "Down" or "DOWN":
                stats[0] = "ladder1"
            elif inputy == "AttackSpell" and stats[0].count("AttackSpell") == 1 and stats[7] >= 1 and bushesburnt == False:
                print("You cast a spell of fire and destroy the bushes.")
                stats[7] = stats[7] - 1
                bushesburnt = True
            elif inputy == "s" or "S" or "south" or "South" or "SOUTH" and bushesburnt == False:
                print("Path blocked!")
            elif inputy == "s" or "S" or "south" or "South" or "SOUTH" and bushesburnt == True:
                stats[0] = "ladder2"
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "ladder2":
            inputy = input("You are at the foot of another ladder.")
            if inputy == "u" or "U" or "up" or "Up" or "UP":
                stats[0] = "floor3start"
            elif inputy == "n" or "N" or "north" or "North" or "NORTH":
                stats[0] = "floor2start"
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "floor3start":
            inputy = input("You are at the top of a ladder. To the north is a forked passageway.")
            if inputy == "n" or "N" or "north" or "North" or "NORTH":
                stats[0] = "floor3-1"
            elif inputy == "d" or "D" or "down" or "Down" or "DOWN":
                stats[0] = "ladder2"
            else:
                print("Sorry, you can't do that here.")
        while str(stats[0]) == "floor3-1":
            inputy = input("You are at the fork in the road. To the northwest is a ramp guarded by a snake, and to the northeast is a wall that appears climbable, albeit difficult.")
            if inputy == "nw" or "NW" or "northwest" or "Northwest" or "NORTHWEST":
                stats[0] = "snake"
            elif inputy == "ne" or "NE" or "northeast" or "Northeast" or "NORTHEAST":
                stats[0] = "tree_cliff"
            elif inputy == "s" or "S" or "south" or "South" or "SOUTH":
                stats[0] = "floor3start"





def healthpot():
    county = stats.count("HealthPot")
    if county >= 1 and stats[5] < stats[6]:
        stats[1].remove("HealthPot")
        stats[5] = stats[5] + 1
    elif county >= 1 and stats[5] >= stats[6]:
        print("HP already maxxed out!")
def magicpot():
    county = stats.count("MagicPot")
    if county >= 1 and stats[7] < stats[8]:
        stats[1].remove("MagicPot")
        stats[7] = stats[7] + 1
    elif county >= 1 and stats[7] >= stats[8]:
        print("MP already maxxed out!")
def use(item):
    if item == "HealthPot":
        healthpot()
    elif item == "MagicPot":
        magicpot()
def regold():
    stats[2] = stats[2] + 50


def dataadd(data):
    data.append(data)
