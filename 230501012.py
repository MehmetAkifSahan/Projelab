import random

Adam_Asmaca_Aşamalar = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

TOLERANCE = 1e-6

class Kelimeler:
    Kategoriler = {
        "Meyveler": ["elma", "armut", "muz", "çilek", "portakal", "kiraz", "şeftali"],
        "Hayvanlar": ["aslan", "kaplumbağa", "kartal", "köpek", "kedi", "tavşan", "kapibara"],
        "Teknoloji": ["bilgisayar", "telefon", "tablet", "monitör", "klavye", "sunucu"]
    }

    def __init__(self):
        self.Kategoriler, self.word = self.Rastgele_kelime_secimi()

    def Rastgele_kelime_secimi(self):
        cat = random.choice(list(self.Kategoriler.keys()))
        word = random.choice(self.Kategoriler[cat])
        return cat, word.lower()

    def mask(self, guessed): #rastgele seçilen kelimenin saklanması
        return "".join(ch if ch in guessed else "_" for ch in self.word)


class Hesap_Makinesi:
    def __init__(self):
        self.ops_used = set()
        self.allowed_ops = {'+': 'Toplama', '-': 'Çıkarma', '*': 'Çarpma', '/': 'Bölme'}

    def perform(self):
        remaining = [op for op in self.allowed_ops if op not in self.ops_used]
        if not remaining:
            print("Tüm işlemler kullanıldı.")
            return False, 0

        print("Kullanılabilir işlemler:")
        for op in remaining:
            print(f" {op} => {self.allowed_ops[op]}")

        op = input("Bir işlem seç (+, -, *, /) veya 'q' ile çık: ").strip()
        if op.lower() == 'q':
            return None, 0  # oyunu kapat

        if op not in remaining:
            print("Geçersiz işlem.")
            return False, 0

        try:
            a = float(input("Birinci sayı: ").replace(",", "."))
            b = float(input("İkinci sayı: ").replace(",", "."))
        except ValueError:
            print("Geçersiz sayı!")
            self.ops_used.add(op)
            return False, 1

        if op == '/' and b == 0:
            print("Sıfıra bölme hatası!")
            self.ops_used.add(op)
            return False, 1

        correct = eval(f"{a}{op}{b}") #doğrıu cevabı tutan satır

        try:
            ans = float(input("Sonucu yazın: ").replace(",", "."))
        except ValueError:
            print("Geçersiz sayı!")
            self.ops_used.add(op)
            return False, 1

        self.ops_used.add(op)

        if abs(ans - correct) <= TOLERANCE:
            print("Doğru! Bonus kazandınız.")
            return True, 0
        else:
            print(f"Yanlış! Doğru sonuç {correct}")
            return False, 1

        #oyunun genel kodları
class AdamAsmaca:
    def __init__(self):
        self.word_manager = Kelimeler()
        self.Hesaplama = Hesap_Makinesi()
        self.guessed = set()
        self.wrong = 0
        self.bonus = 0
        self.revealed_category = False
        self.MAX_ERRORS = len(Adam_Asmaca_Aşamalar) - 1
        # harf tahmini veya diğer seçeneklerin seçimi
    def ask_letter(self):
        while True:
            val = input("Harf tahmin et (veya 'Hesaplama', 'İpucu', 'Çıkış'): ").lower().strip()
            if val in ("hesaplama", "ipucu", "çıkış"):
                return val
            if len(val) != 1 or not val.isalpha():
                print("Lütfen tek harf gir.")
                continue
            if val in self.guessed:
                print("Bu harfi zaten tahmin ettin.")
                continue
            return val

    def play(self):
        print("=== Adam Asmaca ===")

        while True:
            print(Adam_Asmaca_Aşamalar[min(self.wrong, self.MAX_ERRORS)])
            masked = self.word_manager.mask(self.guessed)

            print("Kelime:", " ".join(masked))
            print("Tahminler:", " ".join(sorted(self.guessed)) or "(yok)")
            print("Kalan hata:", self.MAX_ERRORS - self.wrong)
            print("Bonus:", self.bonus)
            if self.revealed_category:
                print("Kategori:", self.word_manager.Kategoriler)
            print("-" * 30)

            if "_" not in masked:
                print("Tebrikler! Kelime:", self.word_manager.word)
                break

            if self.wrong >= self.MAX_ERRORS:
                print("Kaybettiniz! Kelime:", self.word_manager.word)
                break

            choice = self.ask_letter()
            #hesap makinesi işlemi ve ek bonus kazanımı
            if choice == "hesaplama":
                result = self.Hesaplama.perform()
                if result is None: 
                    print("Oyundan çıkış yapıldı.")
                    break
                correct, penalty = result
                if correct:
                    self.bonus += 1
                else:
                    self.wrong += penalty
                continue
            #ipucunun kullanımı ve bonusların harcanması
            if choice == "ipucu":
                if self.bonus > 0:
                    self.bonus -= 1
                    self.revealed_category = True
                    print("Kategori açıldı!")
                else:
                    print("Bonus yok!")
                continue

            if choice == "çıkış": #istendiğinde çıkış yapılması için 
                print("Oyundan çıkılıyor.")
                break

            # Harf tahminleri burada işlenir
            self.guessed.add(choice)
            if choice in self.word_manager.word:
                print(f"Doğru! '{choice}' var.")
            else:
                print(f"Yanlış! '{choice}' yok.")
                self.wrong += 1

        print("Oyun bitti!")


if __name__ == "__main__":
    game = AdamAsmaca()
    game.play()
