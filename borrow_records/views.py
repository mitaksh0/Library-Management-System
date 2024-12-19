from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BorrowRecord
from books.models import Book
from .serializers import BorrowRecordSerializer
from django.utils import timezone


@api_view(['GET','POST'])
def borrow_book(request):        

    if request.method == 'GET':
        borrow_records = BorrowRecord.objects.all()
        serializer = BorrowRecordSerializer(borrow_records, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # print(request.data)
        serializer = BorrowRecordSerializer(data=request.data)

        if serializer.is_valid():
            book = serializer.validated_data['book']
            book = Book.objects.get(id=book.id)
            book.available_copies -= 1

            book.save() # save book into database
            serializer.save() # save borrowed_record into database
            
        return Response(serializer.data)



@api_view(['GET', 'PUT'])
def return_borrow(request, id):
    if request.method == 'GET':
        return Response({"message": "only PUT allowed"})
    elif request.method == 'PUT':
        print(request.data)
        borrow_record = BorrowRecord.objects.get(book=id)
        borrow_record.return_date = timezone.now()

        serializer = BorrowRecordSerializer(borrow_record, data=request.data)
        # if serializer.is_valid(raise_exception=True):
        book = Book.objects.get(id=id)
        book.available_copies += 1
        book.save()
        borrow_record.save()

        return Response(serializer.data)