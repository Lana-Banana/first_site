from django.contrib import admin

# 작성한 모델을 관리자페이지에서 다룰수 있도록 등록
# 모델을 다루는데 관련된 옵션값을 설정
# Register your models here.

# .models : 현재 app 의 모델중
from .models import Bookmark

admin.site.register(Bookmark)