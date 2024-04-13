# Running this script should allow for complete automated solving of the set game, all viewable in the Selenium Firefox window, no manual card entry or anything
# Refer to ../cardNums.txt for which cards correlate to which number

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Opens the setgame website on firefox (may take a little bit to load)
print("~Opening Firefox~")
driver = webdriver.Firefox()
driver.get('https://www.setgame.com/set/puzzle')
time.sleep(0.5)


# Datatable for converting card number to its properties for comparison and finding sets
def dataTable(cardNum):
    # Class for card type
    # Quantity: 0 = 1         1 = 2           2 = 3
    # Shape:    0 = squigle   1 = diamond     2 = oval
    # Fill:     0 = solid     1 = lined       2 = empty
    # Colour:   0 = red       1 = purple      2 = green
    numbers = [0, 1, 2]
    fills   = [0, 1, 2]
    colours = [0, 1, 2]
    shapes  = [0, 1, 2]
    
    # For testing with word values 
    # numbers = ["1", "2", "3"]
    # shapes  = ["Squigles", "Diamonds", "Ovals"]
    # fills   = ["Solid", "Lined", "Empty"]
    # colours = ["Red", "Purple", "Green"]
    
    # Modulo by 3 (3 quantity possibilites for each card)
    numberIndex = (cardNum - 1) % 3
    # Divide by 27 (27 cards of each fill for each shape type)
    fillIndex = (cardNum - 1) // 27
    # Modulo by 9 (3 cards of each colour for each fill type), then divide by the three colour possibilities
    colourIndex = ((cardNum - 1) % 9) // 3 
    # Modulo by 27 (9 squigles + 9 diamonds + 9 ovals) to find its position, then divide by 9 out of the remaining fills 
    shapeIndex = ((cardNum - 1) % 27) // 9
    
    number = numbers[numberIndex]
    fill   = fills[fillIndex]
    colour = colours[colourIndex]
    shape  = shapes[shapeIndex]
    
    return number, fill, colour, shape


# For determining if three cards on the board are a set or not
def isSet(a, b, c):
    def propertySet(prop):
        return (a[prop] == b[prop] == c[prop]) or (a[prop] != b[prop] != c[prop] != a[prop])
    
    numberSet = propertySet(0)
    fillSet = propertySet(1)
    colourSet = propertySet(2)
    shapeSet = propertySet(3)

    return (numberSet and fillSet and colourSet and shapeSet)

# Creating the board
board = [0 for _ in range(12)]

# Gets the card numbers into the array
count = 0
for cardNum in range(0, 12):
    card1Box = driver.find_element(By.NAME, "card" + str(cardNum+1))
    card = card1Box.get_attribute("src").removeprefix("https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/").removesuffix(".png")
    board[count] = dataTable(int(card))
    count += 1

# Logic which finds sets from the array and loads them into a 2dim array for unique sets
sets = [[0 for _ in range(3)] for _ in range(6)]
setCounter = 0
for card1Check in range(0, 12):
    for card2Check in range(card1Check + 1, 12):
        for card3Check in range(card2Check + 1, 12):
            if isSet(board[card1Check], board[card2Check], board[card3Check]) and card1Check != card2Check and card2Check != card3Check and card3Check != card1Check:
                # Isolating unique sets (no 0 2 6, 2 0 6, 0 6 2, etc)
                setIndex = sorted([card1Check, card2Check, card3Check])
                setStr = str(board[setIndex[0]] + board[setIndex[1]] + board[setIndex[2]])
                if setStr not in sets:
                    # print("Set found: ", card1Check, card2Check, card3Check)
                    # sets.append(str(card1Check) + " " + str(card2Check) + " " +  str(card3Check))
                    sets[setCounter][0] = card1Check
                    sets[setCounter][1] = card2Check
                    sets[setCounter][2] = card3Check
                    setCounter += 1


# SOLVER (REPURPOSE LATER)
# For each card, add "card" + the num of the card to allow the code to click the right card for each set stored in a 2dim array
for set in sets:
    # card1Box = driver.find_element(By.NAME, "card" + str(set[0]))
    for card in set:
        print(card)
        card1Box = driver.find_element(By.NAME, "card" + str(card))
    
# for board in nums:
#     for card in board:
#         cardBox = driver.find_element(By.NAME, "card" + str(card))
#         print("~Clicking card " + str(card) + " now~")
#         cardBox.click()
#         time.sleep(0.75)
#     print()
#     time.sleep(0.5)
# print("~I win again!~")


# At the win screen, clear the box that says anonymous, and add BotBot instead
nameBox = driver.find_element(By.ID, "edit-submitted-user-id")
sendBox = driver.find_element(By.NAME, "op")
nameBox.clear()

print("~Typing BotBot~")
nameBox.send_keys("BotBot")
time.sleep(5)

print("~Clicking Submit~")
sendBox.click()
time.sleep(3)

print()

print("~ALL DONE!~")
print("~Closing Firefox~")