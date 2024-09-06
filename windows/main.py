import os
from colorama import init, Fore, Back, Style

from cli import show, configfile

# ! don't change code below if you don't know what you are doing
VERSION = '1.1'
GITHUB_REPO = 'https://github.com/kerogs/pyhosts'
AUTHOR = ['Kerogs']  # Add your name here if you help
PROGRAM_NAME = "PyHosts"
ask_for_exit = True

# ! all code below can be changed

HOSTS_PATH = r'C:\Windows\System32\drivers\etc\hosts'

# Initialiser colorama
init()

class Colors:
    # Couleurs de texte
    BLUE = Fore.BLUE
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    RESET = Style.RESET_ALL

    # Couleurs de texte supplémentaires
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    WHITE = Fore.WHITE
    BLACK = Fore.BLACK

    # Couleurs de fond
    BG_BLUE = Back.BLUE
    BG_GREEN = Back.GREEN
    BG_YELLOW = Back.YELLOW
    BG_RED = Back.RED
    BG_RESET = Back.RESET

    # Text Styles
    BOLD = Style.BRIGHT
    UNDERLINE = Style.DIM

program_name_show = f"[#{Colors.BLUE}{PROGRAM_NAME}{Colors.RESET}]"
file_name_show = f"[#{Colors.YELLOW}hosts{Colors.RESET}]"

def nuke_hosts_file(hosts_path: str) -> bool:
    try:
        with open(hosts_path, 'w') as file:
            file.write("")  # Écrase tout le contenu avec rien
        return False
    except PermissionError:
        return True
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return True

def main():
    print(f"{Colors.BLUE}Welcome to {Colors.YELLOW}{PROGRAM_NAME}{Colors.RESET}")
    print(f"Version : {Colors.GREEN}{VERSION}")
    print("Author :", end=" ")
    for author in AUTHOR:
        print(f"{Colors.CYAN}{author}{Colors.RESET}", end=" ")
    print()
    print(f"REPO : {Colors.GREEN}{GITHUB_REPO}{Colors.RESET}")
    print("\n")
    
    # Boucle principale
    while True:
        # Afficher le fichier hosts
        print(f"{program_name_show} Open hosts file")
        err, content = show.display_hosts_file(HOSTS_PATH)
        
        if err:
            print(f"{Colors.BG_RED}{Colors.RED}{content}{Colors.RESET}")
        else:
            print(content)
        
        # Demander à l'utilisateur quelle action il veut effectuer
        print("\n")
        action = input(f"{program_name_show} Would you like to add, remove, nuke (wipe out) the file, or quit? (add/remove/nuke/quit) : ").strip().lower()
        
        if action == 'add':
            line_to_add_url = input(f"{program_name_show} Please enter new URL (e.g., www.kslabs.fr or kslabs.fr): ").strip()
            line_to_add_ip = input(f"{program_name_show} Please enter new IP (e.g., 127.0.0.1): ").strip()
            error = configfile.add_line_to_hosts(HOSTS_PATH, line_to_add_url, line_to_add_ip)
            if error:
                print(f"{Colors.BG_RED}Error while adding a line.{Colors.RESET}")
            else:
                print(f"{program_name_show}{Colors.GREEN} Line added.{Colors.RESET}")
        
        elif action == 'remove':
            line_to_remove = input(f"{program_name_show} Please enter the line to remove: ").strip()
            error = configfile.remove_line_from_hosts(HOSTS_PATH, line_to_remove)
            if error:
                print(f"{Colors.BG_RED}Error while removing a line.{Colors.RESET}")
            else:
                print(f"{program_name_show}{Colors.GREEN} Line removed.{Colors.RESET}")
        
        elif action == 'nuke':
            confirm = input(f"{program_name_show} {Colors.RED}Are you sure you want to wipe out the entire hosts file? This action cannot be undone! (yes/no) : {Colors.RESET}").strip().lower()
            if confirm == 'yes':
                error = nuke_hosts_file(HOSTS_PATH)
                if error:
                    print(f"{Colors.BG_RED}Error while nuking the file.{Colors.RESET}")
                else:
                    print(f"{program_name_show}{Colors.GREEN} File wiped out successfully.{Colors.RESET}")
            else:
                print(f"{program_name_show}{Colors.YELLOW} Nuke operation cancelled.{Colors.RESET}")
        
        elif action == 'quit':
            print(f"{program_name_show} {Colors.GREEN}Exiting program.{Colors.RESET}")
            ask_for_exit = False
            break  # Sortir de la boucle et terminer le programme
        
        else:
            print(f"{program_name_show} {Colors.RED}Invalid action.{Colors.RESET}")
        
        # Afficher à nouveau le fichier hosts mis à jour
        print(f"{program_name_show} Open hosts file to show update")
        err, content = show.display_hosts_file(HOSTS_PATH)
        
        if err:
            print(f"{Colors.BG_RED}{Colors.RED}{content}{Colors.RESET}")
        else:
            print(content)
        
        print("\n")

if __name__ == '__main__':
    main()

    if ask_for_exit:
        print("\n")
        input(f"{Colors.BG_BLUE}Press Enter to exit...{Colors.RESET}")
