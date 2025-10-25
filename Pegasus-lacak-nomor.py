import os
import time
import sys
from datetime import datetime
import random
import requests
from tqdm import tqdm
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows support
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
    {Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════╗
    ║                         PEGASUS LACAK NOMOR v1.0                          ║
    ║                     Created by: Letda Kes dr. luthfi                       ║
    ╚════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(banner)

def check_password():
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        password = input(f"\n{Fore.YELLOW}[!] Masukkan Password Aktivasi: {Style.RESET_ALL}")
        if password == "luthfi":
            print(f"{Fore.GREEN}[✓] Password benar!{Style.RESET_ALL}")
            time.sleep(1)
            return True
        attempts += 1
        if attempts < max_attempts:
            print(f"\n{Fore.RED}[!] Password salah! Sisa percobaan: {max_attempts - attempts}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}[!] Maksimal percobaan terlampaui. Program berhenti.{Style.RESET_ALL}")
            sys.exit(1)
    return False

def loading_animation():
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for _ in range(20):
        for char in chars:
            sys.stdout.write(f"\r{Fore.CYAN}[{char}] Loading...{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r" + " " * 50 + "\r", end="")

def simulate_search():
    print(f"\n{Fore.CYAN}[INFO] Processing Target Data...{Style.RESET_ALL}")
    loading_animation()
    for _ in tqdm(range(100), desc="Search Data", bar_format="{l_bar}█{bar}█{r_bar}", 
                 colour="cyan", ncols=75):
        time.sleep(0.03)

def generate_random_data():
    # List of sample data for more realistic results
    names = ["Budi Santoso", "Siti Rahayu", "Ahmad Hidayat", "Dewi Putri", "Joko Susanto"]
    streets = ["Jalan Sudirman", "Jalan Gatot Subroto", "Jalan Thamrin", "Jalan Merdeka"]
    cities = ["Jakarta", "Surabaya", "Bandung", "Medan", "Semarang"]
    provinces = ["DKI Jakarta", "Jawa Timur", "Jawa Barat", "Sumatera Utara", "Jawa Tengah"]
    
    return {
        "Nama": random.choice(names),
        "Jenis Kelamin": random.choice(["Laki-laki", "Perempuan"]),
        "Birthday": f"{random.randint(1980, 2000)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
        "Jalan": random.choice(streets),
        "Kota/Town": random.choice(cities),
        "Provinsi": random.choice(provinces),
        "Kode Pos": str(random.randint(10000, 99999)),
        "Negara": "Indonesia",
        "Latitude": f"{random.uniform(-6.0, 6.0):.6f}",
        "Longitude": f"{random.uniform(95.0, 141.0):.6f}",
        "Waktu Pencarian": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def display_result(data):
    print(f"\n{Fore.GREEN}Result:{Style.RESET_ALL}")
    for key, value in data.items():
        if key == "Waktu Pencarian":
            print(f"{Fore.YELLOW}{key}: {value}{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}{key}: {value}{Style.RESET_ALL}")
    print(f"\n{Fore.GREEN}[✔] Search Data complete!{Style.RESET_ALL}")

def main():
    clear_screen()
    print_banner()
    
    if not check_password():
        return
    
    while True:
        clear_screen()
        print_banner()
        
        target = input(f"\n{Fore.YELLOW}[?] Masukkan Nomor Telepon (08xxx) atau NIK: {Style.RESET_ALL}")
        
        if not target:
            print(f"\n{Fore.RED}[!] Input tidak boleh kosong!{Style.RESET_ALL}")
            time.sleep(2)
            continue
            
        if not (target.startswith('08') or len(target) == 16):
            print(f"\n{Fore.RED}[!] Format nomor telepon atau NIK tidak valid!{Style.RESET_ALL}")
            time.sleep(2)
            continue
            
        simulate_search()
        result = generate_random_data()
        display_result(result)
        
        choice = input(f"\n{Fore.YELLOW}[?] Ingin mencari lagi? (y/n): {Style.RESET_ALL}")
        if choice.lower() != 'y':
            break
    
    print(f"\n{Fore.GREEN}[!] Terima kasih telah menggunakan Pegasus Lacak Nomor!{Style.RESET_ALL}")
    time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[!] Program dihentikan oleh pengguna.{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Terjadi kesalahan: {str(e)}{Style.RESET_ALL}")
        sys.exit(1) 