from colorama import Fore, Style

def hello_world(size: int = 3):
    o_s = "o" * size
    i_s = "i" * size
    print(Fore.CYAN +f"Hello y{o_s}u" + Style.RESET_ALL)
    print(Fore.BLUE + f"Have a n{i_s}ce day ! :)" + Style.RESET_ALL)

if __name__ == "__main__":
    hello_world()
