from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from colorama import Fore, Back, Style
import os
import sys
import webbrowser
import pathlib

# 8.5 inch by 11 inch
# ^ width     ^ height

# Detect if i'm an .exe or a .py
# Thanks to https://pyinstaller.org/en/stable/runtime-information.html
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    developmental = False
else:
    developmental = True

# Thanks to ArmindoFlores's answer on Stack Overflow https://stackoverflow.com/questions/51264169/pyinstaller-add-folder-with-images-in-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Inches:
    def __init__(self):
        self.quarter_inch = 0.25 * inch
        self.half_inch = 0.5 * inch
        self.three_quarter_inch = 0.75 * inch
        self.one_inch = 1 * inch
        self.one_and_quarter_inch = 1.25 * inch
        self.one_and_half_inch = 1.5 * inch
        self.one_and_three_quarters_inch = 1.75 * inch
        self.two_inch = 2 * inch

    def inch(amount):
        return amount * inch
    
Inch = Inches()

class Card:
    def __init__(self, x, y, width, height, radius, num):
        self.x = x * inch
        self.y = y * inch
        self.width = width * inch
        self.height = height * inch
        self.radius = radius
        self.num = num

        self.vegetarian = ["Vegetarian", False]
        self.vegan = ["Vegan", False]
        self.gluten_free = ["Gluten Free", False]
        self.nut_free = ["Nut Free", False]
        self.dairy_free = ["Dairy Free", False]

    def draw_self(self):
        canvas.roundRect(self.x, self.y, self.width, self.height, radius=self.radius)

    def draw_name(self, name, description):
        '''Names longer than 50 characters will be cut off. Names longer than 25 characters will move to a second line.'''

        canvas.setFontSize(0.25 * inch)
        if len(name) > 25:
            if name[24] != " ":
                first_line = name[0:24] + "-"
                second_line = name[24:]

            else:
                first_line = name[0:24]
                second_line = name[24:]

            if len(second_line) > 25:
                second_line = second_line[:23]
                second_line = second_line + "..."

            canvas.drawString(self.x + Inch.quarter_inch, self.y + (inch * 1.6), first_line)
            canvas.drawString(self.x + Inch.quarter_inch, self.y + (inch * 1.35), second_line)



        else:
            first_line = name

            canvas.drawString(self.x + Inch.quarter_inch, self.y + Inch.one_and_half_inch, first_line)

        print(description)
        canvas.setFontSize(0.15 * inch)
        canvas.drawString(self.x + Inch.half_inch, self.y + (inch * 1.15), description)

    def draw_food_stats(self):
        canvas.setFontSize(0.17 * inch)
          
        stats = [self.vegetarian, self.vegan, self.gluten_free, self.nut_free, self.dairy_free]

        true_stats = []
        for stat in stats:
            if stat[1] != "n":
                true_stats.append(stat)


        line_iter = 0
        icon_iter = 0
        for stat in true_stats:
            if developmental == True:
                image_name = stat[0].lower()
                image_name = image_name.replace(" ", "_")
                image_name = "./icons/" + image_name + ".png"

            elif developmental == False:
                image_name = stat[0].lower()
                image_name = image_name.replace(" ", "_")
                image_name = image_name + ".png"
                image_name = resource_path(image_name)


            
            if stat[1] == True:
  
                icon_iter += 1
                canvas.drawInlineImage(image_name, self.x + (icon_iter * (inch * 0.37)), self.y + (inch * 0.1), width=(inch * 0.35), height=(inch * 0.35))


            else:
                line_iter += 1
                canvas.drawString(self.x + Inch.half_inch, self.y + (inch * 1.15) - line_iter * (inch * 0.19), stat[1])
                canvas.drawInlineImage(image_name, self.x + Inch.quarter_inch, self.y + (inch * 1.09) - line_iter * (inch * 0.19), width=16, height=16)
                
                


            

        
        
        


canvas = Canvas("./labels.pdf")

card7 = Card(0.25, 1, 3.5, 2, 7, 7)
card8 = Card(4.25, 1, 3.5, 2, 7, 8)

card5 = Card(0.25, 3.25, 3.5, 2, 7, 5)
card6 = Card(4.25, 3.25, 3.5, 2, 7, 6)

card3 = Card(0.25, 5.5, 3.5, 2, 7, 3)
card4 = Card(4.25, 5.5, 3.5, 2, 7, 4)

card1 = Card(0.25, 7.75, 3.5, 2, 7, 1)
card2 = Card(4.25, 7.75, 3.5, 2, 7, 2)

cards = [card1, card2, card3, card4, card5, card6, card7, card8]


# card1.draw_name("A really friendly option!")
# card1.draw_self()
# card1.vegetarian = ["Vegetarian", True]
# card1.vegan = ["Vegan", True]
# card1.gluten_free = ["Gluten Free", True]
# card1.nut_free = ["Nut Free", True]
# card1.dairy_free = ["Dairy Free", True]
# card1.draw_food_stats()



