import os
import sys
import pickle
sys.path.append('D:\pycharmworkspace\ecosim')
from main.economy import *

class Console():
    def __init__(self):
        self.begin()


    def begin(self):
        self.loadGame()
        if Game.save['firsttime']:
            Game.setDefParams(Game)
            self.setMarket()
            self.saveGame()
        self.printMain()

    def cmds(self):
        print(txt_help)
        self.cmds_sess = True
        while self.cmds_sess:
            cmd_ = input().lower()
            cmd = cmd_.split(' ')
            cmd.append('')
            if cmd[0] == 'help':
                print(cmds_gen)
            elif cmd[0] == 'exit':
                print('Exiting..')
                self.saveGame()
                break
            elif cmd[0] == 'del_saves':
                self.delSaves()
            elif cmd[0] == 'save':
                self.saveGame()

    def setMarket(self):
        for x in range(len(products)):
            Game.product_vals.append(Game.Product(products[x],defprices[x],(x+1)))

    def printMain(self):
        print(interface_main_tab)
        for pro in Game.product_vals:
            print(interface_main_mid.format(pro.id,pro.name, pro.price))
        print(interface_main_tab)


    def loadGame(self):
        try:
            with open('save', 'rb') as input:
                Game.save = pickle.load(input)
            with open('product_vals', 'rb') as input:
                Game.product_vals = pickle.load(input)
        except IOError:
            print(txt_load_fail)
            pass

    def saveGame(self):
        try:
            with open('save', 'wb') as op:
                pickle.dump(Game.save, op, pickle.HIGHEST_PROTOCOL)
            with open('product_vals', 'wb') as op:
                pickle.dump(Game.product_vals, op, pickle.HIGHEST_PROTOCOL)
        except IOError:
            print(txt_save_fail)
            pass

    def delSaves(self):
        os.remove('save')
        os.remove('product_vals')
        self.cmds_sess = False



if __name__ == '__main__':
    app = Console()