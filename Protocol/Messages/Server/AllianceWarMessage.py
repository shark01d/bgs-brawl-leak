from ByteStream.Writer import Writer


class AllianceWarMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24776
        self.client = client
        self.player = player


    def encode(self):
        self.writeInt(0) # Player ID
        self.writeInt(1) # Player ID
        self.writeVInt(0) # Your Club Faction
        

        # Club War Events Array
        self.writeVInt(0) # Count
        for x in range(0):
            self.writeVInt(x)
        # Club War Events Array End
        

        # Club War Factions Array
        self.writeVInt(0) # Count
        for x in range(0):
            self.writeVInt(x)
        # Club War Factions Array End