canvas.setFontSize(0.2 * inch)
canvas.drawString(0.6 * inch, 10.2 * inch, "Page 1")

canvas.setFontSize(0.12 * inch)
canvas.drawString(0.6 * inch, 10 * inch, "https://github.com/nfoert/labelgenerator")



print(Fore.YELLOW + "----------")
print(Fore.RED + "nfoert's Label Generator")
print(Fore.YELLOW + "----------")
print(Fore.GREEN + "Welcome! 👋")

event_name = input(Fore.CYAN + "What is the event name? " + Fore.WHITE)

canvas.setFontSize(0.4 * inch)
canvas.drawString(0.5 * inch, 10.5 * inch, event_name)

event_name = event_name.lower()
event_name = event_name.replace(" ", "_")
event_name = event_name.replace("?", "_")
event_name = event_name.replace("/", "_")
event_name = event_name.replace("\\", "_")
event_name = event_name.replace(":", "_")
event_name = event_name.replace("*", "_")
event_name = event_name.replace("<", "_")
event_name = event_name.replace(">", "_")
event_name = event_name.replace('"', "_")
event_name = event_name.replace("|", "_")
try:
    os.mkdir(event_name)
    print(Fore.GREEN + "✅ Ok. A folder has been created.")
    working_card = card1

except FileExistsError:
    print(Fore.GREEN + "📁 Oh! That event already exists.")
    working_card = card1

except FileNotFoundError:
    print("\n")
    print(Fore.RED + "⚠ There was a problem making your folder. " + Fore.YELLOW + "We'll continue anyway.")
    print("\n")
    working_card = card1

while True:
    try:
        print(Back.BLUE + Fore.MAGENTA + f" 📃 Currently working on card {working_card.num}. " + Fore.RESET + Back.RESET)
        food_name = input(Fore.CYAN + "🍴 What is the name of the item? " + Fore.WHITE)
        while True:
            food_description = input(Fore.CYAN + "📔 What is the description for the item? (Leave blank if none) " + Fore.WHITE)
            if len(food_description) <= 32:
                break

            else:
                print("\n")
                print(Fore.RED + "⚠ Description is too long.")
                print("\n")

        working_card.draw_self()
        working_card.draw_name(food_name, food_description)
        print(Fore.YELLOW + "----------")
        print("Now you're going to enter the allergens, ect. for the item.")
        input(Fore.CYAN + "Press enter to continue...")

        vegetarian = input(Fore.CYAN +  "🥕 Is the item vegetarian?  [y/n] " + Fore.WHITE)
        vegan = input(Fore.CYAN +       "🥬 Is the item vegan?       [y/n] " + Fore.WHITE)
        gluten_free = input(Fore.CYAN + "🥐 Is the item gluten free? [y/n] " + Fore.WHITE)
        nut_free = input(Fore.CYAN +    "🥜 Is the item nut free?    [y/n] " + Fore.WHITE)
        dairy_free = input(Fore.CYAN +  "🥛 Is the item diary free?  [y/n] " + Fore.WHITE)

        if vegetarian == "y": vegetarian = True
        elif vegetarian == "n": vegetarian = "n"
        else: vegetarian = vegetarian

        if vegan == "y": vegan = True
        elif vegan == "n": vegan = "n"
        else: vegan = vegan

        if gluten_free == "y": gluten_free = True
        elif gluten_free == "n": gluten_free = "n"
        else: gluten_free = gluten_free

        if nut_free == "y": nut_free = True
        elif nut_free == "n": nut_free = "n"
        else: nut_free = nut_free

        if dairy_free == "y": dairy_free = True
        elif dairy_free == "n": dairy_free = "n"
        else: dairy_free = dairy_free

        working_card.vegetarian = ["Vegetarian", vegetarian]
        working_card.vegan = ["Vegan", vegan]
        working_card.gluten_free = ["Gluten Free", gluten_free]
        working_card.nut_free = ["Nut Free", nut_free]
        working_card.dairy_free = ["Dairy Free", dairy_free]

        working_card.draw_food_stats()
        print(Fore.YELLOW + "----------")

        if working_card.num == 1: working_card = card2
        elif working_card.num == 2: working_card = card3
        elif working_card.num == 3: working_card = card4
        elif working_card.num == 4: working_card = card5
        elif working_card.num == 5: working_card = card6
        elif working_card.num == 6: working_card = card7
        elif working_card.num == 7: working_card = card8
        elif working_card.num == 8: break

        print(Fore.YELLOW + f"You're finished with card {working_card.num - 1}.")
        quit_question = input(Fore.GREEN + "Would you like to quit and export your PDF? [y/n] ")
        if quit_question == "y":
            print(Fore.GREEN + "Goodbye! 👋" + Fore.RESET)
            input(Fore.CYAN + "Press enter to continue...")
            break

    except KeyboardInterrupt:
        break

canvas.save()

if developmental == False:
    print(Fore.GREEN + "You're finished with all 8 cards." + Fore.RESET)
    input(Fore.CYAN + "Press enter to continue...")
    webbrowser.open("labels.pdf")

