class Janken:
    def __init__(self, display, rule):
        self.display = display
        self.rule = rule

    def play(self, left_hand: int, right_hand: int):
        result = self.rule.judge(left_hand, right_hand)
        self.display.show(result)


class DefaultRule:
    def judge(self, left_hand: int, right_hand: int):
        win = 1
        draw = 0   
        lose = -1

        if left_hand == 0:
            if right_hand == 0:
                result = draw 
            if right_hand == 1:
                result = win
            if right_hand == 2:
                result = lose
        
        elif left_hand == 1:
            if right_hand == 0:
                result = lose
            if right_hand == 1:
                result = draw
            if right_hand == 2:
                result = win

        else:
            if right_hand == 0:
                result = win
            if right_hand == 1:
                result = lose
            if right_hand == 2:
                result = draw
        return result


class ReverseRule:
    def judge(self, left_hand: int, right_hand: int):
        win = 1
        draw = 0   
        lose = -1

        if left_hand == 0:
            if right_hand == 0:
                result = draw 
            if right_hand == 1:
                result = win
            if right_hand == 2:
                result = lose
        
        elif left_hand == 1:
            if right_hand == 0:
                result = lose
            if right_hand == 1:
                result = draw
            if right_hand == 2:
                result = win

        else:
            if right_hand == 0:
                result = win
            if right_hand == 1:
                result = lose
            if right_hand == 2:
                result = draw
        return result * (-1)

    
class JapaneseDisplay:
    def show(self, result: int):
        if result == 1:
            print("勝ち")

        elif result == 0:
            print("分け")

        elif result == -1:
            print("負け")

        else:
            print("error")


class EnglishDisplay:
    def show(self, result: int):
        if result == 1:
            print("You win")

        elif result == 0:
            print("Draw")

        elif result == -1:
            print("You lose")

        else:
            print("error")


def main():
    display = EnglishDisplay()
    rule = ReverseRule()
    game = Janken(display, rule)
    game.play(0, 1)
    game.play(2, 0)
    game.play(1, 1)


if __name__ == '__main__':
    main()