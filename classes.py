class Frame:
    def __init__(self) -> None:
        self.throw_score = [0] * 3
        self.throw_num = 0
        # self.is_strike = False
        # self.is_spare = False
        self.bonus_throws = 0
        self.is_current = False

    def throw(self, score):
        self.throw_score[self.throw_num] = score
        if self.is_current:
            if self.throw_num == 0 and self.get_score() == 10:
                self.bonus_throws = 2
                self.is_current = False
            if self.throw_num == 1 and self.get_score() == 10:
                self.bonus_throws = 1
                self.is_current = False
            if self.throw_num == 1:
                self.is_current = False

        else:
            self.bonus_throws -= 1
        self.throw_num += 1

    def is_active(self):
        return self.bonus_throws > 0 or self.is_current

    def set_current(self):
        self.is_current = True

    def is_complete(self):
        return self.throw_num == 2 or self.bonus_throws > 0

    def get_score(self):
        return sum(self.throw_score)


class Game:
    def __init__(self) -> None:
        self.frame_num = 0
        self.frames = []
        for i in range(10):
            self.frames.append(Frame())
        self.frames[0].set_current()

    def start(self):
        while True:
            score = int(input("Enter your score: "))
            for frame in self.frames:
                if frame.is_active():
                    frame.throw(score)
            if self.frame_num < 10:
                if self.frames[self.frame_num].is_complete():
                    self.frame_num += 1
                    if self.frame_num < 10:
                        self.frames[self.frame_num].set_current()
            self.print_score()
            if self.frame_num >= 10 and self.frames[9].is_active() == False:
                break

    def print_score(self):
        for frame in self.frames:
            print(frame.get_score())

    def get_total(self):
        total = 0
        for frame in self.frames:
            total += frame.get_score()
        return total


def main():
    game = Game()
    game.start()
    print(game.get_total())


if __name__ == "__main__":
    main()
