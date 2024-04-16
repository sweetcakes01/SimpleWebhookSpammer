"""
Credits: Webhook spammer made by Sai
Discord: flyingcakes01
Github: flyingcakes01
"""
print("""
                                                                                                 
  __      __   _    _             _       ___                                
 \ \    / /__| |__| |_  ___  ___| |___   \ __|_ __  __ _ _ __  _ __  ___ _ _ 
  \ \/\/ / -_) '_ \ ' \/ _ \/ _ \ / /    \__ \ '_ \/ _` | '  \| '  \/ -_) '_|
   \_/\_/\___|_.__/_||_\___/\___/_\_\   |___/ .__/\__,_|_|_|_|_|_|_\___|_|  
                                            |_|                             
                                    Made by Sai
                                  Github: flyingcakes01
""")

#imports
from dhooks import Webhook
import time

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("Enter a delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Sent. Sub to Flyingcakes01")