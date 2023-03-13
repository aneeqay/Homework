class Room:
    
    def __init__(self, capacity, entry_fee, till):
        self.guest_list = []
        self.song_list = []
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = till

    def check_in(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
            self.charge_entry_fee(guest)
    
    def check_out(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_list.append(song)

    def charge_entry_fee(self, guest):
        guest.pay_entry_fee(self.entry_fee)
        self.till += self.entry_fee
