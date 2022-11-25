# requirements:
# score a bowling game
# a spare is when you get all the pins down in two throws
#   > in this case, the first throw of the next frame counts for the previous frame too
# a strike is when you get all pins down on first throw
#   > in this case, the next two throws count for this frame

total = 0
bonus = 0

# loop through each frame...
for x in range(10):
    frame = 0
    throw2 = 0
    last_bonus = bonus

    # get the throw scores
    throw = int(input("Enter your First score: "))
    if throw < 10:
        throw2 = int(input("Enter your Second score: "))
    frame = throw + throw2

    # if the previous frame was a strike
    if bonus == 10:
        frame += throw + throw2
    if bonus == 20:
        frame += 10
    bonus += throw

    print(frame)
    total += frame
    print("Total score: " + str(total))
    if throw < 10:
        bonus = 0
    print("Bonus: " + str(bonus))

print("Final score " + str(total))

# throw
# throw:   1    2     3    4
# frame 1: 10   10   10                             total 30
# frame 2:      10   10
# frame 3:           10    10   10
# frame 4:                 10
