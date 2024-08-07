import Items


class player:

    name = "탐험가"
    livesLeft = 3
    boulderVisits = 0
    maxHealth = 100
    health = maxHealth

    def getName(self):
        return self.name

    def getLivesLeft(self):
        return self.livesLeft

    def died(self):
        if self.livesLeft > 0:
            self.livesLeft -= 1

    def isAlive(self):
        return True if self.livesLeft > 0 else False

    def getBoulderVisits(self):
        return self.boulderVisits

    def visitBoulder(self):
        self.boulderVisits += 1

    def addLife(self, lives=1):
        self.livesLeft += lives
        self.health = self.maxHealth

    def loseLife(self, lives=1):
        self.livesLeft -= lives

        if self.livesLeft < 0:
            self.livesLeft = 0

        if self.livesLeft == 0:
            self.health = 0
        elif self.livesLeft >= 1:
            self.health = self.maxHealth

    def getHealth(self):
        return self.health

    def addHealth(self, health):
        self.health += health

        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def loseHealth(self, health):
        self.health -= health
        if self.health < 0:
            self.loseLife()
