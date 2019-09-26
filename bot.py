# -*- coding: utf-8 -*- 
import praw
import config
import time
import os
import random


def __init__():
    r = praw.Reddit('bot')
    return r


def run_bot(r, dice_rolled):
    for comment in r.subreddit('RPG_Dice_Bot').comments(limit=1000):
        if "RollD20!" in comment.body and comment.permalink not in dice_rolled:
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,20)) + "**🎲")
            dice_rolled.append(comment.permalink)
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
        if "RollD12!" in comment.body and comment.permalink not in dice_rolled:
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,12)) + "**🎲")
            dice_rolled.append(comment.permalink)
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
        if "RollD%!" in comment.body and comment.permalink not in dice_rolled:
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,100)) + "**🎲")
            dice_rolled.append(comment.permalink)
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
        if "RollD10!" in comment.body and comment.permalink not in dice_rolled:
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(0,9)) + "**🎲")
            dice_rolled.append(comment.permalink)
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
        if "RollD8!" in comment.body and comment.permalink not in dice_rolled:
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,8)) + "**🎲")
            dice_rolled.append(comment.permalink)
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
        if "RollD6!" in comment.body and comment.permalink not in dice_rolled:
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,6)) + "**🎲")
            dice_rolled.append(comment.permalink)
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
        if "RollD4!" in comment.body and comment.permalink not in dice_rolled:
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,4)) + "**🎲")
            dice_rolled.append(comment.permalink)
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
    time.sleep(10)

    
def get_saved_comments():
    if not os.path.isfile("dice_rolled.txt"):
        dice_rolled = []
    else:
        with open("dice_rolled.txt", "r") as f:
            dice_rolled = f.read()
            dice_rolled = dice_rolled.split("\n")
            dice_rolled = list(filter(None, dice_rolled))
    return dice_rolled


r = __init__()
dice_rolled = get_saved_comments()
while True:
    run_bot(r, dice_rolled)
