import math

WINS = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
AI, HUMAN = "O", "X"

def winner(b):
    for a, c, d in WINS:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return "Tie" if " " not in b else None

def minimax(b, is_ai, alpha, beta):
    w = winner(b)
    if w == AI: return 1
    if w == HUMAN: return -1
    if w == "Tie": return 0
    best = -math.inf if is_ai else math.inf
    for i in range(9):
        if b[i] == " ":
            b[i] = AI if is_ai else HUMAN
            s = minimax(b, not is_ai, alpha, beta)
            b[i] = " "
            if is_ai:
                best = max(best, s); alpha = max(alpha, s)
            else:
                best = min(best, s); beta = min(beta, s)
            if beta <= alpha:
                break
    return best

def best_move(b):
    move, best = None, -math.inf
    for i in range(9):
        if b[i] == " ":
            b[i] = AI
            s = minimax(b, False, -math.inf, math.inf)
            b[i] = " "
            if s > best:
                best, move = s, i
    return move

def show(b):
    print()
    for r in range(3):
        print(" " + " | ".join(b[r*3:r*3+3]))
        if r < 2: print("---+---+---")
    print()

def main():
    b = [" "] * 9
    print("Tic-Tac-Toe: you are X, AI is O. Cells 1-9 (left to right, top to bottom).")
    show(b)
    while True:
        try:
            m = int(input("Your move (1-9): ")) - 1
            if not 0 <= m < 9 or b[m] != " ":
                raise ValueError
        except ValueError:
            print("Invalid move."); continue
        b[m] = HUMAN
        if not winner(b):
            b[best_move(b)] = AI
        show(b)
        w = winner(b)
        if w:
            print("It's a tie!" if w == "Tie" else f"{w} wins!")
            break

if __name__ == "__main__":
    main()
