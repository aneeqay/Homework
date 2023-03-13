class Guest:
    
    def __init__(self, name, fave_song, wallet):
        self.name = name
        self.fave_song = fave_song
        self.wallet = wallet

    def fave_song_exclamation(self, room):
        if self.fave_song in room.song_list:
            return "Whoo!"
        
    def pay_entry_fee(self, entry_fee):
        self.wallet -= entry_fee