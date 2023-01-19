from bookpy import BookPy
import os
import logging
import uuid


def init():

    process_id = uuid.uuid4().hex
    log_dir = os.getenv("LOG_DIR", "logs")
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    logging.basicConfig(filename=f"{log_dir}/{process_id}.log",
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(threadName)-10s %(message)s',)

    user = {
        "username": os.getenv("BOOK_APP_USR"),
        "password": os.getenv("BOOK_APP_PWD"),
    }
    url = os.getenv("BOOK_APP_URL")
    data = {
        "title": f"Life ({process_id})",
        "author": "John Doe",
        "dimensions": "20x20x20 cm",
        "format": "eBook",
        "isbn": "ISBN 102030",
        "language": "English",
        "paperback": "20 Pages",
        "publication_date": "2000-10-1",
        "publisher": "IT Books"
    }
    bookpy = BookPy(url)
    if bookpy.initialize():
        if bookpy.execute_login(user):
            if bookpy.execute_link_new_book():
                if bookpy.execute_new_book(data):
                    logging.info("New Book!")


if __name__ == "__main__":
    init()
