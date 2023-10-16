from rest_framework import serializers

from question_library.models import (
    Category,
    VideoEntry,
    VideoType,
    HomePage,
    HomePageInformationCard,
)


class VideoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoType
        fields = "__all__"


class VideoEntrySerializer(serializers.ModelSerializer):
    video_types = VideoTypeSerializer(many=True, read_only=True)

    class Meta:
        model = VideoEntry
        fields = [
            "id",
            "title",
            "author",
            "questions",
            "video_url",
            "video_embed_url",
            "views",
            "language",
            "youtube_id",
            "yt_channel_title",
            "yt_publish_time",
            "duration",
            "video_types",
            "thumbnail_url",
        ]


class CategorySerializer(serializers.ModelSerializer):
    video_entries = VideoEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "full_name", "description", "video_entries", "keywords"]
        lookup_field = "name"


class HomePageInformationCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageInformationCard
        fields = "__all__"


class HomePageSerializer(serializers.ModelSerializer):
    month_category = CategorySerializer(read_only=True)
    highlighted_video = VideoEntrySerializer(read_only=True)
    information_cards = HomePageInformationCardSerializer(many=True, read_only=True)

    class Meta:
        model = HomePage
        fields = "__all__"
