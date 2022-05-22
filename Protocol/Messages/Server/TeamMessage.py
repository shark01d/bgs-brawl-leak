from ByteStream.Writer import Writer
from Utils.Helpers import Helpers
import random

class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVInt(1) # Gameroom Type
        self.writeUInt8(0)
        self.writeVInt(1)
        self.writeLong(1)
        self.writeUInt8(0)
        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeDataReference(15, self.player.map_id)

        self.writeBoolean(False)

        self.writeVInt(1)
        for x in range(1):

            self.writeVInt(1)

            self.writeLong(self.player.ID)

            self.writeDataReference(16, self.player.home_brawler)
            self.writeDataReference(29, self.player.home_skin)

            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(9)

            self.writeVInt(3)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            self.writeString("F1ash")
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)
            self.writeNullVInt()

            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            pass

        self.writeVInt(0)
        for x in range(0):
            pass

        self.writeUInt8(0)
        self.writeUInt8(0)

        if self.player.use_gadget:
            self.writeUInt8(6)
        else:
            self.writeUInt8(0)
