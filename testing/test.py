import cmdstyler as cs
import time

# 1️⃣ Print the game title as a large ASCII header
cs.header("SKIBIDI.exe")
time.sleep(0.5)

# 2️⃣ Add some spacing
cs.empty(1)

# 3️⃣ Welcome message in colored text
cs.color(45, "Welcome to skibidi, the skibidi toilet!")
time.sleep(0.5)

# 4️⃣ A dramatic background-colored alert
cs.background(160, "Danger: A toiler man is approaching!")
time.sleep(0.5)

# 5️⃣ Show a dual-color effect (foreground + background)
cs.bothcolors(161, 19, "Prepare your settlers for the toilets.")
time.sleep(0.5)

# 6️⃣ Introduce game mechanics with RGB colored text
cs.rgbcolor("#FFD700", "Manage resources, build shelters, and survive the brainrot!")
time.sleep(0.5)

# 7️⃣ Create extra spacing before user input
cs.empty(2)

# 8️⃣ Simple instructions with foreground color
cs.color(14, "Press [Enter] to start your adventure...")
input()
