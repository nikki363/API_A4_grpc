
from concurrent import futures
import logging

import grpc
import book_inventory_pb2
import book_inventory_pb2_grpc
import db

class BookInventory(book_inventory_pb2_grpc.BookInventoryServicer):

    def CreateBook(self, request, context):
        book_response = book_inventory_pb2.Book();
        value = request.book.ISBN;
        for i in db.list_of_books:
            for key, val in i.items():
                if (key == "ISBN"  and  val == value) :
                    return book_inventory_pb2.CreateBookResponse(book = None, message = "Book with the given ISBN already exists");

        book_response = book_inventory_pb2.Book();
        book_response.ISBN = request.book.ISBN;
        book_response.title = request.book.title;
        book_response.type = request.book.type;
        book_response.author = request.book.author;
        book_response.publishingYear = request.book.publishingYear;
        return book_inventory_pb2.CreateBookResponse(book = book_response, message = "book created successfully");


    def GetBook(self, request, context):
        value = request.ISBN;
        # iterate over the list
        for i in db.list_of_books:
            for key, val in i.items():
                if (key == "ISBN"  and  val == value) :
                    book_identified = i
                    book_response = book_inventory_pb2.Book()
                    book_response.ISBN = book_identified["ISBN"]
                    book_response.title = book_identified["title"];
                    book_response.type = book_identified["type"];
                    book_response.author = book_identified["author"];
                    book_response.publishingYear = book_identified["publishingYear"];
                    return book_inventory_pb2.GetBookResponse(book = book_response, message = "book retrieved successfully");
        return book_inventory_pb2.GetBookResponse(book = None, message = "book not retrieved");



def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_inventory_pb2_grpc.add_BookInventoryServicer_to_server(BookInventory(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()



