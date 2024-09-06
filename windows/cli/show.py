from typing import Tuple

def display_hosts_file(hosts_path: str) -> Tuple[bool, str]:
    try:
        with open(hosts_path, 'r') as file:
            content = file.read().strip()  # Supprime les espaces ou les sauts de ligne inutiles
        if not content:  # Si le contenu est vide
            return True, "[empty file]"
        return False, content  # Sinon, retourne le contenu normal
    except PermissionError:
        return True, "Error: You must run this script with administrative privileges."
    except Exception as e:
        return True, f"An error has occurred: {e}"

