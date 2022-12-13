

from unittest.mock import MagicMock
import get_book_titles
import book_inventory_client
import sys
sys.path.append("../server/")

import book_inventory_pb2
import book_inventory_pb2_grpc


def MockSubstitute(ISBNDetails):
    book_response = book_inventory_pb2.Book()
    if(ISBNDetails == "1"):
        book_response.ISBN = "1"
        book_response.title = "titanic";
        book_response.type = 2;
        book_response.author = "shakesphere";
        book_response.publishingYear = 1975;
        return book_inventory_pb2.GetBookResponse(book = book_response);

    if(ISBNDetails == "2"):
        book_response.ISBN = "2"
        book_response.title = "Fightclub";
        book_response.type = 1;
        book_response.author = "Cnolen";
        book_response.publishingYear = 1984;
        return book_inventory_pb2.GetBookResponse(book = book_response);
    return book_inventory_pb2.GetBookResponse(book = None);



def TestWithMock():
    bi_client = MagicMock()
    bi_client.GetBook = MagicMock(side_effect = MockSubstitute)

    ISBNList = [1, 2]
    bookTitles = get_book_titles.GetBookTitles(bi_client, ISBNList= ISBNList)
    assert bookTitles == ["titanic", "Fightclub"]
    print("Testing with Mock Successful")

def TestWithServer():

    bic = book_inventory_client.BookInventoryClient(IPaddress="localhost", port= 50051)
    ISBNList = [1, 2]

    bookTitles = get_book_titles.GetBookTitles(bic, ISBNList= ISBNList)
    assert bookTitles == ["titanic", "Fightclub"]
    print("Testing with server Successful")

if __name__ == '__main__':
    TestWithMock()
    TestWithServer()


