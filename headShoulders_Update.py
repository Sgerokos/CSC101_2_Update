# Function that prints the "head shoulders" lines
def head_shoulders():
    print("Head, shoulders, knees and"
          "\ntoes, knees and toes")

# Function that prints the "eyes ears" lines
def eyes_ears():
    print("And eyes and ears and"
          "\nmouth and nose.")

# Function that prints the "march march" lines
def march_march():
    print("March, march, march."
          "\nLet us all march."
          "\nMarch, march, march."
          "\nGet your body charge!")

# Function that prints the "jump jump" lines
def jump_jump():
    print("Jump, jump, jump."
          "\nLet's all jump."
          "\nJump, jump, jump.")

# Function that prints the "muscles" line
def muscles():
    print("Make your muscle pump!")

# Function that prints the "punch punch" lines
def punch_punch():
    print("Punch, punch, punch."
          "\nLet's all punch."
          "\nPunch, punch, punch.")

# Function that prints the "hurty munch" line
def hurty_munch():
    print("Have a hurty munch.")

# Main program
def main():
    for _ in range(2):
        head_shoulders()

    eyes_ears()
    head_shoulders()
    march_march()
    head_shoulders()
    eyes_ears()
    jump_jump()
    muscles()
    head_shoulders()
    eyes_ears()
    head_shoulders()
    punch_punch()
    hurty_munch()

# Call the main program
main()