import unittest

from models.book_class import Book
from models.book_object import add_book, delete_book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Now and Then", "William Corlett", "Fiction - Historical", "https://app.thestorygraph.com/books/a5277205-54b5-4fbe-a359-dcd8004ea0a9", "https://cdn.thestorygraph.com/p8yv2v9202eipojiu02pzprx6bd9")
        self.book2 = Book("Small Things Like These", "Claire Keegan", "Fiction - Historical", "https://app.thestorygraph.com/books/a49523ae-4893-4a00-892f-876543ddf423", "https://cdn.thestorygraph.com/ax6l7ekdmah961c7lthkv5ahvhjh")
        self.book3 = Book("Taste", "Stanley Tucci", "Non-Fiction - Memoir", "https://app.thestorygraph.com/books/9de3288b-b28f-4af2-9fcb-788670336e37", "https://cdn.thestorygraph.com/o9u4erbafu8srluwvferpv561egl")
        self.book4 = Book("I'm a Fan", "Sheena Patel", "Fiction - Contemporary", "https://app.thestorygraph.com/books/446ae4fa-df63-4e98-9333-edacd8592ca6", "https://cdn.thestorygraph.com/d5qtzy4ad6rg2fcd1wvrdbcduix1")
        self.book5 = Book("The Dry", "Jane Harper", "Fiction - Thriller", "https://app.thestorygraph.com/books/333650e7-b9ee-433a-a765-ffaaf2673e0f", "https://cdn.thestorygraph.com/vnvwdz2cjdqomz022w1u48x1vwfn")
        self.book6 = Book("The Devil You Know", "Dr Gwen Adshead", "Non-Fiction - Sociology", "https://app.thestorygraph.com/books/ea9f0822-0941-49dc-aa2a-ca3e0de7b161", "https://cdn.thestorygraph.com/rf8qvil0eqyycjknh0o6qwgrzlda")
        

    def test_book_has_name(self):
        self.assertEqual("Now and Then", self.book1.title)
        self.assertEqual("Small Things Like These", self.book2.title)
        self.assertEqual("Taste", self.book3.title)
        self.assertEqual("I'm a Fan", self.book4.title)
        self.assertEqual("The Dry", self.book5.title)
        self.assertEqual("The Devil You Know", self.book6.title)

    def test_book_has_author(self):
        self.assertEqual("William Corlett", self.book1.author)
        self.assertEqual("Claire Keegan", self.book2.author)
        self.assertEqual("Stanley Tucci", self.book3.author)
        self.assertEqual("Sheena Patel", self.book4.author)
        self.assertEqual("Jane Harper", self.book5.author)
        self.assertEqual("Dr Gwen Adshead", self.book6.author)

    def test_book_has_genre(self):
        self.assertEqual("Fiction - Historical", self.book1.genre)
        self.assertEqual("Fiction - Historical", self.book2.genre)
        self.assertEqual("Non-Fiction - Memoir", self.book3.genre)
        self.assertEqual("Fiction - Contemporary", self.book4.genre)
        self.assertEqual("Fiction - Thriller", self.book5.genre)
        self.assertEqual("Non-Fiction - Sociology", self.book6.genre)

    def test_book_has_storygraph_link(self):
        self.assertEqual("https://app.thestorygraph.com/books/a5277205-54b5-4fbe-a359-dcd8004ea0a9", self.book1.link)
        self.assertEqual("https://app.thestorygraph.com/books/a49523ae-4893-4a00-892f-876543ddf423", self.book2.link)
        self.assertEqual("https://app.thestorygraph.com/books/9de3288b-b28f-4af2-9fcb-788670336e37", self.book3.link)
        self.assertEqual("https://app.thestorygraph.com/books/446ae4fa-df63-4e98-9333-edacd8592ca6", self.book4.link)
        self.assertEqual("https://app.thestorygraph.com/books/333650e7-b9ee-433a-a765-ffaaf2673e0f", self.book5.link)
        self.assertEqual("https://app.thestorygraph.com/books/ea9f0822-0941-49dc-aa2a-ca3e0de7b161", self.book6.link)

    def test_book_has_image_link(self):
        self.assertEqual("https://cdn.thestorygraph.com/p8yv2v9202eipojiu02pzprx6bd9", self.book1.image)
        self.assertEqual("https://cdn.thestorygraph.com/ax6l7ekdmah961c7lthkv5ahvhjh", self.book2.image)
        self.assertEqual("https://cdn.thestorygraph.com/o9u4erbafu8srluwvferpv561egl", self.book3.image)
        self.assertEqual("https://cdn.thestorygraph.com/d5qtzy4ad6rg2fcd1wvrdbcduix1", self.book4.image)
        self.assertEqual("https://cdn.thestorygraph.com/vnvwdz2cjdqomz022w1u48x1vwfn", self.book5.image)
        self.assertEqual("https://cdn.thestorygraph.com/rf8qvil0eqyycjknh0o6qwgrzlda", self.book6.image)


    # def test_book_can_be_added(self):
    #     book7 = Book("Hourglass", "Kieran Goddard", "Fiction - Contemporary", "https://app.thestorygraph.com/books/b4604950-f31c-48aa-925c-49865cce18c8", "https://cdn.thestorygraph.com/ba1l3mrzsenm7anffv5y9440cknk")
    #     book_list = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6]
    #     add_book(book7)
    #     self.assertEqual(7, len(book_list))

    # def test_book_can_be_deleted(self):
    #     book_list = [self.book1, self.book2, self.book3, self.book4, self.book5, self.book6]
    #     delete_book(5)
    #     self.assertEqual(5, len(book_list))
