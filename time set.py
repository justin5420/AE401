from mcpi.minecraft import Minecraft
mc=Minecraft.create()
 
x,y,z=mc.player.getTilePos()
import time
while True:
    mc.executeCommand("time add 50")
   # time.sleep(0.05)