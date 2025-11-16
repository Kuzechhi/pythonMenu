from rich.console import Console
from rich.panel import Panel
from menu import menuItem, ShowMenu

console = Console()

def pelanggan_menu():
   pesanan = {}

   while True:
      console.print(Panel("Mode Pelanggan", style="bold green"))
      ShowMenu()
      
      pilihan = console.input("\nMasukan nama menu yang ingin anda pesan ('exit' buat selesai): ")
      if pilihan.lower() == "exit":
         break
      
      if pilihan not in menuItem:
         console.print("[bold red] menu tidak tersedia![/]")
         continue
      
      qty = int(console.input("Masukan jumlah porsi: "))
      pesanan[pilihan] = pesanan.get(pilihan, 0) + qty
      console.print("[bold green] ditambah ke keranjang[/]")
   
   invoice(pesanan)

def invoice(pesanan):
   console.print(Panel("STRUK PRMBELIAN", style="bold yellow" ))
   total = 0
   
   for item, qty in pesanan.items():
      harga = menuItem[item]
      subtotal = harga * qty
      total += subtotal
      console.print(f"[cyan]{item}[/] x {qty} = [green]Rp {subtotal}[/]")
      
   console.print(f"\n[bold magenta]TOTAL: Rp {total}[/]\n")
   console.print("[bold yellow] Terima Kasih Sudah Belanja")

   