"""
Course: Introduction to Python Programming
Student Name: Daniel Diaz
"""
#%% 
from random import randint
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# %%
def HumanPlayer(GameRecord):
    
    print('====================Welcome!====================')
    choices = ['Rock','rock','r','R','Paper','paper','p','P','Scissors','scissors','s','S','Game','game','g','G','Quit','quit','q','Q']

    while True:
        choice = input('What would you like to do? (R)ock, (P)aper, (S)cissors, See the (G)ame Record, or (Q)uit?\n')
        if(choice not in choices):
            print('Not a valid choice')

        else:
            return choice
    

    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
    '''

# %%
def ComputerPlayer(GameRecord):

    comp = ['Rock','Paper','Scissors']
    x = randint(0,2)

    return comp[x]
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''

# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):

    outcome = 0

    Rock = ['Rock','rock','r','R']
    Paper = ['Paper','paper','p','P']
    Scissors = ['Scissors','scissors','s','S']

    if(((ChoiceOfHumanPlayer in Rock) and (ChoiceOfComputerPlayer in Scissors)) 
        or ((ChoiceOfHumanPlayer in Paper) and (ChoiceOfComputerPlayer in Rock)) 
        or ((ChoiceOfHumanPlayer in Scissors) and (ChoiceOfComputerPlayer in Paper))):
        outcome = 2
        return outcome 

    elif(((ChoiceOfHumanPlayer in Rock) and (ChoiceOfComputerPlayer in Paper)) 
        or ((ChoiceOfHumanPlayer in Paper) and (ChoiceOfComputerPlayer in Scissors)) 
        or ((ChoiceOfHumanPlayer in Scissors) and (ChoiceOfComputerPlayer in Rock)) ):
        outcome = 1
        return outcome

    else:
       return outcome

    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''

# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):

    if(Outcome == 0):
        Outcome = 'Nobody'

    elif(Outcome == 1):
        Outcome = 'Computer'

    elif(Outcome == 2):
        Outcome = 'You'
    
    print('===================AND-THE-WINNER-IS..........===================')
    print(Outcome)
    print('Computer: '+ChoiceOfComputerPlayer)
    print('Human: '+ChoiceOfHumanPlayer)
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''

# %%
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    
    GameRecord[0].append(ChoiceOfComputerPlayer)
    GameRecord[1].append(ChoiceOfHumanPlayer)
    GameRecord[2].append(Outcome)


    '''
    Parameters: 
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    Return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
# %%
def PrintGameRecord(GameRecord):
    Cwins = 0
    Pwins = 0
    Rounds = len(GameRecord[2])

    if(Rounds == 0):
        print('The Game has not even started! What are you hoping to find here?')
        return 0

    for i in GameRecord[2]:
        if(i == 1):
            Cwins += 1
        if(i == 2):
            Pwins += 1

    print('====================History====================')
    print('Total Number of Rounds '+str(Rounds))
    print('Computer Choices were')
    print(', '.join(GameRecord[0]))
    print('Player Choices were')
    print(', '.join(GameRecord[1]))
    print('Computer has won '+str(Cwins)+' time(s)')
    print('Player has won '+str(Pwins)+' time(s)')
    if(Cwins > Pwins):
        print('Wow! I am wrecking you sooooooooooooooooo hard right now.')
    elif(Cwins == Pwins):
        print('Aha! Finally, a worthy opponent!')
    else:
        print('This is a game of chance, it does not reflect skill at all')
        

    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    Return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
# %% the game
def PlayGame():
    GameRecord = [[],[],[],]
    Quit = ['Quit','quit','q']
    Game = ['Game','game','g']
    while True:

        Human = HumanPlayer(GameRecord)
        Computer = ComputerPlayer(GameRecord)
        Result = Judge(Computer,Human)
        if(Human in Quit):
            print('Have a good day')
            break
        elif(Human in Game):
            PrintGameRecord(GameRecord)
        else:
            PrintOutcome(Result,Computer,Human)
            UpdateGameRecord(GameRecord,Computer,Human,Result)
    
    
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''


# %% do not modify anything below
if __name__ == '__main__':
    PlayGame()
