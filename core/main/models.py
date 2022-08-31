from distutils.command.upload import upload
from django.db import models

# Create your models here.


class IndexBg(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    img = models.ImageField('img', upload_to='media')
    
    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'IndexBg'
        verbose_name_plural = 'IndexBgs'
    
class IndexAbout(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    about2 = models.TextField('about2', null= True)
    img = models.ImageField('img', upload_to='media')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'IndexAbout'
        verbose_name_plural = 'IndexAbouts'
    
    
class IndexBest(models.Model):
    name = models.CharField('name', max_length=40)
    about = models.TextField('about')
    img = models.ImageField('img', upload_to='media')
    
    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = 'IndexBest'
        verbose_name_plural = 'IndexBests'
        
class IndexDream(models.Model):
    img = models.ImageField('img', upload_to='media')
    img2 = models.ImageField('img2', upload_to='media')
    img3 = models.ImageField('img3', upload_to='media')
    img4 = models.ImageField('img4', upload_to='media')
    
    def __img__(self):
        return self.img   
    class Meta:
        verbose_name = 'IndexDream'
        verbose_name_plural = 'IndexDreams'
        
class IndexLot(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'IndexLot'
        verbose_name_plural = 'IndexLots'
        
class IndexLot2(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    inte = models.IntegerField('int')
     
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'IndexLot2t'
        verbose_name_plural = 'IndexLot2s'
        
class IndexLot3(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    inte = models.IntegerField('int')
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'IndexLot3'
        verbose_name_plural = 'IndexLot3s'   
        
class IndexSlayd(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    img = models.ImageField('img', upload_to='media') 
    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name = ' IndexSlayd'
        verbose_name_plural = ' IndexSlayds'

class IndexTrend(models.Model):
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    img = models.ImageField('img', upload_to='media') 
    
    
    def __str__(self):
        return self.name2    
    
    class Meta:
        verbose_name = ' IndexTrend'
        verbose_name_plural = ' IndexTrends'
        
class IndexDesigner(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    img = models.ImageField('img', upload_to='media')
    
    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = 'IndexDesigner'
        verbose_name_plural = 'IndexDesigners'
        
class IndexBlog(models.Model):
    name = models.CharField('name', max_length=120)
    name2 = models.CharField('name2', max_length=120)
    name3 = models.CharField('name3', max_length=120)
    name4 = models.CharField('name4', max_length=120)
    name5 = models.CharField('name5', max_length=120)
    img = models.ImageField('img', upload_to='media')
    img2 = models.ImageField('img2', upload_to='media')
    
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name = 'IndexBlog'
        verbose_name_plural = 'IndexBlogs'
# About    
    
class AboutBg(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    about2 = models.TextField('about2', null= True)

    img = models.ImageField('img', upload_to='media')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'AboutBg'
        verbose_name_plural = 'AboutBgs'
    
class AboutDesigner(models.Model):
    name = models.CharField('name', max_length=40)
    name2 = models.CharField('name2', max_length=40)
    about = models.TextField('about')
    img = models.ImageField('img', upload_to='media')
    
    def __str__(self):
        return self.name    
    class Meta:
        verbose_name = 'AboutDesigner'
        verbose_name_plural = 'AboutDesigners'
# Blog


class Blog1(models.Model):
    name = models.CharField('name', max_length=120)
    name2 = models.CharField('name2', max_length=120)
    name3 = models.CharField('name3', max_length=120)
    name4 = models.CharField('name4',max_length=120)
    name5 = models.CharField('name5',max_length=120)
    img = models.ImageField('img', upload_to='media')
    img2 = models.ImageField('img2', upload_to='media')
    
    def __str__(self):
        return self.name   
    class Meta:
        verbose_name = 'Blog1'
        verbose_name_plural = 'Blog1s'
        
class Blog2(models.Model):
    name = models.CharField('name', max_length=120)
    name2 = models.CharField('name2', max_length=120)
    name3 = models.CharField('name3', max_length=120)
    name4 = models.CharField('name4', max_length=120)
    name5 = models.CharField('name5', max_length=120)
    img = models.ImageField('img', upload_to='media')
    img2 = models.ImageField('img2', upload_to='media')
    
    def __str__(self):
        return self.name   
    class Meta:
        verbose_name = 'Blog2'
        verbose_name_plural = 'Blog2s'

class Logo(models.Model):
    img = models.ImageField('img', upload_to = 'media')

    def __img__(self):
        return self.img  
    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'



class Instagram(models.Model):
    img = models.ImageField('img', upload_to = 'media')
    img2 = models.ImageField('img2', upload_to = 'media')
    img3 = models.ImageField('img3', upload_to = 'media')
    img4 = models.ImageField('img4', upload_to = 'media')
    img5 = models.ImageField('img5', upload_to = 'media')
    img6 = models.ImageField('img6', upload_to = 'media')

    def __img__(self):
        return self.img  
    class Meta:
        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagrames'
