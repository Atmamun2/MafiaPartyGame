import time

MafiaGame = False
NameList = []
print(" |\                      /|")
print(" | \                    / |")
print(" |  \                  /  |")
print(" |   \                /   |")
print(" |    \              /    |")
print(" |     \            /     |")
print(" |      \          /      |")
print(" |       \        /       |")
print(" |        \      /        |")
print(" |         \    /         |")
print(" |          \  /          |")
print(" |           \/           |")
print()
time.sleep(2)

print("             /\            ")
print("            /  \           ")
print("           /    \          ")
print("          /      \         ")
print("         / ______ \        ")
print("        /          \       ")
print("       /            \      ")
print("      /              \     ")
print("     /                \    ")
print("    /                  \   ")
print("   /                    \  ")
print("  /                      \ ")
print()
time.sleep(2)

print("   ________________        ")
print("  |                        ")
print("  |                        ")
print("  |                        ")
print("  |________________        ")
print("  |                        ")
print("  |                        ")
print("  |                        ")
print("  |                        ")
print("  |                        ")
print("  |                        ")
print()
time.sleep(2)

print("    ______________________  ")
print("              |             ")
print("              |             ")
print("              |             ")
print("              |             ")
print("              |             ")
print("              |             ")
print("              |             ")
print("              |             ")
print("              |             ")
print("    __________|___________  ")
print()
time.sleep(2)

print("             /\            ")
print("            /  \           ")
print("           /    \          ")
print("          /      \         ")
print("         / ______ \        ")
print("        /          \       ")
print("       /            \      ")
print("      /              \     ")
print("     /                \    ")
print("    /                  \   ")
print("   /                    \  ")
print()
time.sleep(2)

RulesOfMafia = input("Would You Like To Listen To The Rules? Yes Or No?\n")

if RulesOfMafia.lower() == "yes":
    print("*****MAFIA MAIN IDEA*****")
    print("Welcome To The Mafia Game!\n")
    print(
        "This Game Was Designed For You To Be The Host So You Can Conduct The Game! Even If You Don't Know Anything About It!\n"
    )
    print(
        "Mafia Is A Murder Mystery Game! ALl About Deceiving Your Way To Victory!\n"
    )
    print("There Are Two Sides In Mafia. The Mafios And The Citizens\n")
    print("The Aim Of The Mafios Is To Kill All Of The Citizens\n")
    print("The Citizens Need To Execute The Mafios Through A Voting System!\n")
    print(
        "Whoever Has The Most Votes Will Be Executed To See If They Are A Mafios Member!\n"
    )
    print("If No Mafios Are Alive. Than Citizens Will Win!\n")
    print(
        "If The Number Of Mafios Are Equal To The Number Of Citizens. Mafia Wins!\n"
    )
    print()
    print()
    print("*****THE ROLES IN MAFIA*****\n")
    print(
        "There Are Many Citizens And Mafios Roles. The Ones In This Mafios Game Is:"
    )
    print(
        "The Mafia: A Normal Mafia Role Who Is Meant To Defeat The Citizens Until 1 Remains\n"
    )
    print("The Villager: The Normal Citizen. A Basic Citizen Figure\n")
    print(
        "The Doctor ( Citizen Role ): They Can Heal One Person Each Night To Save Them From The Mafios\n"
    )
    print(
        "The Detective ( Citizen Role ): They Can Investigate One Person Each Night To See If They Are The Mafios Member ( GodFathers Are Claimed Innocent Even If They Are Mafios-Member )\n"
    )
    print("*****OPTIONAL ROLES******")
    print(
        "The GodFather ( Mafios ): A Mafios Member Who Cannot Be Detected By The Detective (When Checked Will Be Classified As Innocent)\n"
    )
    print(
        "The Vigilante ( Citizen ): A Citizen Who Can Kill At Night BUT If They Pick Wrong They Will Die With The Citizen They Have Justified ( Killed ) Through Guilt If They Kill The Mafios Than The Mafios Has Been Justified\n"
    )
    print(
        "If The Vigilante Justifies Mafios Than They Live On To Make Another Day Of Judgement\n"
    )
    print()
    print()
    print("*****THE HOST ADVICE*****")
    print(
        "This Code Is Designed For A Host Whom Will Conduct The Mafia Game\n")
    print(
        "This Is Why Make Sure That As The Host You Write Down The Roles As The Ones Below\n"
    )
    print(
        "Villager:1, Villager:2 , Doctor:1 , Mafia:1 , Detective:1 , Vigilante:1 , GodFather:1 If They Are Multiple Of Any Of These It Will Be Villager:2 , Mafia:4 Etc\n"
    )
    print(
        "So Whatever The Mafios May Want To Kill, The Doctors Want To Heal, The Detective May Want To Check , The Vigilante May Want To Justify. You Need To Respond With The Role Of That Certain Person!\n"
    )
    print("You Need To Respond With The Roles 2 Lines Above\n")
    print(
        "You Have To Insert The Value So Make Sure That You Focus And Enter The Values\n"
    )
    print("If You Don't Understand Then That's Okay.\n")
    print("Try It Out For Yourself And You Might Just Understand.\n")
