class WhoAmI():
    def __init__(self):
        self.name = "the body"
        #phone status
        self.hasphone = False
        self.unlockedphone = False
        self.checkedphone = False
        #nightstand status
        self.checkedns = False
        #dresser status
        self.checkeddresser = False
        #cabinet status
        self.checkedcabinets = False
        #tv status
        self.tvon = False
        #keys status
        self.haskeys = False
        #wallet status
        self.haswallet = False
        #body status
        self.clean = False
        self.clothed = False
        self.fed = False
        self.shoed = False
        #counters
        self.spray = 0
        self.monster = 0
        #location status
        self.spot = "bed"
        self.lastspot = ""
        #situation status
        self.event = ""
        self.situation = ""
