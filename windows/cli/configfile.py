def add_line_to_hosts(hosts_path: str, url: str, ip: str) -> bool:
    line_to_add = f"{ip} {url}"
    try:
        with open(hosts_path, 'a') as file:
            file.write(f"{line_to_add}\n")
        return False  # Aucune erreur
    except PermissionError:
        print("Erreur : You must run this script with administrative privileges.")
        return True
    except Exception as e:
        print(f"An error has occurred : {e}")
        return True


def remove_line_from_hosts(hosts_path: str, line_to_remove: str) -> bool:
    try:
        # Lire le fichier hosts
        with open(hosts_path, 'r') as file:
            lines = file.readlines()
        
        # Vérifier si la ligne existe et la retirer si présente
        new_lines = [line for line in lines if line.strip() != line_to_remove.strip()]
        
        # Si la ligne n'existe pas, retourner une erreur
        if len(new_lines) == len(lines):
            print(f"The line '{line_to_remove}' does not exist in the hosts file.")
            return True

        # Réécrire le fichier sans la ligne
        with open(hosts_path, 'w') as file:
            file.writelines(new_lines)
        
        return False  # Aucun problème
    except PermissionError:
        print("Error : You must run this script with administrative privileges.")
        return True
    except Exception as e:
        print(f"An error has occurred when removing the line : {e}")
        return True

