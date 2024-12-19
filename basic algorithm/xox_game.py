class Game():
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.status = True
        self.move = 0

    def play(self):
        if self.move % 2 == 0:
            self.p1_select()
        else:
            self.p2_select()

        self.status = self.game_control()

        if not self.status:
            self.show_board()
            winner = ""
            if self.move % 2 == 0:
                winner = "X"
            else:
                winner = "O"

            print(f"oyun bitti kazanan: {winner}")

        self.move += 1

    def p1_select(self):
        self.show_board()
        print("Birinci Oyuncu")
        row = int(input("satır giriniz: "))

        while row < 1 or row > 3:
            row = int(input("girilecek sayı değeri 1 ile 3 arasında olamlı"))

        column = int(input("sütun giriniz: "))
        while column < 1 or column > 3:
            column = int(input("girilecek sayı değeri 1 ile 3 arasında olamlı"))

        if self.is_full(row, column):
            self.p1_select()
        else:
            self.board[row-1][column-1] = "X"

    def p2_select(self):
        self.show_board()
        print("İkinci Oyuncu")
        row = int(input("satır giriniz: "))
        while row < 1 or row > 3:
            row = int(input("girilecek sayı değeri 1 ile 3 arasında olamlı"))

        column = int(input("sütun giriniz: "))
        while column < 1 or column > 3:
            column = int(input("girilecek sayı değeri 1 ile 3 arasında olamlı"))

        if self.is_full(row, column):
            self.p2_select()
        else:
            self.board[row-1][column-1] = "O"

    def is_full(self, row, column):
        if self.board[row-1][column-1] != " ":
            return True
        else:
            return False

    def show_board(self):
        for i in self.board:
            print(i)

    def game_control(self):
        # YATAY KONTROL
        if [self.board[0][0],self.board[0][1],self.board[0][2]] == "XXX" or [self.board[0][0],self.board[0][1],self.board[0][2]] == "OOO":
           return False
        if [self.board[1][0],self.board[1][1],self.board[1][2]] == "XXX" or [self.board[1][0],self.board[1][1],self.board[1][2]] == "OOO":
           return False
        if [self.board[2][0],self.board[2][1],self.board[2][2]] == "XXX" or [self.board[2][0],self.board[2][1],self.board[2][2]] == "OOO":
           return False

        # DİKEY KONTROL
        if [self.board[0][0],self.board[1][0],self.board[2][0]] == "XXX" or [self.board[0][0],self.board[1][0],self.board[2][0]] == "OOO":
           return False
        if [self.board[0][1],self.board[1][1],self.board[2][1]] == "XXX" or [self.board[0][1],self.board[1][1],self.board[2][1]] == "OOO":
           return False
        if [self.board[0][2],self.board[1][2],self.board[2][2]] == "XXX" or [self.board[0][0],self.board[1][2],self.board[2][2]] == "OOO":
           return False

        # ÇAPRAZ KONTROL
        if [self.board[0][0],self.board[1][1],self.board[2][2]] == "XXX" or [self.board[0][0],self.board[1][1],self.board[2][2]] == "OOO":
           return False
        if [self.board[0][2],self.board[1][1],self.board[2][0]] == "XXX" or [self.board[0][2],self.board[1][1],self.board[2][0]] == "OOO":
           return False

        return True


game = Game()

while game.status:
    game.play()
