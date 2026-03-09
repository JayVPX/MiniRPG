from paths.magePath import *
from methods import mage_path
from methods import rogue_path
from methods import warrior_path
from methods import intro
from methods import select_class
from utils import logout



def main():
    intro()

    classe = select_class()


    if classe == "1":
        mage_path()

    elif classe == "2":
        rogue_path()

    elif classe == "3":
        warrior_path()
    else: 
        logout()

if __name__ == "__main__":
    main()