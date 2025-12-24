class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"Kitap Adı: {self.name}, Yazar: {self.author}, Yayın Yılı: {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author, year):
        book = Book(name, author, year)
        self.books.append(book)
        print("Kitap başarıyla eklendi.")

    def remove_book(self, name):
        for book in self.books:
            if book.name.lower() == name.lower():
                self.books.remove(book)
                print("Kitap başarıyla silindi.")
                return
        print("Kitap bulunamadı.")

    def search_by_name(self, name):
        found = False
        for book in self.books:
            if name.lower() in book.name.lower():
                print(book)
                found = True
        if not found:
            print("Aranan isimde kitap bulunamadı.")

    def search_by_author(self, author):
        found = False
        for book in self.books:
            if author.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("Bu yazara ait kitap bulunamadı.")

    def list_books(self):
        if not self.books:
            print("Kütüphanede hiç kitap yok.")
            return
        print("\nKütüphanedeki Kitaplar:")
        for book in self.books:
            print(book)


def menu():
    print("\n--- KÜTÜPHANE YÖNETİM SİSTEMİ ---")
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitap Ara (İsme Göre)")
    print("4. Kitap Ara (Yazara Göre)")
    print("5. Tüm Kitapları Listele")
    print("6. Çıkış")


def main():
    library = Library()

    while True:
        menu()
        choice = input("Seçiminizi girin (1-6): ")

        if choice == "1":
            name = input("Kitap Adı: ")
            author = input("Yazar: ")
            year = input("Yayın Yılı: ")
            library.add_book(name, author, year)

        elif choice == "2":
            name = input("Silinecek Kitap Adı: ")
            library.remove_book(name)

        elif choice == "3":
            name = input("Aranacak Kitap Adı: ")
            library.search_by_name(name)

        elif choice == "4":
            author = input("Aranacak Yazar Adı: ")
            library.search_by_author(author)

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen 1-6 arası bir değer girin.")


if __name__ == "__main__":
    main()