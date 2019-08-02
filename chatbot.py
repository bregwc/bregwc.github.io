class personaity():
hiresponce = ""
whatsupresponce = ""
howareyouresponce = ""
otherresponce = ""

def processinput(self, responce):
if responce == "hi":
print(self.hiResponce)
elif responce == "whats up?":
print(self.whatsupresponcne)
elif responce == "how are you?":
print(self.howareyouresponce)
else:
print(self.otherresponce)

# --- Define your functions below! ---
def intro():
    print("hello, I am Chatbort")
    print("Let's Talk")
    print("[Instructions foe use]")

# r/p/s - 5
# different bort perssonalities

def choosepersonaity():
print("choose a personality to talk to. you can c hoose:")
choice = input("mean, nice, or nervous")
return choice

 # --- Put your main program below! ---
def main():
userchoice choosepersonality()
print(userchoice)

nicerobot = personality()
nicerobot.hiresponce = "hi, its so nice to meet you!"
nicerobot.whatsypresponce = "oh, im just talking to the most interseting"
nicerobot.howareyouresponce = " oh, im just lovely"
nicerobot.otherresponce = " terrbly sorry, but i dont understand!"

meanrobot = personality()
meanrobot.hiresponce = "can you leave??"
meanrobot.whatsupresponcne = "dont speak to me fool"
meanrobot.howareyouresponce ="terrible, now that i'm talking to you"
meanrobot.otherresponce = "i dont understand your gibberish, swite"

nervousrobot = personality()
nervousrobot.hiresponce = ""
nervousrobot.whatsupresponce = "...um, hi"
nervousrobot.howareyouresponce = "nervous!"
nervousrobot.otherresponce = "the world is large and confussing"


intro()

 intro()
while True:

  intro()
  while True:
    answer = input("(What will you say?) ")
    if (userchoice == "nice"):
    nicerobot.processinput(answer)
elif (userchoice == "mean"):
    meanrobot.proccesinput(answer)

    # DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
