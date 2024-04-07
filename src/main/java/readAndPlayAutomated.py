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
time.sleep(3)


# Read in each card on the board into a 2dim array, making the board understandable to the code
# Creating and initializing the board for the values to get read into
rows, cols = (3, 4)
board = [[0]*cols for _ in range(rows)]

# Reading in the values from the website into the 2dim array
row, col = (0, 0)
for cardNum in range(0, 12):
    # Gets and stores the card number extracted from the https://webpath/image.png link  
    card1Box = driver.find_element(By.NAME, "card" + str(cardNum+1))
    card = card1Box.get_attribute("src").removeprefix("https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/").removesuffix(".png")
    # For proper adding to the 2dim array from one number
    if cardNum != 0 and cardNum % 4 == 0:
        row += 1
        col = 0
    board[row][col] = card
    col += 1


# SOLVER (REPURPOSE LATER)
# For each card, add "card" + the num of the card to allow the code to click the right card for each set stored in a 2dim array
for board in nums:
    for card in board:
        cardBox = driver.find_element(By.NAME, "card" + str(card))
        print("~Clicking card " + str(card) + " now~")
        cardBox.click()
        time.sleep(0.75)
    print()
    time.sleep(0.5)
print("~I win again!~")

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