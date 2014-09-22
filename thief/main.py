'''
Created on Sep 19, 2014

@author: Lupi
'''
import libtcodpy as tcod




SHEI = 50
SWID = 80
LIMFPS = 20

class MapObj():
    #generic map object (pc, npc, items, anything that's drawn on the screen)
    
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
    def move(self, dx, dy):
        # adds a positive or negative value to the object's coordinates
        self.x += dx
        self.y += dy
    def draw(self):
        #set the color and then draw on the console at x and y
        tcod.console_set_default_foreground(con, self.color)
        tcod.console_put_char(con, self.x, self.y, self.char, tcod.BKGND_NONE)
    def clear(self):
        tcod.console_put_char(con, self.x, self.y, ' ', tcod.BKGND_NONE)

class Tile():
    #tile of the map and properties
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
        #if a tile is blocked, it blocks sight by default
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight
        
 
def handle_keys():
    global p    
    key = tcod.console_wait_for_keypress(True)
    if key.vk == tcod.KEY_ENTER and tcod.KEY_ALT:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
    elif  key.vk == tcod.KEY_ESCAPE:
        return True
    
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        p.move(0, -1)
    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        p.move(0, 1)
    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        p.move(-1, 0)
    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        p.move(1, 0)    


tcod.console_set_custom_font("prestige12x12_gs_tc.png", tcod.FONT_TYPE_GREYSCALE|tcod.FONT_LAYOUT_TCOD)
tcod.console_init_root(SWID, SHEI, "Thief RL Prototype")
con = tcod.console_new(SWID, SHEI)
#player
p = MapObj(SWID/2, SHEI/2, '@', tcod.white)
#npc
npc = MapObj(SWID/2 - 5, SHEI/2, '@', tcod.yellow)
#object list
os = [p, npc]

while not tcod.console_is_window_closed():
    for o in os:
        o.draw()
        
    tcod.console_blit(con, 0, 0, SWID, SHEI, 0, 0, 0)
    tcod.console_flush()
    for o in os:
        o.clear()
    if handle_keys():
        break
     