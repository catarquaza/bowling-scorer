# requirements:
# score a bowling game
# a spare is when you get all the pins down in two throws
#   > in this case, the first throw of the next frame counts for the previous frame too
# a strike is when you get all pins down on first throw
#   > in this case, the next two throws count for this frame

prev_throw = ""
prev_prev_throw = ""
frame_score = [0] * 10
current_frame = 0
throw_num = 1

while True:
    # throw ball
    throw = int(input("Enter your score: "))
    if current_frame < 10:
        # add points to frame
        frame_score[current_frame] += throw

    # add points to previous frames with spares / strikes
    if prev_throw == "strike" or prev_throw == "spare":
        frame_score[current_frame - 1] += throw
    if prev_prev_throw == "strike":
        frame_score[current_frame - 2] += throw

    # track if the previous frame and prev_prev_frame are spares / strikes
    if current_frame < 10:
        prev_prev_throw = prev_throw
    if current_frame == 10 and prev_prev_throw == "":
        prev_throw = ""

    if current_frame < 10:
        if frame_score[current_frame] == 10 and throw_num == 1:
            prev_throw = "strike"
        elif frame_score[current_frame] == 10 and throw_num == 2:
            prev_throw = "spare"
        else:
            prev_throw = ""
        # increment frame
        if frame_score[current_frame] == 10 or throw_num == 2:
            throw_num = 1
            current_frame += 1
        else:
            throw_num += 1
    else:
        prev_prev_throw = ""

    print(frame_score)

    # stop loop if frame is 10 and not frames have spares/strikes to throw for
    if current_frame >= 10 and prev_throw == "" and prev_prev_throw != "strike":
        break


print(sum(frame_score))


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
