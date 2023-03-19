from models.book_class import Book

book1 = Book("Now and Then", "William Corlett", "Fiction - Historical", "https://app.thestorygraph.com/books/a5277205-54b5-4fbe-a359-dcd8004ea0a9", "https://cdn.thestorygraph.com/p8yv2v9202eipojiu02pzprx6bd9")
book2 = Book("Small Things Like These", "Claire Keegan", "Fiction - Historical", "https://app.thestorygraph.com/books/a49523ae-4893-4a00-892f-876543ddf423", "https://cdn.thestorygraph.com/ax6l7ekdmah961c7lthkv5ahvhjh")
book3 = Book("Taste", "Stanley Tucci", "Non-Fiction - Memoir", "https://app.thestorygraph.com/books/9de3288b-b28f-4af2-9fcb-788670336e37", "https://cdn.thestorygraph.com/o9u4erbafu8srluwvferpv561egl")
book4 = Book("I'm a Fan", "Sheena Patel", "Fiction - Contemporary", "https://app.thestorygraph.com/books/446ae4fa-df63-4e98-9333-edacd8592ca6", "https://cdn.thestorygraph.com/d5qtzy4ad6rg2fcd1wvrdbcduix1")
book5 = Book("The Dry", "Jane Harper", "Fiction - Thriller", "https://app.thestorygraph.com/books/333650e7-b9ee-433a-a765-ffaaf2673e0f", "https://cdn.thestorygraph.com/vnvwdz2cjdqomz022w1u48x1vwfn")
book6 = Book("The Devil You Know", "Dr Gwen Adshead", "Non-Fiction - Sociology", "https://app.thestorygraph.com/books/ea9f0822-0941-49dc-aa2a-ca3e0de7b161", "	https://cdn.thestorygraph.com/rf8qvil0eqyycjknh0o6qwgrzlda")

book_list = [book1, book2, book3, book4, book5, book6]

def add_book(self, new_book):
    book_list.append(new_book)

def delete_book(self, index):
    book_list.remove(index)

# def toggle_check_out(self, status):

