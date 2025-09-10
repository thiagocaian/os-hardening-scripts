import subprocess

def check_filevault():
    """Verifica se o FileVault está habilitado no macOS."""
    try:
        r = subprocess.run(["fdesetup","status"], capture_output=True, text=True)
        return "FileVault is On" in r.stdout, r.stdout.strip()
    except FileNotFoundError:
        return False, "fdesetup não encontrado"

def check_firewall():
    """Verifica se o firewall do macOS está ativo."""
    try:
        r = subprocess.run(["/usr/libexec/ApplicationFirewall/socketfilterfw","--getglobalstate"], capture_output=True, text=True)
        return "enabled" in r.stdout.lower(), r.stdout.strip()
    except FileNotFoundError:
        return False, "socketfilterfw não encontrado"
