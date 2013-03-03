
import sys
sys.path.append( "/home/stupschwartz/")

from ArtCode.Layout.models import Box,Rectangle

import generateLayout
import time

iii = 0

def main(w,h):
    global iii
    generateLayout.Rectangle.solve(w,h)

    for s in generateLayout.Rectangle.solutions[(w,h)]:
        boxes = []
        for box in s.boxes:
            newBox = Box.objects.filter(startX=box.start[0], startY=box.start[1],
                                    sizeX=box.size[0],sizeY=box.size[1])
            if newBox:
                box = newBox[0]
            else:
                box = Box(startX=box.start[0], startY=box.start[1],
                                    sizeX=box.size[0],sizeY=box.size[1])
                box.save()
            boxes.append( box)

        #newRect = Rectangle.objects.filter(sizeX=s.width, sizeY=s.height, totalBoxes=s.stats['total'],
        #                minX=s.stats['minX'], minY=s.stats['minY'], maxX=s.stats['maxX'],
        #                maxY=s.stats['maxY'], selectedTotal=0)
        #if newRect:
        #    rect = newRect[0]
        #else:
        rect = Rectangle( sizeX=s.width, sizeY=s.height, totalBoxes=s.stats['total'],
                        minX=s.stats['minX'], minY=s.stats['minY'], maxX=s.stats['maxX'],
                        maxY=s.stats['maxY'], selectedTotal=0)
        rect.save()
        rect.boxes.add( *boxes)
        rect.save()
        iii+=1
        if iii % 100 == 0:
            print "added the %sth at %s" % (iii, time.time())



if __name__ == "__main__":
    main(4,3)
    #main(3,4)
    #main(4,4)
    #b = Box( startX=0,startY=0, sizeX=4,sizeY=3)
    #b.save()
    print Box.objects.all()
    print Rectangle.objects.all()