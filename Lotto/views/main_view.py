# coding: utf-8

import ui
from  Lotto import db
from Lotto.views.user_view import User_View
from Lotto.views.test import test
from Lotto import style
import time

VIEW = {'user': User_View,
        'test': test}


class Main_Controller(object):
    
    def __init__(self):
        self.offset_y = 30
        self.view = ui.load_view('Lotto/views/main_view')
        style.set_style(self.view)
        self.current_view = VIEW['user']().view
        self.view['view1'].add_subview(self.current_view)
        
    def change_view(self,view,*args):
        self.view['view1'].remove_subview(self.current_view)
        self.current_view = VIEW[view](*args).view
        self.view['view1'].add_subview(self.current_view)
        
    def load(self):
        self.view.present('sheet')
        time.sleep(3)
        self.change_view('test')
        
view = Main_Controller()
        
if __name__ == '__main__':
    view.load()
        

        
