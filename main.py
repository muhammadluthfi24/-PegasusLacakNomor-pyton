import time
import random
from tqdm import tqdm
from colorama import init, Fore, Style

from config.settings import (
    ACTIVATION_PASSWORD, MAX_PASSWORD_ATTEMPTS,
    PROGRESS_BAR_WIDTH, LOADING_ANIMATION_DURATION,
    LOADING_ANIMATION_ITERATIONS, VALID_PHONE_PREFIX,
    NIK_LENGTH, LATITUDE_RANGE, LONGITUDE_RANGE,
    BIRTH_YEAR_RANGE
)
from data.sample_data import (
    NAMES, STREETS, CITIES, PROVINCES,
    POSTAL_CODES, GENDERS
)
from utils.helpers import (
    clear_screen, print_colored, validate_input,
    format_timestamp, handle_exception, handle_keyboard_interrupt
)

# Initialize colorama
init()

def print_banner():
    """Print the application banner."""
    banner = f"""
    {Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════╗
    ║                         PEGASUS LACAK NOMOR v1.0                          ║
    ║                     Created by: Letda Kes dr. Sobri                       ║
    ╚════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(banner)

def check_password():
    """Check activation password."""
    attempts = 0
    
    while attempts < MAX_PASSWORD_ATTEMPTS:
        password = input(f"\n{Fore.YELLOW}[!] Masukkan Password Aktivasi: {Style.RESET_ALL}")
        if password == ACTIVATION_PASSWORD:
            print_colored("[✓] Password benar!", "SUCCESS")
            time.sleep(1)
            return True
        attempts += 1
        if attempts < MAX_PASSWORD_ATTEMPTS:
            print_colored(f"\n[!] Password salah! Sisa percobaan: {MAX_PASSWORD_ATTEMPTS - attempts}", "ERROR")
        else:
            print_colored("\n[!] Maksimal percobaan terlampaui. Program berhenti.", "ERROR")
            sys.exit(1)
    return False

def loading_animation():
    """Show loading animation."""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for _ in range(LOADING_ANIMATION_ITERATIONS):
        for char in chars:
            sys.stdout.write(f"\r{Fore.CYAN}[{char}] Loading...{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(LOADING_ANIMATION_DURATION)
    print("\r" + " " * 50 + "\r", end="")

def simulate_search():
    """Simulate search process with progress bar."""
    print_colored("\n[INFO] Processing Target Data...", "INFO")
    loading_animation()
    for _ in tqdm(range(100), desc="Search Data", 
                 bar_format="{l_bar}█{bar}█{r_bar}",
                 colour="cyan", ncols=PROGRESS_BAR_WIDTH):
        time.sleep(0.03)

def generate_random_data():
    """Generate random data for demonstration."""
    return {
        "Nama": random.choice(NAMES),
        "Jenis Kelamin": random.choice(GENDERS),
        "Birthday": f"{random.randint(*BIRTH_YEAR_RANGE)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
        "Jalan": random.choice(STREETS),
        "Kota/Town": random.choice(CITIES),
        "Provinsi": random.choice(PROVINCES),
        "Kode Pos": random.choice(POSTAL_CODES),
        "Negara": "Indonesia",
        "Latitude": f"{random.uniform(*LATITUDE_RANGE):.6f}",
        "Longitude": f"{random.uniform(*LONGITUDE_RANGE):.6f}",
        "Waktu Pencarian": format_timestamp()
    }

def display_result(data):
    """Display search results."""
    print_colored("\nResult:", "SUCCESS")
    for key, value in data.items():
        if key == "Waktu Pencarian":
            print_colored(f"{key}: {value}", "WARNING")
        else:
            print_colored(f"{key}: {value}", "INFO")
    print_colored("\n[✔] Search Data complete!", "SUCCESS")

def main():
    """Main program loop."""
    clear_screen()
    print_banner()
    
    if not check_password():
        return
    
    while True:
        clear_screen()
        print_banner()
        
        target = input(f"\n{Fore.YELLOW}[?] Masukkan Nomor Telepon (08xxx) atau NIK: {Style.RESET_ALL}")
        
        if not validate_input(target, VALID_PHONE_PREFIX, NIK_LENGTH):
            time.sleep(2)
            continue
            
        simulate_search()
        result = generate_random_data()
        display_result(result)
        
        choice = input(f"\n{Fore.YELLOW}[?] Ingin mencari lagi? (y/n): {Style.RESET_ALL}")
        if choice.lower() != 'y':
            break
    
    print_colored("\n[!] Terima kasih telah menggunakan Pegasus Lacak Nomor!", "SUCCESS")
    time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()
    except Exception as e:
        handle_exception(e) 