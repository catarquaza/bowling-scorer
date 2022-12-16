# requirements:
# score a bowling game
# a spare is when you get all the pins down in two throws
#   > in this case, the first throw of the next frame counts for the previous frame too
# a strike is when you get all pins down on first throw
#   > in this case, the next two throws count for this frame

total = 0
bonus = 0
prev_frame = ""
prev_prev_frame = ""
frame_score = 0

# frame_score.append(0)  # [0]
# frame_score.append(7)  # [0,7]
# frame_score[0] = 5  # [5,7]

# loop through each frame...
for x in range(12):
    # frame_score.append(0)
    frame = 0
    throw2 = 0
    last_bonus = bonus

    # get the throw scores
    throw = int(input("Enter your First score: "))
    if throw < 10:
        throw2 = int(input("Enter your Second score: "))
    frame = throw + throw2

    # add points to previous frames with spares or strikes
    if prev_frame == "strike" or prev_frame == "spare":
        total += throw
    if prev_frame == "strike":
        total += throw2
    if prev_prev_frame == "strike":
        total += throw

    # keep track of what happened two frames ago
    prev_prev_frame = prev_frame

    # store info of this frame so the next frame can use it
    if throw == 10:
        prev_frame = "strike"
    elif frame == 10:
        prev_frame = "spare"
    else:
        prev_frame = ""

    # print(frame_score)
    print("Frame: ", frame)
    if x <= 10:
        total += frame
    print("Total score: " + str(total))
    # frame_score = frame

    if x >= 10 and prev_frame == "" and prev_prev_frame == "":
        break

print("Final score " + str(total))

# throw
# throw:   1    2     3    4     5    6    7    8      9    10   11     12
# frame 1: 10   10   10
# frame 2:      10   10    10
# frame 3:           10    10    10
# frame 4:                 10    10   10
# frame 5:                       10   10   10
# frame 6:                            10   10   10
# frame 7:                                 10   10    10
# frame 8:                                      10    10    10
# frame 9:                                            10    10    10
# frame 10:                                                 10    10    10


# when you make a throw:
# - if the previous frame was a strike or a spare, double the throw
# - if the previous-previous frame was a strike, double the throw
