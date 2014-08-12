# coding: utf-8

import ui
import db

class Main_Controller(ui.View):
    def __init__(self):
        self.present('sheet')
        
    def did_load(self):
        users = db.list_users()
        tbl = []
        for user in users:
            itm = {}
            print user
            itm['title'] = '%s  %s %s' % (user['name'],user['balance'],user['won'])
            itm['accessory_type'] = 'detail_button'
            tbl.append(itm)
        lst1 = ui.ListDataSource(tbl)
        self['user_view'].data_source = lst1
        self['user_view'].delegate = lst1
        self['user_view'].editing = False
        lst1.font = ('Courier',14)
        lst1.accessory_action = self.table_tapped
        #lst1.action = table1_tapped
        lst1.delete_enabled = False 
        
    def table_tapped(self,sender):
        print sender.items[sender.tapped_accessory_row]
        
if __name__ == '__main__':
    ui.load_view()
        

        
