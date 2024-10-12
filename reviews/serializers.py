from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'review_content', 'rating', 'user', 'created_date', 'slug']
        read_only_fields = ['user', 'created_date']

    def create(self, validated_data):
        # Manually assign the user
        validated_data['user'] = self.context['request'].user  
        return Review.objects.create(**validated_data)
    
    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
