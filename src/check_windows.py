import subprocess

def check_firewall():
    """Checa se o firewall do Windows está habilitado."""
    try:
        r = subprocess.run(["netsh","advfirewall","show","allprofiles"], capture_output=True, text=True, check=False)
        return "ON" in r.stdout.upper(), r.stdout
    except FileNotFoundError:
        return False, "netsh não disponível"

def check_services():
    """Checa se o serviço de Windows Update está rodando."""
    try:
        r = subprocess.run(["sc","query","wuauserv"], capture_output=True, text=True)
        return "RUNNING" in r.stdout.upper(), r.stdout
    except Exception as e:
        return False, str(e)
