class Room:
    
    def __init__(self, guest_list, song_list):
        self.guest_list = []
        self.song_list = []

    def check_in(self, Guest):
        Room.guest_list.append(Guest)
    
    def check_out(self, Guest):
        Room.guest_list.remove(Guest)