Ready = input("Ready?\n")

if Ready.lower() == "no" or Ready.lower() == "never" or Ready.lower(
) == "negative":
    print("We Will Give You Another 30 Seconds To Read\n")
    time.sleep(30)
    print("May The Mafia Game Begin!")
    print()
    time.sleep(2)

if RulesOfMafia.lower() == "no" or Ready.lower() == "yes" or Ready.lower(
) == "sure" or Ready.lower() == "alright" or Ready.lower() == "positive":
    print("May The Mafia Game Begin!")
    print()
    print()
    print()
    time.sleep(2)

while MafiaGame == False:
    MafiaValue = int(input("Give The Number of How Many Mafias\n"))

    VillagerValue = int(input("Give The Number of How Many Villagers\n"))

    DoctorValue = int(input("Will There Be A Doctor? 0. No 1. Yes\n"))

    DetectiveValue = int(input("Give The Number of How Many Detectives\n"))

    GodFatherValue = int(input("Give The Number of How Many GodFathers\n"))

    VigilanteValue = int(input("Give The Number of How Many Vigilantes\n"))

    TimeDiscussion = int(
        input("How Long Shall Discussions Last? ( In Seconds )\n"))

    AccusationTime = int(
        input("How Long Shall Accusation Time Last? ( In Seconds )\n"))

    RoleList = {
        "Villager": VillagerValue,
        "Doctor": DoctorValue,
        "Detective": DetectiveValue,
        "Mafia": MafiaValue,
        "GodFather": GodFatherValue,
        "Vigilante": VigilanteValue
    }

    Citizens = VillagerValue + DoctorValue + DetectiveValue + VigilanteValue

    Mafia_Sided = GodFatherValue + MafiaValue

    Players = Citizens + Mafia_Sided

    if Citizens <= Mafia_Sided or Mafia_Sided == 0:
        print("This Set Of People Cannot Work\n")
        continue

    if Players >= 15:
        print("This Set OF People Cannot Work\n")
        continue

    RandomList = []
    NameAddList = []
    NameDictionary = {}
    MafiaList = []
    VillagerList = []
    GodFatherList = []
    DetectiveList = []
    VigilanteList = []
    MafiosGodFatherList = []

    IsPersonKilled = False
    IsPersonHealed = False
    IsPersonChecked = False
    IsPersonJustified = False
    Voted_Period = False
    MafiaGame2 = False
    DetectiveOGValue = DetectiveValue
    MafiaDead = ""
    VigiDocSelf = ""
    DocSelf = ""
    VigiDetectiveCheckSelf = ""
    DetectiveCheckSelf = ""
    VigilanteJustifies = ""
    MafiaKill = ""
    DetectiveSelf = ""
    GodFatherDead = ""

    for i in RoleList:
        for j in range(RoleList[i]):
            RandomList.append(i + ":" + str(j + 1))

    for i in RandomList:
        print("Enter The Name Of", i)
        name = input()
        NameDictionary[i] = name

    for i in range(MafiaValue):
        index = (i + 1)
        MafiaList.append(NameDictionary["Mafia:" + str(index)])

    for i in range(VillagerValue):
        index = (i + 1)
        VillagerList.append(NameDictionary["Villager:" + str(index)])

    for i in range(GodFatherValue):
        index = (i + 1)
        GodFatherList.append(NameDictionary["GodFather:" + str(index)])

    for i in range(DetectiveValue):
        index = (i + 1)
        DetectiveList.append(NameDictionary["Detective:" + str(index)])

    for i in range(VigilanteValue):
        index = (i + 1)
        VigilanteList.append(NameDictionary["Vigilante:" + str(index)])

    MafiosGodFatherList = MafiaList + GodFatherList

    def MafiaFun(MafiaKill):
        global IsPersonKilled, Citizens, VillagerValue, DoctorValue, DetectiveValue, MafiaValue, DocSelf, DetectiveCheckSelf, GodFatherValue, VigilanteJustification, MafiaDead
        for i in RandomList:
            if MafiaKill == i:
                IsPersonKilled = True
                if i[:4] == "Vill":
                    VillagerValue = VillagerValue - 1
                    break
                if i[:4] == "GodF":
                    GodFatherValue = GodFatherValue - 1
                    break
                if i[:4] == "Doct":
                    DocSelf = "Doct"
                    break
                if i[:4] == "Dete":
                    DetectiveValue = DetectiveValue - 1
                    break
                if i[:4] == "Mafi":
                    MafiaDead == "Murdered"
                    MafiaValue = MafiaValue - 1
                    break
                if i[:4] == "Vigi":
                    VigilanteJustification = "Vigi"
                    break
        else:
            print("That Person Does Not Exist In The Game\n")

    def VigilanteJustice(VigilanteJustifies):
        global VigilanteValue, IsPersonJustified, DocSelf, DetectiveCheckSelf, VillagerValue, DetectiveValue, GodFatherValue, MafiaValue, VigiDocSelf, VigiDetectiveCheckSelf
        for i in RandomList:
            if VigilanteValue != 0:
                IsPersonJustified = True
                if VigilanteJustifies[:4] == "Vill":
                    VillagerValue = VillagerValue - 1
                    VigilanteValue = VigilanteValue - 1
                    break
                if VigilanteJustifies[:4] == "Doct":
                    VigiDocSelf = "Doct"
                    VigilanteValue = VigilanteValue - 1
                    break
                if VigilanteJustifies[:4] == "Dete":
                    DetectiveValue = DetectiveValue - 1
                    VigilanteValue = VigilanteValue - 1
                    break
                if VigilanteJustifies[:4] == "Mafi":
                    MafiaValue = MafiaValue - 1
                    break
                if VigilanteJustifies[:4] == "GodF":
                    GodFatherValue = GodFatherValue - 1
                    break
                if VigilanteJustifies[:4] == "Vigi":
                    VigilanteValue = VigilanteValue - 1
                    break
        else:
            print("That PersoN Does Not Exist In The Game\n")

    def DoctorFun(DoctorHeal):
        global IsPersonHealed, VillagerValue, DoctorValue, DetectiveValue, Citizens, MafiaValue, DocSelf, GodFatherValue, VigilanteValue, MafiaDead, GodFatherDead
        for i in RandomList:
            if DoctorHeal == i:
                print(i, "I")
                IsPersonHealed = True
                if VigiDocSelf == "Doct":
                    DoctorValue = 0
                if DocSelf == "Doct":
                    DoctorValue = 0
                if i[:4] == "Mafi":
                    MafiaDead = "Healed"
                    if MafiaDead == "Healed":
                        if MafiaKill == DoctorHeal:
                            MafiaValue = MafiaValue + 1
                            break
                        elif VigilanteJustifies == DoctorHeal:
                            MafiaValue = MafiaValue + 1
                            break
                if MafiaDead == "Murdered":
                    break
                if i[:4] == "Vill":
                    if MafiaKill[:4] == "Vill":
                        VillagerValue = VillagerValue + 1
                    break
                if i[:4] == "Doct":
                    DoctorValue = 1
                    break
                if i[:4] == "Dete":
                    DetectiveValue = DetectiveValue + 1
                    break
                if i[:4] == "GodF":
                    GodFatherDead = "Healed"
                    if GodFatherDead == "Healed":
                        if MafiaKill == DoctorHeal:
                            GodFatherValue = GodFatherValue + 1
                            break
                        elif VigilanteJustifies == DoctorHeal:
                            GodFatherValue = GodFatherValue + 1
                            break
                if i[:4] == "Vigi":
                    VigilanteValue = VigilanteValue + 1
                    break
        else:
            print("That Person Does Not Exist In The Game\n")

    def DetectiveFun(DetectiveChecks):
        global IsPersonChecked, VillagerValue, DoctorValue, DetectiveValue, Citizens, DetectiveCheckSelf, MafiaKill
        for i in RandomList:
            if DetectiveChecks == i:
                IsPersonChecked = True
                if i[:
                     4] == "Vill" or i[:
                                       4] == "Doct" or i[:
                                                         4] == "GodF" or i[:
                                                                           4] == "Vigi":
                    print("This Person Is ... INNOCENT!")
                else:
                    print("This Person Is ... MAFIA!")
                    break

    print("If The Mafios", MafiosGodFatherList,
          "Want To Kill Anyone Simply Say Yes Or No")
    MafiaNone = input()
    if Mafia_Sided != 0 and MafiaNone.lower() == "yes":
        while IsPersonKilled == False:
            print("Who Does The Mafiaos", MafiosGodFatherList, " Want To Kill")
            MafiaKill = input()
            MafiaFun(MafiaKill)

    if VigilanteValue != 0:
        print("If The Vigilantes", VigilanteList,
              "Want To Kill Anyone Simply Say Yes Or No")
        VigilanteNone = input()
        if VigilanteNone.lower() == "yes":
            while IsPersonJustified == False:
                for i in range(VigilanteValue):
                    print("Who Does The Vigilante", VigilanteList,
                          "Want To Justify?")
                    VigilanteJustifies = input()
                    if VigilanteJustifies not in RandomList:
                        print("This Person Does Not Exist In The Game\n")
                        continue
                    else:
                        VigilanteJustice(VigilanteJustifies)

    while IsPersonHealed == False:
        if DoctorValue == 1:
            print("Who Does The Doctor ['" + NameDictionary["Doctor:1"] +
                  "'] Want To Heal?")
            DoctorHeal = input()
            DoctorFun(DoctorHeal)
        else:
            print()
            print("... The Doctor Is Dead ...\n")
            break

    if DetectiveValue != 0:
        while IsPersonChecked == False:
            DetectiveCheckSelf = "Dete"
            for i in range(DetectiveOGValue):
                print("Who Does The Detective", DetectiveList,
                      "Want To Check?")
                DetectiveChecks = input()
                if DetectiveChecks[:4] == "Dete":
                    print("You Cannot Check Yourself\n")
                    continue
                if DetectiveChecks not in RandomList:
                    print("This Person Does Not Exist In The Game\n")
                    continue
                DetectiveFun(DetectiveChecks)
    else:
        print()
        print("... The Detective Is Dead ...\n")
        print("So Their Investigation Doesn't Matter\n")
    print()
    print("...Day Begins...\n")

    if MafiaKill[:4] == "Vill":
        if MafiaKill == DoctorHeal:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("A Villager Has Died!\n")

    if MafiaKill[:4] == "Doct":
        if MafiaKill == DoctorHeal:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("A Doctor Has Died!\n")

    if MafiaKill[:4] == "Dete":
        if MafiaKill == DoctorHeal:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("A Detective Has Died!\n")

    if MafiaKill[:4] == "GodF":
        if MafiaKill == DoctorHeal:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("A GodFather Has Died!\n")

    if MafiaKill[:4] == "Vigi":
        if MafiaKill == DoctorHeal:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("A Vigilante Has Died!\n")
    if MafiaKill[:4] == "Mafi":
        if MafiaKill == DoctorHeal:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[MafiaKill],
                  " Was Killed!\n")
            time.sleep(2)
            print("A Mafia Has Died! The Mafios Have Killed Themselves!\n")

    if VigilanteJustifies[:4] == "Vill":
        if VigilanteJustifies == DoctorHeal:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("A Villager Has Died!\n")
            print("Because The Vigilante Has Took The Life Of The Innocent!\n")
            print("The Vigilante Has Died!\n")

    if VigilanteJustifies[:4] == "Doct":
        if VigilanteJustifies == DoctorHeal:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("A Doctor Has Died!\n")
            print("Because The Vigilante Has Took The Life Of The Innocent!\n")
            print("The Vigilante Has Died!\n")

    if VigilanteJustifies[:4] == "Mafi":
        if VigilanteJustifies == DoctorHeal:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print(
                "Because The Vigilante Has Took The Of A Mafios! Well Done!\n")
            print("A Mafia Has Died!\n")

    if VigilanteJustifies[:4] == "Dete":
        if VigilanteJustifies == DoctorHeal:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("A Detective Has Died!\n")
            print("Because The Vigilante Has Took The Life Of The Innocent!\n")
            print("The Vigilante Has Died!\n")

    if VigilanteJustifies[:4] == "GodF":
        if VigilanteJustifies == DoctorHeal:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("The Vigilante Has Took The Life Of A Mafios! Well Done!\n")
            print("A GodFather Has Died!\n")

    if VigilanteJustifies[:4] == "Vigi":
        if VigilanteJustifies == DoctorHeal:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("But They Were Saved By The Doctor!\n")
        else:
            print("During The Night ", NameDictionary[VigilanteJustifies],
                  " Was Justified!\n")
            time.sleep(2)
            print("A Villager Has Died!\n")
            print("Because The Vigilante Has Took The Life Of The Himself!\n")
            print("The Vigilante Has Died!\n")

    time.sleep(2)
    Mafia_Sided = MafiaValue + GodFatherValue
    time.sleep(2)
    if Mafia_Sided == Citizens:
        print()
        print("The Number of Mafia Equals To The Number Of Villagers\n")
        print("Mafia Wins!\n")
        MafiaGame = True
        break
    time.sleep(2)
    if Mafia_Sided == 0:
        print("All The Mafios Are Defeated!\n")
        print("The Citizens Wins!\n")
        break
    print("DISCUSSION TIME BEGINS!\n")
    for i in range(TimeDiscussion):
        print(str(TimeDiscussion - i) + " Seconds Remaining...")
        time.sleep(1)
    print()
    print("DISCUSSION TIME IS OVER!\n")
    TieQuestion = input("Is There A Tie Breaker? Yes Or No?\n")
    if TieQuestion.lower() == "yes":
        TieBreakerP1 = input("Who Is The First Tied Person?\n")
        if TieBreakerP1[:
                        4] == "Mafi" or TieBreakerP1[:
                                                     4] == "Doct" or TieBreakerP1[:
                                                                                  4] == "Dete" or TieBreakerP1[:
                                                                                                               4] == "Vill" or TieBreakerP1[:
                                                                                                                                            4] == "GodF" or TieBreakerP1[:
                                                                                                                                                                         4] == "Vigi":
            TieBreakerP2 = input("Who Is The Second Tied Person?\n")
            if TieBreakerP2[:
                            4] == "Mafi" or TieBreakerP2[:
                                                         4] == "Doct" or TieBreakerP2[:
                                                                                      4] == "Dete" or TieBreakerP2[:
                                                                                                                   4] == "Vill" or TieBreakerP2[:
                                                                                                                                                4] == "GodF" or TieBreakerP2[:
                                                                                                                                                                             4] == "Vigi":
                print()
                print("Both Accused Have ", AccusationTime,
                      " Seconds To Explain Why They Are Not Mafia-Sided.\n")
                for f in range(AccusationTime):
                    print(str(AccusationTime - f) + " Seconds Remaining...")
                    time.sleep(1)
                print()
                print("Time Is Up! May The Other Accused Rise And Speak\n")
                for f in range(AccusationTime):
                    print(str(AccusationTime - f) + " Seconds Remaining...")
                    time.sleep(1)
                Voted1 = input("Who Has Been Executed?\n")
                if Voted1[:4] == "Mafi":
                    MafiaValue = MafiaValue - 1
                    if Mafia_Sided == 0:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("GodFather!\n")
                        print("Citizens Wins!\n")
                        break

                    elif Mafia_Sided != 0:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("GodFather!\n")
                        print("Mafios Still Remains!\n")
                        print("...The Game Continues...!\n")
                        print()
                        print("The People Who Remain Are\n")
                        print("The Value Of Mafias Is: ", MafiaValue)
                        print()
                        print("The Value Of Villagers Is: ", VillagerValue)
                        print()
                        if DoctorValue == 1:
                            print("The Doctor Is Alive.")
                        if DoctorValue == 0:
                            print("The Doctor Is Dead.")
                        print()
                        print("The Value Of Detectives Is: ", DetectiveValue)
                        print()
                        print("The Value Of GodFathers Is:", GodFatherValue)
                        print()
                        print("The Value Of Vigilantes Is:", VigilanteValue)
                        continue

                if Voted1[:4] == "Vill":
                    VillagerValue = VillagerValue - 1
                    if Citizens == Mafia_Sided:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("Villager!\n")
                        print(
                            "The Number Of Mafios Is Equal To The Number Of Citizens!\n"
                        )
                        time.sleep(2)
                        print("Mafia Wins!\n")
                        break

                    if Citizens != Mafia_Sided:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("Villager!\n")
                        print("...The Game Continues...!\n")
                        print()
                        print("The People Who Remain Are\n")
                        print("The Value Of Mafias Is: ", MafiaValue)
                        print()
                        print("The Value Of Villagers Is: ", VillagerValue)
                        print()
                        if DoctorValue == 1:
                            print("The Doctor Is Alive.")
                        if DoctorValue == 0:
                            print("The Doctor Is Dead.")
                        print()
                        print("The Value Of Detectives Is: ", DetectiveValue)
                        print()
                        print("The Value Of GodFathers Is:", GodFatherValue)
                        print()
                        print("The Value Of Vigilantes Is:", VigilanteValue)

                        continue

                if Voted1[:4] == "Doct":
                    DoctorValue = 0
                    if Citizens == Mafia_Sided:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("Doctor!\n")
                        print(
                            "The Number Of Mafios Is Equal To The Number Of Citizens!\n"
                        )
                        time.sleep(2)
                        print("Mafia Wins!\n")
                        break

                    if Citizens != Mafia_Sided:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("Doctor!\n")
                        print("...The Game Continues...!\n")
                        print()
                        print("The People Who Remain Are\n")
                        print("The Value Of Mafias Is: ", MafiaValue)
                        print()
                        print("The Value Of Villagers Is: ", VillagerValue)
                        print()
                        if DoctorValue == 1:
                            print("The Doctor Is Alive.")
                        if DoctorValue == 0:
                            print("The Doctor Is Dead.")
                        print()
                        print("The Value Of Detectives Is: ", DetectiveValue)
                        print()
                        print("The Value Of GodFathers Is:", GodFatherValue)
                        print()
                        print("The Value Of Vigilantes Is:", VigilanteValue)
                        continue

                if Voted1[:4] == "Dete":
                    DetectiveValue = DetectiveValue - 1
                    if Citizens == Mafia_Sided:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("Detective!\n")
                        print(
                            "The Number Of Mafios Is Equal To The Number Of Citizens!\n"
                        )
                        time.sleep(2)
                        print("Mafia Wins!\n")
                        break

                    if Citizens != Mafia_Sided:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("Detective!\n")
                        print("...The Game Continues...!\n")
                        print()
                        print("The People Who Remain Are\n")
                        print("The Value Of Mafias Is: ", MafiaValue)
                        print()
                        print("The Value Of Villagers Is: ", VillagerValue)
                        print()
                        if DoctorValue == 1:
                            print("The Doctor Is Alive.")
                        if DoctorValue == 0:
                            print("The Doctor Is Dead.")
                        print()
                        print("The Value Of Detectives Is: ", DetectiveValue)
                        print()
                        print("The Value Of GodFathers Is:", GodFatherValue)
                        print()
                        print("The Value Of Vigilantes Is:", VigilanteValue)
                        continue

                if Voted1[:4] == "GodF":
                    GodFatherValue = GodFatherValue - 1
                    if Mafia_Sided == 0:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("GodFather!\n")
                        print("Citizens Wins!\n")
                        break

                    elif Mafia_Sided != 0:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("GodFather!\n")
                        print("Mafios Still Remains!\n")
                        print("...The Game Continues...!\n")
                        print()
                        print("The People Who Remain Are\n")
                        print("The Value Of Mafias Is: ", MafiaValue)
                        print()
                        print("The Value Of Villagers Is: ", VillagerValue)
                        print()
                        if DoctorValue == 1:
                            print("The Doctor Is Alive.")
                        if DoctorValue == 0:
                            print("The Doctor Is Dead.")
                        print()
                        print("The Value Of Detectives Is: ", DetectiveValue)
                        print()
                        print("The Value Of GodFathers Is:", GodFatherValue)
                        print()
                        print("The Value Of Vigilantes Is:", VigilanteValue)
                        continue

                if Voted1[:4] == "Vigi":
                    VigilanteValue = VigilanteValue - 1
                    if Citizens == Mafia_Sided:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("Vigilante!\n")
                        print(
                            "The Number Of Mafios Is Equal To The Number Of Citizens!\n"
                        )
                        time.sleep(2)
                        print("Mafia Wins!\n")
                        break

                    if Citizens != Mafia_Sided:
                        print("The Role Of This Person Is\n")
                        time.sleep(2)
                        print("Vigilante!\n")
                        print("...The Game Continues...!\n")
                        print()
                        print("The People Who Remain Are\n")
                        print("The Value Of Mafias Is: ", MafiaValue)
                        print()
                        print("The Value Of Villagers Is: ", VillagerValue)
                        print()
                        if DoctorValue == 1:
                            print("The Doctor Is Alive.")
                        if DoctorValue == 0:
                            print("The Doctor Is Dead.")
                        print()
                        print("The Value Of Detectives Is: ", DetectiveValue)
                        print()
                        print("The Value Of GodFathers Is:", GodFatherValue)
                        print()
                        print("The Value Of Vigilantes Is:", VigilanteValue)
                        continue

    if TieQuestion.lower() == "no":
        Voted2 = input("Who Has Been Executed? ")
        if Voted2[:4] == "Mafi":
            MafiaValue = MafiaValue - 1
            if Mafia_Sided == 0:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Mafia!\n")
                print("Citizens Wins!\n")
                break

            elif Mafia_Sided != 0:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Mafia!\n")
                print("Mafios Still Remains!\n")
                print("...The Game Continues...!\n")
                print()
                print("The People Who Remain Are\n")
                print("The Value Of Mafias Is: ", MafiaValue)
                print()
                print("The Value Of Villagers Is: ", VillagerValue)
                print()
                if DoctorValue == 1:
                    print("The Doctor Is Alive.")
                if DoctorValue == 0:
                    print("The Doctor Is Dead.")
                print()
                print("The Value Of Detectives Is: ", DetectiveValue)
                print()
                print("The Value Of GodFathers Is:", GodFatherValue)
                print()
                print("The Value Of Vigilantes Is:", VigilanteValue)
                continue

        if Voted2[:4] == "Vill":
            VillagerValue = VillagerValue - 1
            if Citizens == Mafia_Sided:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Villager!\n")
                print(
                    "The Number Of Mafios Is Equal To The Number Of Citizens!\n"
                )
                time.sleep(2)
                print("Mafia Wins!\n")
                break

            if Citizens != Mafia_Sided:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Viilager!\n")
                print("...The Game Continues...!\n")
                print()
                print("The People Who Remain Are\n")
                print("The Value Of Mafias Is: ", MafiaValue)
                print()
                print("The Value Of Villagers Is: ", VillagerValue)
                print()
                if DoctorValue == 1:
                    print("The Doctor Is Alive.")
                if DoctorValue == 0:
                    print("The Doctor Is Dead.")
                print()
                print("The Value Of Detectives Is: ", DetectiveValue)
                print()
                print("The Value Of GodFathers Is:", GodFatherValue)
                print()
                print("The Value Of Vigilantes Is:", VigilanteValue)
                continue

        if Voted2[:4] == "Doct":
            DoctorValue = 0
            if Citizens == Mafia_Sided:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Doctor!\n")
                print(
                    "The Number Of Mafios Is Equal To The Number Of Citizens!\n"
                )
                time.sleep(2)
                print("Mafia Wins!\n")
                break

            if Citizens != Mafia_Sided:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Vigilante!\n")
                print("...The Game Continues...!\n")
                print()
                print("The People Who Remain Are\n")
                print("The Value Of Mafias Is: ", MafiaValue)
                print()
                print("The Value Of Villagers Is: ", VillagerValue)
                print()
                if DoctorValue == 1:
                    print("The Doctor Is Alive.")
                if DoctorValue == 0:
                    print("The Doctor Is Dead.")
                print()
                print("The Value Of Detectives Is: ", DetectiveValue)
                print()
                print("The Value Of GodFathers Is:", GodFatherValue)
                print()
                print("The Value Of Vigilantes Is:", VigilanteValue)
                continue

        if Voted2[:4] == "Dete":
            DetectiveValue = DetectiveValue - 1
            if Citizens == Mafia_Sided:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Detective!\n")
                print(
                    "The Number Of Mafios Is Equal To The Number Of Citizens!\n"
                )
                time.sleep(2)
                print("Mafia Wins!\n")
                break

            if Citizens != Mafia_Sided:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Detective!\n")
                print("...The Game Continues...!\n")
                print()
                print("The People Who Remain Are\n")
                print("The Value Of Mafias Is: ", MafiaValue)
                print()
                print("The Value Of Villagers Is: ", VillagerValue)
                print()
                if DoctorValue == 1:
                    print("The Doctor Is Alive.")
                if DoctorValue == 0:
                    print("The Doctor Is Dead.")
                print()
                print("The Value Of Detectives Is: ", DetectiveValue)
                print()
                print("The Value Of GodFathers Is:", GodFatherValue)
                print()
                print("The Value Of Vigilantes Is:", VigilanteValue)
                continue

        if Voted2[:4] == "GodF":
            GodFatherValue = GodFatherValue - 1
            if Mafia_Sided == 0:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("GodFather!\n")
                print("Citizens Wins!\n")
                break

            elif Mafia_Sided != 0:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("GodFather!\n")
                print("Mafios Still Remains!\n")
                print("...The Game Continues...!\n")
                print()
                print("The People Who Remain Are\n")
                print("The Value Of Mafias Is: ", MafiaValue)
                print()
                print("The Value Of Villagers Is: ", VillagerValue)
                print()
                if DoctorValue == 1:
                    print("The Doctor Is Alive.")
                if DoctorValue == 0:
                    print("The Doctor Is Dead.")
                print()
                print("The Value Of Detectives Is: ", DetectiveValue)
                print()
                print("The Value Of GodFathers Is:", GodFatherValue)
                print()
                print("The Value Of Vigilantes Is:", VigilanteValue)
                continue

        if Voted2[:4] == "Vigi":
            VigilanteValue = VigilanteValue - 1
            if Citizens == Mafia_Sided:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Vigilante!\n")
                print(
                    "The Number Of Mafios Is Equal To The Number Of Citizens!\n"
                )
                time.sleep(2)
                print("Mafia Wins!\n")
                break

            if Citizens != Mafia_Sided:
                print("The Role Of This Person Is\n")
                time.sleep(2)
                print("Vigilante!\n")
                print("...The Game Continues...!\n")
                print()
                print("The People Who Remain Are\n")
                print("The Value Of Mafias Is: ", MafiaValue)
                print()
                print("The Value Of Villagers Is: ", VillagerValue)
                print()
                if DoctorValue == 1:
                    print("The Doctor Is Alive.")
                if DoctorValue == 0:
                    print("The Doctor Is Dead.")
                print()
                print("The Value Of Detectives Is: ", DetectiveValue)
                print()
                print("The Value Of GodFathers Is:", GodFatherValue)
                print()
                print("The Value Of Vigilantes Is:", VigilanteValue)
                continue

print("Thank You For Playing The Mafia Host Game!")
print("Make Sure To Gather Your Friends!")
print("For Another Game Of Mafia!")
print("Until We Meet Again!")
print("Make Sure You Aren't Going To Be Murdered By The Mafios!")
