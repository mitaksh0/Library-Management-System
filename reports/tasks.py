import json
import os
from celery import shared_task
from authors.models import Author
from books.models import Book
from borrow_records.models import BorrowRecord
from datetime import datetime


# file_path = os.path.join(os.path.dirname(__file__), 'report.json')
dir_path = os.path.join(os.path.dirname(__file__), 'data')

@shared_task
def store_report():
    authors = Author.objects.count()
    books = Book.objects.count()
    borrowed_count = BorrowRecord.objects.filter(return_date__isnull=True).count()

    # Get the current date and time
    current_date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    data = {
        "books_count": books,
        "authors_count": authors,
        "borrowed_books_count": borrowed_count,
        "generated_at": current_date_time,
    }

    file_path = os.path.join(dir_path, current_date_time + ".json")
     # Save the random text in a JSON file
    with open(file_path, 'w') as f:
        json.dump(data, f)

    return {'message': "success"}


def read_report(option):
    try:
        # List all files in the 'data' directory
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

         # Initialize a list to store JSON content
        content_list = []

        # If 'all' is passed, sort all files by modification time (descending)
        if option == 'all':
            files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(dir_path, f)), reverse=True)
            for file in files:
                file_path = os.path.join(dir_path, file)
                with open(file_path, 'r') as f:
                    content_list.append(json.load(f))
            return content_list  # Return an array of JSON objects for 'all'

        # If no option or 'latest' is passed, read only the latest file
        if not option or option == 'latest':
            # Sort the files by modification time and pick the latest one
            latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(dir_path, f)))
            latest_file_path = os.path.join(dir_path, latest_file)
            with open(latest_file_path, 'r') as f:
                content_list.append(json.load(f))
            return content_list[0]  # Return only the single JSON object
        

    except FileNotFoundError:
        return {"error": "file not found"}
    except ValueError:
        return {"error": "invalid JSON format"}
    except Exception as e:
        return {"error": str(e)}