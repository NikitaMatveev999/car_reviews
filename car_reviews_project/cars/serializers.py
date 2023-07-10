from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment


class ManufacturerSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    cars = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'cars', 'comment_count']

    def get_cars(self, instance):
        cars = Car.objects.filter(manufacturer=instance)
        serializer = CarSerializer(cars, many=True)
        return serializer.data

    def get_comment_count(self, instance):
        cars = Car.objects.filter(manufacturer=instance)
        comment_count = Comment.objects.filter(car__in=cars).count()
        return comment_count


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = serializers.StringRelatedField(many=True, read_only=True, source='manufacturer_set')

    class Meta:
        model = Country
        fields = ['id', 'name', 'manufacturers']

    def get_manufacturers(self, instance):
        manufacturers = Manufacturer.objects.filter(country=instance)
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return serializer.data


class CarSerializer(serializers.ModelSerializer):
    manufacturer = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'manufacturer', 'comments', 'comment_count']

    def get_comments(self, instance):
        comments = Comment.objects.filter(car=instance)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_comment_count(self, instance):
        return instance.comment_set.count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author_email', 'car', 'created_date', 'comment']
