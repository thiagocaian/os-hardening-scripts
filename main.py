import platform
from datetime import datetime
from typing import Tuple

from src import check_linux, check_macos, check_windows

def line(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def show_result(name: str, result: Tuple[bool, str]) -> None:
    ok, msg = result
    status = "✅ OK" if ok else "❌ FAIL"
    print(f"[{status}] {name} -> {msg}")

def run_linux():
    line("Linux hardening quick checks")
    show_result("Firewall (ufw/firewalld)", check_linux.check_firewall())
    show_result("/etc/shadow permissions", check_linux.check_shadow_permissions())

def run_macos():
    line("macOS hardening quick checks")
    show_result("FileVault", check_macos.check_filevault())
    show_result("Firewall", check_macos.check_firewall())

def run_windows():
    line("Windows hardening quick checks")
    show_result("Firewall", check_windows.check_firewall())
    show_result("Windows Update service", check_windows.check_services())

def auto():
    osname = platform.system().lower()
    line(f"Auto-detect mode: {platform.system()} @ {datetime.now().isoformat(timespec='seconds')}")
    if osname == "linux":
        run_linux()
    elif osname == "darwin":
        run_macos()
    elif osname == "windows":
        run_windows()
    else:
        print(f"Sistema não suportado: {platform.system()}")

def menu():
    while True:
        print("\n== OS Hardening Quick Menu ==")
        print("1) Auto (detectar SO atual)")
        print("2) Linux checks")
        print("3) macOS checks")
        print("4) Windows checks")
        print("0) Sair")
        choice = input("Escolha: ").strip()
        if choice == "1":
            auto()
        elif choice == "2":
            run_linux()
        elif choice == "3":
            run_macos()
        elif choice == "4":
            run_windows()
        elif choice == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
