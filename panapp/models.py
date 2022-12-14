from django.db import models
import cv2
from .utils import get_computedagain
from django.conf import settings



class PanCard(models.Model):
    pan_url = models.URLField(max_length=500)
    #pan_id=models.CharField(max_length=50)
    pan_details=models.CharField(max_length=250)
    #filename = settings.MEDIA_ROOT + image.name
    

    # def user_directory_path(self, instance, filename, *args, **kwargs):
    #     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #     self.filename = settings.MEDIA_ROOT + self.image.name
    #     super(PanCard, self).user_directory_path(*args, **kwargs)

    #     return 'user_{0}/{1}'.format(instance.user.id, filename)   
    
    def __str__(self):
        return str(self.id)
    

    # def get_computed(self):
    #     img = cv2.imread(self.image)
    #     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #     mypan=pytesseract.image_to_string(img, lang ="eng+hin")
    #     l=[]
    #     l=mypan.splitlines()
    #     for i in len(l):
    #         if(bool(re.match('((?=.*\d)(?=.*[A-Z]).{10})', l[i]))==True):
    #             self.pan_id=l[i]
    #     return self.pan_id
    
    # def get_computedagain(self):
    #     img = cv2.imread(self.image)
    #     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #     mypan=pytesseract.image_to_string(img, lang ="eng+hin")
    #     self.pan_details=mypan
    #     return self.pan_details

    def save(self, *args, **kwargs):
        cap = cv2.VideoCapture(self.pan_url)
        success, img = cap.read()
        if success:
            #self.pan_id = get_computed(img)
            self.pan_details=get_computedagain(img)
        
        super(PanCard, self).save(*args, **kwargs)
        
        