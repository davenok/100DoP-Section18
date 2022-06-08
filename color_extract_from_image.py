import colorgram
from pprint import pprint

colors = colorgram.extract('22328162_master.jpg', 30)
#pprint.pprint(colors)

color_list = []

for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
    
pprint(color_list)