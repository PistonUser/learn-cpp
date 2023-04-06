class enemy:
    def __init__(self, intelli, otherthing):
        self.intelli = intelli
        self.otherthing = otherthing


dumbo = enemy("stupid", "something")

print(dumbo.intelli + dumbo.otherthing)