from rest_framework import serializers
from .models import Book, Author

#base serializer
class BookPlainSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    published_date = serializers.DateField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance
    
        
#modelserializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

#modelserializer
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']

#hyperlinkedmodelserializer
class BookHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author', 'published_date']

#listserializer
class BookBulkCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)

class BookBulkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        list_serializer_class = BookBulkCreateListSerializer

#nested serializer
class AuthorNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class BookNestedAuthorSerializer(serializers.ModelSerializer):
    author = AuthorNestedSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        return Book.objects.create(author=author, **validated_data)

#related field serializers
class BookWithStringRelatedFieldSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']

class BookWithPKRelatedFieldSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']

class BookWithSlugRelatedFieldSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
