# coding: utf-8

import ui
from Lotto import db
from Lotto import style

class User_View(object):
    
    def __init__(self):
        self.offset_y = 30
        self.view = ui.load_view('Lotto/views/user_view')
        #style.set_style(self.view)
        users = db.list_users()
        tbl = []
        
        y = 75
        x = 25
        for user in users:
            self.add_button(user,x,y)
            self.add_number(user,x+100,y)
            y += self.offset_y
            
        #self.view.present('sheet')
        
    def add_button(self,user,x,y):
        btn = ui.Button()
        btn.x = x
        btn.y = y
        y += self.offset_y
        btn.width = 100
        btn.height = 14
        btn.name = str(user['_id'])
        btn.title = user['name']
        btn.action = self.button_pressed
        self.view.add_subview(btn)
        
    def add_number(self,user,x,y):
        lbl = ui.Label()
        lbl.text = user['number']
        lbl.x = x
        lbl.y = y
        lbl.width = 125
        lbl.height = 14
        self.view.add_subview(lbl)
        
    def button_pressed(self,sender):
        print sender.name
        
        
if __name__ == '__main__':
    Main_Controller()
        

        
