class TheLibrary:
    def __init__(self):
        
        #   Welcome! Don't forget your library card:
        #   _______________________________________
        #   |   ______                            |
        #   |  |  ()  |    THE VIRTUAL LIBRARY    |
        #   |  | /[]\ |    LIBRARY CARD           |
        #   |  |  /\  |    NAME: JOHN SMITH       |
        #   |  |______|                           |   
        #   | BARCODE: |  _ |  |  _ | _  _ _  |   |
        #   | CARD # : 4 19 5 23 10 5 2 16 8 25   |
        #   |_____________________________________|

        self.myAry = []
        self.nextValue = 1

    def __str__(self):
        print('This is the Library!')

    def FunctionA(self):
        if len(self.myAry) < 6:
            self.nextValue *= 2
            self.myAry.append(self.nextValue)
        else:
            print("Call these functions 6 times, no more, no less")
            self.myAry.clear()
            self.nextValue = 1

    def FunctionB(self):
        if len(self.myAry) < 6:
            self.nextValue += 5
            self.myAry.append(self.nextValue)
        else:
            print("Call these functions 6 times, no more, no less")
            self.myAry.clear()
            self.nextValue = 1

    def FunctionC(self):
        if len(self.myAry) < 6:
            self.myAry.append(self.nextValue)
        else:
            print("Call these functions 6 times, no more, no less")
            self.myAry.clear()
            self.nextValue = 1

    def FunctionD(self):
        if len(self.myAry) < 6:
            self.nextValue = self.nextValue % 3
            self.myAry.append(self.nextValue)
        else:
            print("Call these functions 6 times, no more, no less")
            self.myAry.clear()
            self.nextValue = 1

    def FunctionE(self):
        if len(self.myAry) < 6:
            self.nextValue = round(self.nextValue / 3) + 2
            self.myAry.append(self.nextValue)
        else:
            print("Call these functions 6 times, no more, no less")
            self.myAry.clear()
            self.nextValue = 1

    def TalkToAnEmployee(self):
        print("Hey! You're the new worker, yea? Great!")
        print("Can you go reorganize the alphabet functions?")
        print("Call them sequetially in the correct order,")
        print("then see me again once you're done.")
        
    def TalkToAnEmployeeAgain(self):
        if len(self.myAry)==6:
            print("Done? Thanks! Wait... You're not an employee?")
            print("Why didn't you say so!? Sorry about that...")
            print("Here, take this as my apology,")
            print("it's what you need for the waterslide: ")
            outputAry = []
            outputAry.append(chr(self.myAry[0] * 19 + 2))
            outputAry.append(chr(round(pow(self.myAry[1], 3)) + 41))
            outputAry.append(chr(ord('d') - self.myAry[2]))
            outputAry.append(chr(round(pow(self.myAry[3], 3) * 12) + 11))
            outputAry.append(chr(self.myAry[4] * 15 - 4))
            outputAry.append(chr(self.myAry[5] + 112))
            print(''.join(outputAry))
        else:
            print("Looks like you haven't put those alphabet books in the right order yet!")

    def BookBorrowingCard(self, first: str, second: str, third: str, fourth: str, fifth: str, sixth: str):
        print("Written on the back of this borrowing card is")
        print("'Everyone else got out...")
        print("I miss my friends. I miss the world.")
        print("I even miss my favorite snack: ")
        favoriteSnack = []
        favoriteSnack.append(fourth[1])
        favoriteSnack.append(chr((len(first) * 22) + 2))
        favoriteSnack.append(chr(((ord(fifth[1]) - ord('a')) + 3) + ord('a')))
        favoriteSnack.append(chr(ord('d') + (-2 * (ord(third[2]) - ord('l')))))
        favoriteSnack.append(sixth[2])
        favoriteSnack.append(second[2])
        favoriteSnack.append("'")
        print(''.join(favoriteSnack))

    def DoSomething(self):
        numbers = [48, 72, 88, 0, 48, 72]
        print("You find a button that says 'Do Something'. You press it.")
        for number in numbers:
            self.HelpDoSomething(number)

    def HelpDoSomething(self, val: int):
        moreNumbers =  ["11", "111", "01111", "21", "022", "0111", "011", "03", "211", "021", "31", "4", "013", "01", "3", "112", "0211", "02", "1", "12", "2", "0112", "012", "13", "0121", "121"]
        rank = val >> 2
        if rank >= 0 and rank < 26:
            useThis = moreNumbers[rank]
            for i in range(0,len(useThis)):
                next = ord(useThis[i]) - ord('0')
                for j in range(0,next):
                    if ((i + 1) % 2 == 1):
                        self.simpleOne()
                    else:
                        self.simpleTwo()
            print()

    def simpleOne(self):
        print(chr(46),end="")

    def simpleTwo(self):
        print(chr(45),end="")

    def VigenereDecryptor(self, keyInput: str, scrambledInput: str) -> str:
        scrambledInputAry = list(scrambledInput)
        keyAry = list(keyInput)
        keyIndex = 0
        plainText = []
        for index in range(0,len(scrambledInputAry)):
            if 0 > ord(scrambledInputAry[index])-ord('a') or ord(scrambledInputAry[index])-ord('a') > 26:
                plainText.append(scrambledInputAry[index])
                continue
            scrambledInputAry[index] = ((ord(scrambledInputAry[index])-ord('a'))-(ord(keyAry[keyIndex])-ord('a')))%26
            keyIndex = (keyIndex + 1) % len(keyAry)
            plainText.append(chr(scrambledInputAry[index]+ord('a')))
        outputStr = ''.join(plainText)
        return outputStr
  
    def SpeakWithRosie(self):
        print("You look up and notice an old woman sitting on a bench.")
        print("She appears to be reading something. You approach her.")
        print("Maybe she knows how to get out of here. You kindly introduce yourself")
        print("and she responds, saying her name is Rosie... Oh no... ")
        print("You pull a snack out of your bag and give it to her.")
        print("What snack do you give her? (Enter it into the Terminal)")

        userInput = input()
        print()
        print("Rosie accepts, and says:")
        print()
        print(self.VigenereDecryptor(userInput, "twpyo qoj. nzy euhi sene gtlh gug hesjy pco wwec bj rgtt."))
        print(self.VigenereDecryptor(userInput, "mn ucmwnsh lrv i vde wlurz tr zegt jisrh prs."))
        print(self.VigenereDecryptor(userInput, "twpe asttgdpadt hesjy lpd sfe pieiepi dy jagjgtry oji sso td tdgspt."))
        print(self.VigenereDecryptor(userInput, "wt issmgwi elst lgtxanv dfv gwc qzsc wph elw ktn. myl twpe assc'i byatt xe."))
        print(self.VigenereDecryptor(userInput, "oct mc gnt bj jjitcow warw qmyugto smt wdh xg ehrltw, bji t rwvtg xefavto."))
        print(self.VigenereDecryptor(userInput, "twtj xjits es zeae xi xivjci at dje, fmt iwp pabgpcmsnh pci sllpjw oairsmfg."))
        print(self.VigenereDecryptor(userInput, "aaa elwy rdfpv dd llw depkp qw twxd gdut: 'utvkt 8/11iwd sx twt vsfabx nsve'."))
        print(self.VigenereDecryptor(userInput, "acs t hgn'i zyso iu xe'w zeaeqyd, bji peuh ixxi gnt dq xzeb tdgspts t xzojvsx a spl elwm ealcanv ltxz sdbp patiap xgy."))

    def InvestigateTheShelves(self):
        print("You wander around the shelves to try to get an idea of the layout")
        print("that you're stuck in. You make a mental map. You noticed that")
        print("someone drew a couple symbols on the shelves in random locations.")
        print("You note the location of those symbols in your mental map.")

        # self.line(); self.dash(61); self.line(); print() 
        # # L1 D61 L1
        # self.line();self.space(1);print(chr(79),end="");self.space(17);self.line();self.space(41);self.line(); print()
        # # L1 S1 C79 S17 L1 S41 L1
        # self.line();self.dash(15);self.line();self.space(3);self.line();self.space(3);self.line();self.dash(33);self.line();self.space(3);self.line(); print()
        # # L1 D15 L1 S3 L1 S3 L1 D33 L1 S3 L1
        # self.line();self.space(28);self.line();self.space(7);self.line();self.space(9);self.line();self.space(10);self.line(); self.space(3);self.line(); print()
        # # L1 S28 L1 S7 L1 S9 L1 S10 L1 S3 L1
        # self.line();self.space(3);self.line();self.dash(24);self.line();self.space(3);self.line();self.dash(9);self.line();self.space(3);self.line();self.space(3);self.line();self.dash(2);self.line();self.space(3);self.line();self.space(3);self.line(); print()
        # # L1 S3 L1 D24 L1 S3 L1 D9 L1 S3 L1 S3 L1 D2 L1 S3 L1 S3 L1
        # self.line();self.space(17);self.line();self.space(24);self.line();self.space(3);self.line();self.space(6);self.line();self.space(3);self.line();self.space(3);self.line(); print()
        # # L1 S17 L1 S24 L1 S3 L1 S6 L1 S3 L1 S3 L1
        # self.line();self.dash(9);self.line();self.space(3);self.line();self.space(3);self.line();self.space(3);self.line();self.dash(16);self.line();self.space(3);self.line();self.space(3);self.line();self.dash(6);self.line();self.space(3);self.line();self.space(3);self.line(); print()
        # # L1 D9 L1 S3 L1 S3 L1 S3 L1 D16 L1 S3 L1 S3 L1 D6 L1 S3 L1 S3 L1
        # self.line();self.space(13);self.line();self.space(3);self.line();self.space(3);self.line();self.space(35);self.line();self.space(3);self.line(); print()
        # # L1 S13 L1 S3 L1 S3 L1 S35 L1 S3 L1
        # self.line();self.space(3);self.line();self.dash(9);self.line();self.space(3);self.line();self.space(3);self.line();self.space(3);self.line();self.dash(31);self.line();self.space(3);self.line(); print()
        # # L1 S3 L1 D9 L1 S3 L1 S3 L1 S3 L1 D31 L1 S3 L1
        # self.line();self.space(17);self.line();self.space(1);print(chr(88),end="");self.space(1);self.line();self.space(39);self.line(); print()
        # # L1 S17 L1 S1 C88 S1 L1 S39 L1 
        # self.line();self.dash(61);self.line(); print()
        # # L1 D61 L1
        self.mazeMaker("L1 D61 L1")
        self.mazeMaker("L1 S1 C79 S17 L1 S41 L1")
        self.mazeMaker("L1 D15 L1 S3 L1 S3 L1 D33 L1 S3 L1")
        self.mazeMaker("L1 S28 L1 S7 L1 S9 L1 S10 L1 S3 L1")
        self.mazeMaker("L1 S3 L1 D24 L1 S3 L1 D9 L1 S3 L1 S3 L1 D2 L1 S3 L1 S3 L1")
        self.mazeMaker("L1 S17 L1 S24 L1 S3 L1 S6 L1 S3 L1 S3 L1")
        self.mazeMaker("L1 D9 L1 S3 L1 S3 L1 S3 L1 D16 L1 S3 L1 S3 L1 D6 L1 S3 L1 S3 L1")
        self.mazeMaker("L1 S13 L1 S3 L1 S3 L1 S35 L1 S3 L1")
        self.mazeMaker("L1 S3 L1 D9 L1 S3 L1 S3 L1 S3 L1 D31 L1 S3 L1")
        self.mazeMaker("L1 S17 L1 S1 C88 S1 L1 S39 L1")
        self.mazeMaker("L1 D61 L1")

    def mazeMaker(self,lineInstructions):
        for word in lineInstructions.split():
            instruction = word[0]
            amount = int(word[1:])
            if instruction == 'C':
                print(chr(amount),end="")
            else:
                for i in range(amount):
                    match instruction:
                        case 'L':
                            myOut = chr(124)
                        case 'D':
                            myOut = chr(45)
                        case 'S':
                            myOut = chr(32)
                    print(myOut,end="")
        print()

    def AnnoyingLibrarians():
        print("A librarian walks past the end of the row of books that")
        print("you're in and says in passing: 'Have you figured out the")
        print("eight motions needed to solve that toy yet?'.")
        print("You chase after them to ask them what that means, but as")
        print("you get to the end of the row and look around, the librarian")
        print("is gone... These stupid librarians are no help. Worst library ever.")

    def ReadTheFlyer(self):
        print("You find a notice board where people can post flyers")
        print("for events and such. There's a single flyer on it.")
        print("It is a mostly blank piece of paper titled: ")
        print("This Month's Reading Club!")
        print("and has the following at the top:")
        print()
        print("1    18   6  this")
        print("8    18   8  is")
        print("124  29   6  an")
        print("172  29   3  example")
        print()
        print("followed by a space and then these numbers:")
        print()

        numAry = [ 2, 29, 4, 3, 23, 4, 16, 23, 6, 18, 17, 7, 45, 21, 13, 50, 21, 4, 75, 30, 1, 83, 26, 9 ]
        for tracker in range(0,len(numAry),3):
            print("{:>5} {:>5} {:>5}".format(*numAry[tracker:tracker+3]))

        print("On a small table beneath the posting board lie 4 books:")
        print("Sherlock Holmes, Moby Dick, The Odyssey, and the")
        print("transcript from The Princess Bride movie.")

    def InvestigateTheFlyerFurther(self):
        # Something urges you to investigate the flyer further.
        # You lift up the corner and notice a second flyer underneath.
        # This second flyer must be last month's flyer.
        # It says the same thing as the current flyer, except the numbers are different:
        numAry = [ 1, 18, 1, 3, 4, 3, 4, 13, 3, 5, 23, 6, 8, 23, 3, 8, 23, 4, 10, 2, 7, 336, 4, 3, 31, 3, 3, 47, 34, 7, 291, 19, 1, 128, 22, 10, 185, 24, 3, 336, 4, 3 ]
        for tracker in range(0,len(numAry),3):
            print("{:>5} {:>5} {:>5}".format(*numAry[tracker:tracker+3]))

    def PlayWithRubix(self):
        # You find a Rubix Rectangle sitting on a table. 
        # This is the 2D, rectangular, counterpart of a Rubix Cube.
        # Similar to a Rubix Cube, you can shift the rows 
        # and columns to rearrange the components in the square.
        # To operate it, enter 3 characters into the Serial
        # Monitor: 
        # 1) Whether you want to shift a row or a column,
        # indicated by an R or C, respectively.
        # 2) The index of the row/column, entered as a single
        # digit number.
        # 3) Which direction you want to shift, using U, D, L, R
        # to represent up, down, left, right, respectively.

        # So if you want to shift column 2 down you would
        # enter: "C2D"

        # If you are playing with the Rubix Rectangle and would
        # like to stop, simply type "exit".

        mainMatrix = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [1,'e','d','j','o','x','f','f','k'],
            [2,'i','b','n','s','o','r','v','v'],
            [3,'o','y','d','o','b','b','k','n'],
            [4,'o','b','k','o','x','w','z','i'],
            [5,'n','u','f','j','l','f','a','x']
        ]
        
        while True:
            print("Current Rubix Rectangle configuration:")
            for i in range(len(mainMatrix)):
                for j in range(len(mainMatrix[0])):
                    print(mainMatrix[i][j],end="\t")
                print()
            print("Please input your rubix command")
            userInput = input()
            if userInput == "exit":
                print("Thanks for playing!")
                break
            if (len(userInput)==3 and userInput[1].isdigit()
                and ((userInput[0].lower()=='c' and userInput[2].lower() in ('u','d') and 1<=int(userInput[1])<=8) 
                     or (userInput[0].lower()=='r' and userInput[2].lower() in ('l','r') and 1<=int(userInput[1])<=5))):
                print("Shifting the rubix rectangle!")
                self.ShiftMatrix(userInput,mainMatrix)
            else:
                print("Please Enter a valid command")

    def ShiftMatrix(self,userInput,currentMatrix):
        whichOne = int(userInput[1])
        numOfLoops = 5 if userInput[0].lower() == 'c' else 8
        negVal = 1 if userInput[2].lower() in ('u','l') else -1
        tempHolder = currentMatrix[negVal if numOfLoops == 5 else whichOne][whichOne if numOfLoops==5 else negVal] #################
        i = negVal
        while abs(i)<numOfLoops:
            currentMatrix[i if numOfLoops==5 else whichOne][whichOne if numOfLoops==5 else i] = currentMatrix[i+negVal if numOfLoops==5 else whichOne][whichOne if numOfLoops==5 else i+negVal]
            i+=negVal
        currentMatrix[negVal*numOfLoops if numOfLoops == 5 else whichOne][whichOne if numOfLoops == 5 else negVal*numOfLoops] = tempHolder ############

    def RestrictedSection(self):
        print("In a nook of the library you find a restricted section. The lock")
        print("on the gate is a directional lock. On the back of it is a brief")
        print("message that says: 'Remember: how do you get from O to X'")
        print()
        print("Enter the directional combination.")
        print("(Use w, a, s, d as up, left, down, right, respectively)")
        userInput = input()

        print(self.VigenereDecryptor(userInput, "lf wdh jeowniuwwg ohuterj ygx kha d kmwoh rwdvljj laxoa wawz wdh fuiear"))
        print(self.VigenereDecryptor(userInput, "hajdw zujgnev wzlnwwej skifw lknhw"))
        print(self.VigenereDecryptor(userInput, "fsurhv ijwk il dk lb eq a buwnllu saukoj zetz d bdcjwd lhj."))
        print(self.VigenereDecryptor(userInput, "qwap wg ip lj szdjseh as w vaeelfjhb sdzlpigqso jrle pkwt kdqv"))
        print(self.VigenereDecryptor(userInput, "'oaendjy ydnd'."))

        print("___________________________________________________________________________________")
        print("* If you got it wrong, remember to press twice on the lock to reset it!           *")
        print("* (This is a joke alluding to how all escape rooms tell people about pressing     *")
        print("* twice to reset directional locks haha. This is a virtual library after all,     *")
        print("* you can't actually 'press on it twice'. Just try again with a different combo.) *")
        print("___________________________________________________________________________________")


    # def ProgrammingSection(self):
        ##################################################################
        # The "Programming Section" of this library is old and unused.   #
        # It is covered in dust and is completely greyed out everywhere. #
        # If you would like to explore this section you must first       #
        # dust the place and get it back up and functioning. Remember,   #
        # do not change any of the code in this library, but you can     #
        # certainly ungrey things. The staff will be happy for your help #
        # keeping the place dust-free.                                   #
        ##################################################################
        
        # import NewLibrary
        # theWayOut = NewLibrary.MyOwnBook()
        # print("What is this? A book titled 'The Way Out'?")
        # print("But this book doesn't seem to be from this library...")
        # print("The book borrowing card at the front is from a different library.")

        # if theWayOut.enter() :
        #     print("You open to the middle of the book and are sucked into it.")
        #     key = theWayOut.exit()
        #     print(self.VigenereDecryptor(key, "bci jyyjfg ozc dus slrrcof oog qvrvysojsg zx gvjv zwsbnfz."))
        #     print(self.VigenereDecryptor(key, "bci lxpcwhfsu dus fqrsrfbft rt drcg kbqrsioeg."))
        #     print(self.VigenereDecryptor(key, "bci feggndfhvn gvf hjsi gnhdkwbx vvpsdfwrxf."))
        #     print(self.VigenereDecryptor(key, "bci uogsspwbvn gvbw hvvbr wt qc kri biu lb hysf zjefoii,"))
        #     print(self.VigenereDecryptor(key, "vc mfe pzfysfci pffdhsu ibis rkb csofbum."))
        #     print(self.VigenereDecryptor(key, "lb mfee zjefoii lcv dfs krr abvhsi, xbh kdgce."))
        #     print(self.VigenereDecryptor(key, "bci vxgss bcii vvpsdfm rxq qshohv ka sylh prmx hp wvs ionz xrfzu."))
        #     print(self.VigenereDecryptor(key, "bci ykis ork sjmndfg xojya'g mlpfrbl, hiucixr ywcuofp saqfshwfx."))
        #     print(self.VigenereDecryptor(key, "fcbxbnhvoohzyag!"))
        
