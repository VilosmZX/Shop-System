import random
import sys

payment_id = random.randint(1000000, 1000000000)

class Shop():

    def __init__(self, name, age, gender):
        self.balance = 0
        self.wallet = 0
        self.nama = name
        self.umur = age
        self.kelamin = gender

    def Menu(self):
        in_menu = True
        while in_menu:
            print(f"""
Selamag datang, {self.nama}

 1) Top Up Games
 2) Top Up Balance
 3) Cari Kerja untuk top up Balance
 4) Informasi pengguna

            """)
            action = input("Choose >> ")
            if action.isdigit() == True:
              action = int(action)

            if action == 1:
              a.Games()
            elif action == 2:
              a.Balance()
            elif action == 3:
              a.Job()
            elif action == 4:
              a.User_Info()


    def Games(self):
      try:
        if self.balance == 0:
          print("Warning >> Saldo mu Rp0!")
          input("Pencet Enter.....")
        user_is_shopping = True
        while user_is_shopping:
          print("""
Game available
1) Free Fire
2) Mobile Legend
3) Pubg Mobile
4) Kembali
                  """)
          action = int(input("Choose >>"))
          if action == 1:
            a.PaymentFF()
          elif action == 2:
            a.PaymentML()
          elif action == 4:
            a.Menu()
      except ValueError:
        print("Masukan angka!")
        input("Pencet Enter....")
        a.Games()
      except EOFError:
        print("\nPaksa Berhenti Program Berhasil!")
        sys.exit()


    def Balance(self):
        user_payment = True
        while user_payment:
          amount = int(input("Masukan Jumlah Balance: Rp"))
          if amount > self.wallet:
              print("Wallet mu tidak cukup, kerja lah untuk mendapat wallet.")
              input("Pencet Enter untuk kembali......")
              a.Menu()
          else:

             self.balance += amount
             self.wallet -= amount
             print("Balance mu sudah bertambah menjadi Rp{}\nSekarang kamu bisa top up!".format(self.balance))
             print("Sisa Walletmu: Rp{}".format(self.wallet))
             user_payment = False

        input("Press enter untuk kembali ke menu...")
        a.Menu()


    def PaymentFF(self):
      user_payment = True
      while user_payment:
        print("Sekarang kamu berada di menu pembayaran")
        action = int(input("Berapa banyak diamond yang kamu mau: : "))
        price = action * 250
        if  price > self.balance:
          print("Uang mu tidak cukup!\nUangmu: Rp{}".format(self.balance))
          continue
        else:
          print(f"""
Final Payment ( Mohon diperiksa )

Nama Pengguna: {self.nama}
Diamond: {action}
Harga: {price}
Games: Free Fire

Id Pembayaran: {payment_id}

                """)
          action = input("Lanjutkan?(y/n): ").lower()
          if action == "y":
            print("Terimakasih telah top up di toko kami.")
            self.balance -= price

          if action == "y":
            print(f"Balance mu sekarang: Rp{self.balance}")
            input("Pencet enter...")
            a.Menu()
          elif action == "n":
            input("Pembayaran dibatalkan...Pencet Enter untuk kembali...")
            a.Menu()

    def Job(self):
      try:
        gaji = random.randint(1000, 100000)
        jobs = [
          "Tukang Parkir",
          "Programmer",
          "Youtuber",
          "Koki",
          "Pendeta",
          "Pilot",
          "Supir"
            ]
        find_job = True
        while find_job:
          print("""
List Job

1) Tukang parkir ( Gaji: Random )
2) Programmer ( Gaji: Random )
3) Youtuber ( Gaji: Random )
4) Koki ( Gaji: Random )
5) Pendeta ( Gaji: Random )
6) Pilot ( Gaji: Random )
7) Supir ( Gaji: Random )

                      """)
          action = int(input("Job >> ")) - 1
          if action > 7:
            print(f"Pekerjaan hang tersedia tidak lebih dari 7\nKamu memilih pekerjaan ke {action}")
            print("Pencet Enter untuk mengulang......")
            continue
          else:
            self.wallet += gaji
            print(f"Kamu telah bekerja sebagai {jobs[action]}\nGaji: Rp{gaji} telah masuk ke wallet mu")
            input("Pencet Enter untuk kembali ke Menu.....")
            a.Menu()

      except EOFError as fc:
        pass
      except IndexError:
        find_job = False
        print("Masukan opsi yang ada!")
        a.Job()

    def PaymentML(self):
      user_payment = True
      while user_payment:
        print("Sekarang kamu berada di menu pembayaran")
        action = int(input("Berapa banyak diamond yang kamu mau: : "))
        price = action * 500
        if price > self.balance:
          print("Uang mu tidak cukup!\nUangmu: Rp{}".format(self.balance))
          print("Harga diamond: Rp{}".format(price))
          input("Pencet Enter.....")
          continue
        else:
          print(f"""
Final Payment ( Mohon diperiksa )

Diamond: {action}
Harga: {price}
Games: Mobile Legends

Id Pembayaran: {payment_id}

                """)
          action = input("Lanjutkan?(y/n): ").lower()
          if action == "y":
            print("Terima kasih telah top up di Toko kami, {}".format(self.nama))
            self.balance -= price
          if action == "y":
            print(f"Balance mu sekarang: Rp{self.balance}")
            input("Pencet enter...")
            a.Menu()
          elif action == "n":
            input("Pembayaran dibatalkan...Pencet Enter untuk kembali...")
            a.Menu()


    def User_Info(self):
      if self.kelamin == "L":
        self.kelamin = "Laki-laki"
      elif self.kelamin == "P":
        self.kelamin = "Perempuan"

      print(f"""
  Informasi Pengguna

  Nama: {self.nama}
  Umur: {self.umur}
  Kelamin: {self.kelamin}
  Balance: {self.balance}
  Wallet: {self.wallet}
  ID: {payment_id}

      """)
      input("Pencet Enter untuk kembali....")
      a.Menu()



nama = input("Masukan namamu: ").lower()
age = int(input("Umur: "))
if age <= 12 and age >= 0:
  print("Lu Bocil Pergi Sana!")
  sys.exit()
elif age >= 50:
  print("Lu ketuaan pergi sana!")
  sys.exit()
elif nama.isdigit() == True:
  print("Apa namamu menggunakan angka???? lucu sekali")
  next
elif age > 12 and age <= 50:
  next

gender = input("Kelamin(L/P): ").upper()
a = Shop(nama, age, gender)
a.Menu()
