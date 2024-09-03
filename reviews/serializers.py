from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()
    job_title = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'created_at','user','job' ,'user_username', 'job_title']
        

    def get_user_username(self, obj):
        return obj.user.username

    def get_job_title(self, obj):
        return obj.job.title