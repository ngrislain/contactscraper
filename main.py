#!/usr/bin/python
# -*- coding:utf8 -*-
import app
import time
import curses

class ContactApp(app.App):
    def main(self):        
#         d = app.Menu(self.stdscr, 'Please validate the entry', [
#             #app.Item('OK', ['hjk', 'ghj'])
#             "hello"
#             ])
        
#         d = app.Item(self.stdscr, 'Prénom', ['Nicolas', 'Tancrede'], 2, action=lambda i:self.stdscr.addstr('n'))
        menu = app.Menu(self.stdscr, 'Validate entry', (
                ('Name', ['Nicolas', 'Tancrede']),
                ('City', ['Paris', 'Bordeaux'])
                ))
        
        quit = False
        while(not quit):
            valid = False
            while(not (valid or quit)):
                menu.display(self.stdscr, True)
                key = self.stdscr.getch()
                menu.event(key)
                self.stdscr.refresh()
                quit = key==ord('q')
                valid = key==curses.KEY_ENTER

if __name__ == '__main__':
    print "Starting the main loop"
    app = ContactApp().start()
    