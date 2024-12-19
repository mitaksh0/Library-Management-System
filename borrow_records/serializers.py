from rest_framework import serializers
from .models import BorrowRecord
from books.models import Book

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = '__all__'

    # books validation check
    def validate_book(self, value):
        try:
            # make get query for given book id
            if isinstance(value, Book):
                book_id = value.id  # Access the 'id' of the Book instance
            else:
                book_id = value  # If it's already an ID, use it directly
            book = Book.objects.get(id=book_id)
            
            # check if book in stock
            if book.available_copies <= 0:
                raise serializers.ValidationError("book not in stock")

        except Book.DoesNotExist:
            # book not in database
            raise serializers.ValidationError("book not found")
        
        except Exception as error:
            print(error)
            raise serializers.ValidationError(error)
    
        return value