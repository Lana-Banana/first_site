from django.db import models

# DB에 어떤 자료를 어떻게 저장할 것인가 결정
# 각 모델에 관련된 기능들을 만드는 부분
# Create your models here.

# models 클래스를 상속받아서 작성
# ORM : 클래스 객체를 만들어서 DB 처리, 쿼리 안만들고 클래스로 묘사만 하면 알아서 되도록..

class Bookmark(models.Model):
    # fields (컬럼 작성)
    # 필드 이름 = 필드 종류 (
    # 1. db에 어떤식으로 저장할래? dataType
    # 2. 사용자의 입력을 받을때 어떤 form tag를 보여줄 것인지)
    # 2-1. 입력폼 밸리데이션도 자동으로 된다.
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')  # ('label')

    class Meta:
        # 오름차순 정렬 (내림차순은 - 를 붙여줌 ['-site_name']
        ordering = ['site_name']

    # 객체 출력 정의 (toString())
    def __str__(self):
        return "사이트이름 : " + self.site_name

    def get_absolute_url(self):
        pass




