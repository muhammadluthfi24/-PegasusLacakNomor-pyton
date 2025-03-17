import os
import sys
from datetime import datetime
from colorama import Fore, Style
from config.settings import COLORS

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(message, color_type="INFO"):
    """Print a colored message to the console."""
    color = getattr(Fore, COLORS.get(color_type, "WHITE").upper())
    print(f"{color}{message}{Style.RESET_ALL}")

def validate_input(target, valid_prefix, nik_length):
    """Validate phone number or NIK input."""
    if not target:
        print_colored("\n[!] Input tidak boleh kosong!", "ERROR")
        return False
        
    if not (target.startswith(valid_prefix) or len(target) == nik_length):
        print_colored("\n[!] Format nomor telepon atau NIK tidak valid!", "ERROR")
        return False
        
    return True

def format_timestamp():
    """Get current timestamp in formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def handle_exception(e):
    """Handle exceptions and print error message."""
    print_colored(f"\n[!] Terjadi kesalahan: {str(e)}", "ERROR")
    sys.exit(1)

def handle_keyboard_interrupt():
    """Handle keyboard interrupt (Ctrl+C)."""
    print_colored("\n\n[!] Program dihentikan oleh pengguna.", "WARNING")
    sys.exit(0) 