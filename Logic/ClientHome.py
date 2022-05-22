from Logic.Home.LogicDailyData import LogicDailyData
from Logic.Home.LogicConfData import LogicConfData

class LogicClientHome:

    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)

        self.writeLong(self.player.ID)

        self.writeVInt(1)  # Hotification Count
        self.writeVInt(83) # NotifìcationID
        self.writeInt(0)
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString("F1ash")
        self.writeInt(0)
        self.writeString("Добро пожаловать в LW Brawl") # Title

        self.writeInt(0)
        self.writeString("Ты знал что у нас есть свой Telegram Канал а также веселый чат") # Subtitle

        self.writeInt(0)
        self.writeString("TELEGRAM") # Button Text 

        self.writeString("/36042168-49af-4e79-b5f3-13c8c279bc5c_brawltalkpopup.png") # ImageUrl
        self.writeString('28d8d5533ddecebf766daac49f3290415a36fa42')

        self.writeString("brawlstars://extlink?page=https%3A%2F%2Ft.me%2Flwbrawl") # RedirectLink
        self.writeVInt(3473)
        for x in range(0):
            pass

        self.writeVInt(0)  # Unknown

        self.writeUInt8(0) # Unknown
