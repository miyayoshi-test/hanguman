import random

#ハングマンの関数
def hangman(word):
    wrong = 0 #ユーザが間違った回数を記録する
    stages = ["",
              "__________      ",
              "|               ",
              "|      |        ",
              "|      0        ",
              "|     /|\       ",
              "|     / \       ",
              "|_______________",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    while wrong < len(stages) -1 :
        print("\n");
        print("1文字を予想してね")
        char = input("文字:")
        if char in rletters:
            cind = rletters.index(char);
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1;
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ちです")
            print(" ".join(board))
            win = True
            break;
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負けです。正解は{0}です".format(word))

wordList = ["cat","monkey","elephant"]
r = random.randint(0,2)
hangman(wordList[r])
