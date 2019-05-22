class Mission:
    def __init__(self, game):
        self.game = game
        self.objetivos = {"lvl_0": self.All_kill, "lvl_1": self.All_kill, "v1": self.the_End, "v2": self.the_End }
        self.mission_actual = self.objetivos[self.game.lvl]

    def update(self):
        self.mission_actual()
        if self.mission_actual() == True:
            pass

    # print("¡Mission COMPLET!")

    def All_kill(self):
        if len(self.game.enemies) > 0:
            return False
        else:
            return True
    def the_End(self):
        """event = pg.event.get()
        if event != None:
            exit(0)"""
        pass


