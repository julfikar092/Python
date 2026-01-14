
questions = ["In what year did the Great October Socialist Revolution take place?\na.1917\nb.1923\nc.1914\nd.1920",
             "What is the largest lake in the world?\na.Caspian Sea\nb.Baikal\nc.Lake Superior\nd.Ontario",
             "Which planet in the solar system is known as the “Red Planet”?\na.Venus\nb.Earth\nc.Mars\nd.Jupiter",
             "Who wrote the novel “War and Peace?\na.Anton Chekhov\nb.Fyodor Dostoevsky\nc.Leo Tolstoy\nd.Ivan Turgenevyes",
             "What is the capital of Japan?\na.Beijing\nb.Tokyo\nc.Seoul\nd.Bangkok",
             "Which river is the longest in the world?\na.Amazon\nb.Mississippi\nc.Nile\nd.Yangtze",
             "What gas is used to extinguish fires?\na.Oxygen\nb.Nitrogen\nc.Carbon dioxide\nd.Hydrogen",
             "What animal is the national symbol of Australia?\na.Kangaroo\nb.Koala\nc.Emu\nd.Crocodile",
             "Which of the following planets is not a gas giant?\na.Mars\nb.Jupiter\nc.Saturn\nd.Uranus",
             "What is the name of the process by which plants convert sunlight into energy?\na.Respiration\nb.Photosynthesis\nc.Oxidation\nd.Evolution",
             "What chemical element is designated as “Hg”?\na.Silver\nb.Tin\nc.Copper\nd.Mercury",
             "In what year was the first international modern Olympiad held?\na.1896\nb.1900\nc.1912\nd.1924",
             "For which of these disciplines Nobel Prize is awarded?\na.Physics, Chemistry\nb.Physiology\nc.Medicine\nd.All of the above",
             "Entomology is the science that studies:\na.Behavior of human beings\nb.Insects\nc.The origin and history of technical and scientific terms\nd.The formation of rocks",
             "Hitler's party is known as:\na.Labour Party\nb.Nazi Party\nc.Ku-Klux-Klan\nd.Democratic Party",
             "For which Galileo is famous?\na.Developed the telescope\nb.Discovered four satellites of Jupiter\nc.Found that the swinging motion of the pendulum results in consistent time measurement.\nd.All of the above"]

answer = ["a","b","c","c","b","c","b","a","a","b","d","a","d","b","b","d"]
prizemoney = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]

earnedMoney= 0

def goToKBC():
    for i in range(0,15,1):
        print("Here is your ", i+1,"th question")
        print(questions[i])
        ans = input("My answer is: ")
        if ans == answer[i]:
            earnedMoney = prizemoney[i]
            print("Congratulations. You have earned total money: ", earnedMoney)
        else:
            if i==0:
                print("Sorry dear your question is wrong. Before going you have earned ", 0)
                break 
            else:
                print("Sorry dear your question is wrong. Before going you have earned ", prizemoney[i-1])
                break      
        if(i>4):
            print("Do you want to continue or quiet? If continue then \"y\" or no then \"n\"")
            thisOption = input("My option is: ")
            if (thisOption == "y"):
                continue
            else:
                print("Weldone! Before you leaving the platform you have earned ", earnedMoney)
        

print("Welcome to KBC!\nAre you ready?")
choice = input("If ready then type \"y\" or to hold type \"n\": ")

if (choice == "y"):
   goToKBC ()
        
else:
    option = input("Take your time, don't rush! when you ready just type \"y:\" ")
    if (option == "y"):
       goToKBC()

