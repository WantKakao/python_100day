from tictactoe import Tictactoe


def win(x, y):
    global i, is_game_on
    print()
    print(f"WINNER IS {T.item[x][y]}")
    print()
    resume = input("Type 'y' to restart game or 'f' to finish: ")
    if resume == 'y':
        T.reset()
        i = 0
    else:
        is_game_on = False


def get_input():
    while True:
        try:
            x, y = map(int, input("빈 칸 중 하나의 행과 열을 띄어쓰기로 구분해 적어주세요: ").split())
            if x >= 4 or y >= 4:
                print("행과 열의 값은 1 이상 3 이하의 숫자로 입력해주세요.")
                continue
            if T.item[x - 1][y - 1] != ' ':
                print("선택한 위치가 이미 채워져 있습니다. 다른 위치를 선택해주세요.")
                continue
            break
        except ValueError:
            print("잘못된 입력입니다. 다시 입력해주세요.")
    return x, y


T = Tictactoe()
i = 0
is_game_on = True
T.show()
while is_game_on:
    print()
    if i == 0:
        print("선공 O의 차례!")
        a, b = get_input()
        T.put(a, b, 'O')
        i = 1
    else:
        print("후공 X의 차례!")
        a, b = get_input()
        T.put(a, b, 'X')
        i = 0
    T.show()
    for idx in range(3):
        if T.item[idx][0] == T.item[idx][1] == T.item[idx][2] != ' ':
            win(idx, 0)
            break
        if T.item[0][idx] == T.item[1][idx] == T.item[2][idx] != ' ':
            win(0, idx)
            break
        if T.item[0][0] == T.item[1][1] == T.item[2][2] != ' ':
            win(1, 1)
            break
        if T.item[2][0] == T.item[1][1] == T.item[0][2] != ' ':
            win(1, 1)
            break