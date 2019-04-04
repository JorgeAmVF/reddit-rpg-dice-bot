# -*- coding: utf-8 -*- 
import praw
import config
import time
import os
import random

def bot_login():
    print ("Logging in...")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "reddit:r/RPG_Dice_Bot:vAlpha (by u/RPG_Dice_Bot)")
    print ("Logged!")

    return r

def run_bot(r, dice_rolled):
    print ("Searching last 1000 comments looking for players rolling dice...")

    for comment in r.subreddit('RPG_Dice_Bot').comments(limit=1000):
        if "RollD20!" in comment.body and comment.permalink not in dice_rolled:
            
            print ("Rolled dice found in the following comment: " + comment.permalink + ".")
                        
            print ("The die is cast, " + comment.author.name + "!")
       
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,20)) + "**🎲")
                        
            print ("Die face successfully read!")
            
            dice_rolled.append(comment.permalink)
            
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
                print ("The comment permalink has been archived to avoid duplicates in the future.")
    
        if "RollD12!" in comment.body and comment.permalink not in dice_rolled:
            
            print ("Rolled dice found in the following comment: " + comment.permalink + ".")
                        
            print ("The die is cast, " + comment.author.name + "!")
       
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,12)) + "**🎲")
                        
            print ("Die face successfully read!")
            
            dice_rolled.append(comment.permalink)
            
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
                print ("The comment permalink has been archived to avoid duplicates in the future.")

        if "RollD%!" in comment.body and comment.permalink not in dice_rolled:
            
            print ("Rolled dice found in the following comment: " + comment.permalink + ".")
                        
            print ("The die is cast, " + comment.author.name + "!")
       
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,100)) + "**🎲")
                        
            print ("Die face successfully read!")
            
            dice_rolled.append(comment.permalink)
            
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
                print ("The comment permalink has been archived to avoid duplicates in the future.")

        if "RollD10!" in comment.body and comment.permalink not in dice_rolled:
            
            print ("Rolled dice found in the following comment: " + comment.permalink + ".")
                        
            print ("The die is cast, " + comment.author.name + "!")
       
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(0,9)) + "**🎲")
                        
            print ("Die face successfully read!")
            
            dice_rolled.append(comment.permalink)
            
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
                print ("The comment permalink has been archived to avoid duplicates in the future.")
                
        if "RollD8!" in comment.body and comment.permalink not in dice_rolled:
            
            print ("Rolled dice found in the following comment: " + comment.permalink + ".")
                        
            print ("The die is cast, " + comment.author.name + "!")
       
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,8)) + "**🎲")
                        
            print ("Die face successfully read!")
            
            dice_rolled.append(comment.permalink)
            
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
                print ("The comment permalink has been archived to avoid duplicates in the future.")                    

        if "RollD6!" in comment.body and comment.permalink not in dice_rolled:
            
            print ("Rolled dice found in the following comment: " + comment.permalink + ".")
                        
            print ("The die is cast, " + comment.author.name + "!")
       
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,6)) + "**🎲")
                        
            print ("Die face successfully read!")
            
            dice_rolled.append(comment.permalink)
            
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
                print ("The comment permalink has been archived to avoid duplicates in the future.")                 

        if "RollD4!" in comment.body and comment.permalink not in dice_rolled:
            
            print ("Rolled dice found in the following comment: " + comment.permalink + ".")
                        
            print ("The die is cast, " + comment.author.name + "!")
       
            comment.reply("*ALEA IACTA EST*: " + "🎲**" + str(random.randint(1,4)) + "**🎲")
                        
            print ("Die face successfully read!")
            
            dice_rolled.append(comment.permalink)
            
            with open ("dice_rolled.txt", "a") as f:
                f.write(comment.permalink + "\n")
                print ("The comment permalink has been archived to avoid duplicates in the future.")                 
                
                
    print (dice_rolled)

    print ("Task done!")
    
    print ("Awaiting 10 seconds to restart...")
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

r = bot_login()
dice_rolled = get_saved_comments()
print (dice_rolled)

while True:
    run_bot(r, dice_rolled)
