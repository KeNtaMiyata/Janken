from janken import Janken, DefaultRule, ReverseRule, JapaneseDisplay, EnglishDisplay


def main():
    display = EnglishDisplay()
    rule = ReverseRule()
    game = Janken(display, rule)
    game.play(0, 1)
    game.play(2, 0)
    game.play(1, 1)


if __name__ == '__main__':
    main()