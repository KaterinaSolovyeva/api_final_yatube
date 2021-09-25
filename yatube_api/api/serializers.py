from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        required=False
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        required=True,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        exclude = ('id',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        if not User.objects.filter(username=following).exists():
            raise serializers.ValidationError(
                'Такого пользователя не существует.'
            )
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя самого.'
            )
        return data
