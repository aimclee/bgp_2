from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'images/') 
    # images 디렉토리를 만들고 settings.py에서 MEDIA_URL과 MEDIA_ROOT 경로 바로 아래에 위치해 있을건데, 여기에 파일을 넣을 것.
    # image를 올리고 싶다면 pip install pillow를 통해 pip을 설치해야함.
    
    description = models.CharField(max_length = 500)

    def __str__(self): # admin 사이트에 제목영역에 title이 뜨기를 원하기 때문에 이 코드를 작성함.
        return self.title