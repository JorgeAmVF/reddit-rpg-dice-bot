# Reddit RPG Dice Bot

A simple RPG dice bot for Reddit.

## Installation

1. Clone the repository;
2. run the command prompt;
3. go to its folder and run `py bot.py`.

## Usage

To change the subreddit where it acts, edit:

    for comment in r.subreddit('RPG_Dice_Bot').comments(limit=1000):`

To change a die or to create a new dice, edit:

    if "RollD20!" in comment.body and comment.permalink not in dice_rolled:
        comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,20)) + "**🎲")
        dice_rolled.append(comment.permalink)
        with open ("dice_rolled.txt", "a") as f:
            f.write(comment.permalink + "\n")
            
