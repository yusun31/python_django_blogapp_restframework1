from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # 삭제할 예정 마이그레이션 테스트 하기 위함
    # test = models.TextField()

    # Model클래스에 정의된 __str__ 함수를 재정의 (title 필드값을 리턴함)
    def __str__(self):
        return self.title +'(' + str(self.id) + ')'
    
    # published_date 필드에 현재날짜를 저장하는 메서드
    def publish(self):
        self.published_date = timezone.now()
        self.save()