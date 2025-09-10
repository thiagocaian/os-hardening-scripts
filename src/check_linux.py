import subprocess

def check_firewall():
    """Verifica se o firewall (ufw ou firewalld) está ativo no Linux."""
    try:
        r = subprocess.run(["ufw", "status"], capture_output=True, text=True, check=False)
        if "Status: active" in r.stdout:
            return True, "ufw ativo"
        r = subprocess.run(["systemctl", "is-active", "firewalld"], capture_output=True, text=True)
        return r.stdout.strip() == "active", "firewalld ativo"
    except FileNotFoundError:
        return False, "Firewall não encontrado"

def check_shadow_permissions():
    """Verifica se /etc/shadow possui permissões seguras (-rw-------)."""
    try:
        r = subprocess.run(["ls", "-l", "/etc/shadow"], capture_output=True, text=True)
        return r.stdout.startswith("-rw-------"), r.stdout.strip()
    except Exception as e:
        return False, str(e)
