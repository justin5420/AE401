from mcpi.minecraft import Minecraft
mc=Minecraft.create()
 
x,y,z=mc.player.getTilePos()

import random
for i in range(2000):
    r = random.randrange(1,5)
    if r== 1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x=x+4
    if r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x =x-4
    if r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z = z+4
    if r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z = z-4
        
        















