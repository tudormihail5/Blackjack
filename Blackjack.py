import random as r
amount2 = 0


def create_deck():
    deck = []
    for j in range(0, 4):
        for d in range(2, 11):
            deck.append(str(d))
        deck.append("A")
        deck.append("J")
        deck.append("Q")
        deck.append("K")
    return deck


class Player:
    def __init__(self, hand, score=0, money=100):
        self.hand = hand
        self.score = score
        self.money = money

    def initial(self):
        d = Deck.pop()
        self.hand.append(d)
        b = Deck.pop()
        self.hand.append(b)
        if d == "J" or d == "Q" or d == "K":
            d = 10
        elif d == "A":
            d = 11
        else:
            d = int(d)
        if b == "J" or b == "Q" or b == "K":
            b = 10
        elif b == "A":
            b = 11
        else:
            b = int(b)
        s = d + b
        self.score = s
        if self.score == 22:
            self.score -= 10

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def hit(self):
        c = Deck.pop()
        self.hand.append(c)
        if c == "J" or c == "Q" or c == "K":
            c = 10
        elif c == "A":
            c = 11
        else:
            c = int(c)
        self.score += c
        if c == 11 and self.score > 21:
            self.score -= 10

    def win(self, hand2):
        if self.score == 21 and len(self.hand) == 2:
            print("You won with a Blackjack!")
            self.money += amount2 * 2.5
        elif self.score == hand2 and self.score <= 21:
            print("Draw!")
            self.money += amount2
        elif hand2 > 21 and self.score > 21:
            print("Draw!")
            self.money += amount2
        elif hand2 < self.score <= 21 or hand2 > 21:
            print("You won!")
            self.money += amount2 * 2
        else:
            print("You lost!")

    def bet(self, amount):
        self.money -= amount
        global amount2
        amount2 = amount

    def __str__(self):
        return "Hand: " + str(self.hand) + " and score: " + str(self.score) + "\nMoney: £" + str(self.money)


def print2(printing):
    if printing[8] == "1":
        printing = printing[:8] + "X" + printing[10:18]
    else:
        printing = printing[:8] + "X" + printing[9:17]
    return printing


i = 0
print("Welcome!")
while True:
    Deck = create_deck()
    r.shuffle(Deck)
    player1 = Player([])
    if i > 0:
        player1.set_money(m)
    player2 = Player([])
    x = input("How much do you want to bet?\n")
    player1.bet(int(x))
    player1.initial()
    player2.initial()
    print("Player1:")
    print(player1)
    print("Player2:")
    a = str(player2)
    print(print2(a))
    while player1.score < 21:
        x = input("Do you want to draw another card?(y/n) ")
        if x == "y":
            player1.hit()
            print("Player1:")
            print(player1)
        else:
            break
    print("Player1:")
    print(player1)
    while player2.score <= 17:
        player2.hit()
        a = str(player2)
        print("Player2:")
        print(a[:-12])
    player1.win(player2.score)
    a = str(player2)
    print("Player2:")
    print(a[:-12])
    print("Player1:")
    print(player1)
    x = input("Do you want to play again?(y/n) ")
    if x == "n":
        break
    m = player1.get_money()
    i += 1
print("Thank you for playing Blackjack with us!")
