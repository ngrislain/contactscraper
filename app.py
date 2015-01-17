#!/usr/bin/python
# -*- coding:utf8 -*-
import curses
import traceback
from numpy import rank

# Global constants
NORMAL = 1
ACTIVE = 2

class Displayable(object):
    def __init__(self, window, x, y, w, h):
        self.w = w
        self.h = h
        self.window = window.derwin(h, w, y, x)
    def display(self, window, active=False):
        self.window.clear()
        self.window.refresh()

class EventProcessor(object):
    def event(self, key):
        pass

class Menu(Displayable, EventProcessor):
    def __init__(self, window, name, values, default_index=0, action=lambda i:None):
        h, w = window.getmaxyx()
        marg_w = int(w*0.2)
        marg_h = int(h*0.2)
        Displayable.__init__(self, window, marg_w/2, marg_h/2, w-marg_w, h-marg_h)
        self.name = name
        self.values = []
        for i in xrange(len(values)):
            self.values.append(Item(self.window, values[i][0], values[i][1], 1+i))
        self.index = default_index%len(self.values)
        self.action = action
    # display the menu
    def display(self, window, active=False):
        self.window.clear()
        self.window.bkgd(' ', curses.color_pair(NORMAL)|curses.A_BOLD)
        self.window.addnstr(0, self.w/2-len(self.name)/2, self.name, self.w)
        for i in xrange(len(self.values)):
            if i==self.index:
                self.values[i].display(window, active=True)
            else:
                self.values[i].display(window)
        self.window.refresh()
    
    # process the events
    def event(self, key):
        self.values[self.index].event(key)
        if key == curses.KEY_UP:
            self.index = (self.index-1)%len(self.values)
        elif key == curses.KEY_DOWN: 
            self.index = (self.index+1)%len(self.values)

class Item(Displayable, EventProcessor):
    def __init__(self, window, name, values, rank, name_w=16, default_index=0, action=lambda i:None):
        h, w = window.getmaxyx()
        Displayable.__init__(self, window, 0, rank, w, 1)
        self.name = name
        self.values = values
        self.name_w = name_w
        self.index = default_index
        self.action = action
    # display the menu
    def display(self, window, active=False):
        self.window.clear()
        if active:
            self.window.bkgd(' ', curses.color_pair(ACTIVE))
        else:
            self.window.bkgd(' ', curses.color_pair(NORMAL))
        self.window.addnstr(0, 0, self.name, self.name_w)
        self.window.addnstr(0, self.name_w, self.values[self.index], self.name_w)
        self.window.refresh()
    # process the events
    def event(self, key):
        if key == curses.KEY_LEFT:
            self.index = (self.index-1)%len(self.values)
        elif key == curses.KEY_RIGHT: 
            self.index = (self.index+1)%len(self.values)
        self.action(self.index)

# A class of curses application
class App(object):
    
    # An abstract method
    def main(self):
        pass
    
    def init_color(self):
        curses.start_color()
        curses.init_pair(NORMAL, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(ACTIVE, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    
    def start(self):
        try:
            # Initialize curses
            self.stdscr = curses.initscr()
            # Get some convenient values
            self.h, self.w = self.stdscr.getmaxyx()
            # Turn off echoing of keys, and enter cbreak mode,
            # where no buffering is performed on keyboard input
            curses.noecho()
            curses.cbreak()
            # Init colors
            self.init_color()
            # In keypad mode, escape sequences for special keys
            # (like the cursor keys) will be interpreted and
            # a special value like curses.KEY_LEFT will be returned
            self.stdscr.keypad(1)
            self.main()  # Enter the main loop
            # Set everything back to normal
            self.stdscr.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()  # Terminate curses
        except:
            # In event of error, restore terminal to sane state.
            self.stdscr.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
            print "The program exited abnormally"
            traceback.print_exc()
        return self
