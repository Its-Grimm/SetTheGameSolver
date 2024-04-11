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


rows, cols = (3, 4)
board = [[0] * cols for _ in range(rows)]
# For printing each line(row)
# for row in board:
#     print(row)

# For printing each element(col) in each row, with a space in between
# for row in board:
#     for col in row:
#         print(col, end=' ')
#     print()

# Getting the card number and only the card number 
# card1Box = driver.find_element(By.NAME, "card" + str(1))
# cardNum = card1Box.get_attribute("src").removeprefix("https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/").removesuffix(".png")
# print("Card Number:", cardNum)

# Gets the card numbers into the 2dim array 
row, col = (0, 0)
for cardNum in range(0, 12):
    # Gets and stores the card number extracted from the https://webpath/image.png link  
    card1Box = driver.find_element(By.NAME, "card" + str(cardNum+1))
    card = card1Box.get_attribute("src").removeprefix("https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/").removesuffix(".png")
    # For proper adding to the 2dim array from one number
    if cardNum != 0 and cardNum % 4 == 0:
        row += 1
        col = 0
        # print()
    board[row][col] = dataTable(int(card))
    
    # print(dataTable(board[row][col]))
    col += 1
    
# Compare with the card data-table and assign each property (quantity, fill, colour, shape) a digit



# For printing each element(col) in each row, with a space in between
for row in board:
    for col in row:
        print(col, end=' ')
    print()


# Closes the browser window at the end of execution
driver.quit()