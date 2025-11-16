from rich.console import Console
from rich.panel import Panel
from menu import menuItem, ShowMenu

console = Console()

def owner_menu():
   while True:
      console.print(Panel("MODE OWNER", style="bold blue"))
      console.print("[1] Lihat Menu")
      console.print("[2] Tambah menu")
      console.print("[3] Hapus Menu")
      console.print("[4] Ubah Harga")
      console.print("[5] Exit")

      pilih = console.input("\nPilih aksi: ")

      if pilih == "1":
         ShowMenu()
      elif pilih == "2":
         nama = console.input("Nama Menu Baru: ")
         harga = int(console.input("Harga: "))
         menuItem[nama] = harga
         console.print("[green]Menu berhasil ditambahkan[/]")
      elif pilih == "3":
         nama = console.input("Nama Menu yang ingin dihapus: ")
         if nama in menuItem:
            del menuItem[nama]
            console.print("[red]Menu berhasil dihapus[/]")
         else:
            console.print("[red]Menu tidak ditemukan[/]")
      elif pilih == "4":
         nama = console.input("Nama Menu yang ingin diubah: ")
         if nama in menuItem:
            harga = int(console.input("Harga Baru: "))
            menuItem[nama] = harga
            console.print("[yellow]Harga berhasil diupdate")
         else:
            console.print("[red]Menu tidak ditemukan")
      elif pilih == "5":
         break
      
      console.print("\n")
