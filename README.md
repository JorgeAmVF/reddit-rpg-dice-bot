# Reddit RPG Dice Bot

A simple RPG dice bot for Reddit that uses [random](https://docs.python.org/3/library/random.html) in order to simulate the roll of each die in a 7-dice set.

## Installation

1. Clone the repository;
2. run the command prompt;
3. reach the folder and run `py bot.py`.

## Usage

To change the subreddit where it runs, edit:

    for comment in r.subreddit('RPG_Dice_Bot').comments(limit=1000):`

To change a die or to create new dice, edit:

    if "RollD20!" in comment.body and comment.permalink not in dice_rolled:
        comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,20)) + "**🎲")
        dice_rolled.append(comment.permalink)
        with open ("dice_rolled.txt", "a") as f:
            f.write(comment.permalink + "\n")
            
## Credits
A special thanks to [Yashar](https://github.com/yashar1)'s [Reddit Comment Bot code and README](https://github.com/yashar1/reddit-comment-bot) for the introductory lessons they provided in the past.
