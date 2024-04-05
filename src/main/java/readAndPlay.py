#Tyler Patenaude (300338859)
#Uses Python 3.10.6 to read the setdata file, and then solves the set board on the actual website for you
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Reading file taken from: https://www.w3schools.com/python/python_file_open.asp
#Open the Set results data file (expFile.txt) using fileReader to control the file 
fileReader = open('expFile.txt', 'r')

#Stores the files text into the fileText variable
fileText = fileReader.read()
fileReader.close()

#Creates and splits strings until it gets down to just the extracted nums
nums = []
lines = fileText.split('\n')

#For all the text in the fileText all on one line for easy splitting
for line in lines:
    if line:
        #If line exists, then split up the parts into the sections after the triple bar
        parts = line.split("|||")
        if len(parts) >=2:
            numbers = parts[-1].strip()
            #Split apart again at "AT" and strip any white spaces left behind to finally get to the numbers
            numStr = numbers.split("AT")[1].strip()
            #The numbers are finally split from eachother and the colons, and then added to nums to make a 2dim array of each set. Easier for working with the website
            getNums = [int(num) for num in numStr.split(":")]
            nums.append(getNums)
print(nums)

#Controlling web from:   https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
#Understanding Selenuim: https://selenium-python.readthedocs.io/ 

#Opens the setgame website on firefox (may take a little bit to load)
print("~Opening Firefox~")
driver = webdriver.Firefox()
driver.get('https://www.setgame.com/set/puzzle')
time.sleep(3)

#For each card, add "card" + the num of the card to allow the code to click the right card for each set stored in a 2dim array
for board in nums:
    for card in board:
        cardBox = driver.find_element(By.NAME, "card" + str(card))
        print("~Clicking card " + str(card) + " now~")
        cardBox.click()
        time.sleep(0.75)
    print()
    time.sleep(0.5)
print("~I win again!~")

#At the win screen, clear the box that says anonymous, and add BotBot instead
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