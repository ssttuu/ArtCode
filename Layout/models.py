from django.db import models

# Create your models here.

class Box( models.Model):
    startX = models.PositiveIntegerField()
    startY = models.PositiveIntegerField()
    sizeX = models.PositiveIntegerField()
    sizeY = models.PositiveIntegerField()

    def __unicode__(self):
        return "<{size} Box @ {position}>".format(size=(self.sizeX,self.sizeY),
                                            position=(self.startX,self.startY))

class RectangleManager( models.Manager):
    def random(self,**kwargs):
        import random
        rect = random.choice( list( super( RectangleManager, self).get_query_set().filter( **kwargs)))
        rect.selectedTotal += 1     #increment times selected
        rect.save()
        return rect

class Rectangle( models.Model):
    sizeX = models.PositiveIntegerField()
    sizeY = models.PositiveIntegerField()
    totalBoxes = models.PositiveIntegerField()
    minX = models.PositiveIntegerField()
    minY = models.PositiveIntegerField()
    maxX = models.PositiveIntegerField()
    maxY = models.PositiveIntegerField()
    selectedTotal = models.PositiveIntegerField()
    boxes = models.ManyToManyField( Box)

    objects = RectangleManager() # The default manager.

    class Meta:
        ordering = ["-totalBoxes"]

    def __unicode__(self):
        return "<{size} Rectangle w/ {total} boxes>".format( size=(self.sizeX,self.sizeY),
                                                        total=self.totalBoxes)

    def formatBoxes(self, posts=[], thumbnailUnit=20):

        thumbnail = {"width":(self.sizeX*thumbnailUnit),
                    "height":(self.sizeY*thumbnailUnit)}

        boxes = []
        for box in self.boxes.all():
            boxNormalized = {"width":box.sizeX/(self.sizeX+0.0),"height":box.sizeY/(self.sizeY+0.0),
                            "startX":box.startX/(self.sizeX+0.0),"startY":box.startY/(self.sizeY+0.0),}

            currentBox = { "width":boxNormalized["width"]*100, "height":boxNormalized["height"]*100,
                           "startX":boxNormalized["startX"]*100,"startY":boxNormalized["startY"]*100}

            currentBox["thumbnail"] = { "startX": max(thumbnail["width"]*boxNormalized["startX"],1),
                                        "startY": max(thumbnail["height"]*boxNormalized["startY"],1),
                                        "width": boxNormalized["width"]*thumbnail["width"],
                                        "height": boxNormalized["height"]*thumbnail["height"],}
            if posts:
                currentBox["post"] = posts.pop()

            boxes.append( currentBox)

        return {"boxes":boxes,"thumbnail":thumbnail}



