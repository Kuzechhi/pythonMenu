from rich.table import Table
from rich.console import Console

console = Console()

menuItem = {
   "nasi Goreng": 15_000,
   "ayam geprek": 18_000,
   "Es teh manis": 6_000,
   "Kopi gula Aren": 5_000,
}

def ShowMenu():
   table = Table(title="Menu Toko", style="bold cyan")
   table.add_column("Nama Menu", justify="left")
   table.add_column("Harga", justify="right")

   for nama, harga in menuItem.items():
      table.add_row(nama, f"Rp {harga}")

   console.print(table)