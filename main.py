from rich.console import Console
from rich.panel import Panel
from pelanggan import pelanggan_menu
from owner import owner_menu

console = Console()

while True:
   console.print(Panel("SELAMAT DATANG DI TOKO", style="bold magenta"))
   console.print("[1] Mode Pelanggan")
   console.print("[2] Mode Owner")
   console.print("[3] Exit")

   pilih = console.input("\nMasukan pilihan: ")

   if pilih == "1":
      pelanggan_menu()
   elif pilih == "2":
      owner_menu()
   elif pilih == "3":
      console.print("[bold cyan]Sampai jumpa lagi semoga harimu menyenangkan[/]")
      break
   else:
      console.input("[red]Invalid Choice[/]")
