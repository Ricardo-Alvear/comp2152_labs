import random

choices = ["Rock", "Paper", "Scissors"]
playerWins = 0
playerLosses = 0
drawScore = 0
computerWins = 0
computerLosses = 0

for i in range(10):
    try:
        playerChoice = int(input("Choose a number between the follow list: 1-Rock, 2-Paper, 3-Scissors: "))
        computerChoice = random.randint(1, 3)

        if playerChoice < 1 or playerChoice > 3:
            print("Error, please choose between 1-Rock, 2-Paper, 3-Scissors")
            continue

        if playerChoice == computerChoice:
            drawScore += 1
            print("Draw | Total draws are", drawScore, "and the computer has", computerWins, "wins and", computerLosses,
                  "losses while you have", playerWins, "wins and", playerLosses, "losses")
        elif playerChoice == 1 and computerChoice == 3:
            playerWins += 1
            computerLosses += 1
            print("Rock beats Scissors - You win! The computer has", computerWins, "wins and", computerLosses,
                  "losses while you have", playerWins, "wins and", playerLosses, "losses")
        elif playerChoice == 2 and computerChoice == 1:
            playerWins += 1
            computerLosses += 1
            print("Paper beats Rock - You win! The computer has", computerWins, "wins and", computerLosses,
                  "losses while you have", playerWins, "wins and", playerLosses, "losses")
        elif playerChoice == 3 and computerChoice == 2:
            playerWins += 1
            computerLosses += 1
            print("Scissors beats Paper - You win! The computer has", computerWins, "wins and", computerLosses,
                  "losses while you have", playerWins, "wins and", playerLosses, "losses")
        else:
            playerLosses += 1
            computerWins += 1
            print("You lose!, the computer wins! The computer has", computerWins, "wins and", computerLosses,
                  "losses while you have", playerWins, "wins and", playerLosses, "losses")

    except ValueError:
        print("Invalid input! Please enter a number.")