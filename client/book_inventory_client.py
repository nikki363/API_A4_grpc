from __future__ import print_function

import logging
import grpc
import sys
sys.path.append("../server/")

import book_inventory_pb2
import book_inventory_pb2_grpc

class BookInventoryClient:

    def __init__(self, IPaddress, port):
        self.IPaddress = IPaddress;
        self.port = port;

    def CreateBook(self, bookDetails):
        bookCreated = book_inventory_pb2.Book();
        bookCreated.ISBN = bookDetails["ISBN"];
        bookCreated.title = bookDetails["title"];
        bookCreated.type = bookDetails["type"];
        bookCreated.author = bookDetails["author"];
        bookCreated.publishingYear = bookDetails["publishingYear"];

        with grpc.insecure_channel(str(self.IPaddress) + ":" + str(self.port)) as channel:
            stub = book_inventory_pb2_grpc.BookInventoryStub(channel)
            CreateBookresponse = stub.CreateBook(book_inventory_pb2.CreateBookRequest(book = bookCreated))
            return CreateBookresponse


    def GetBook(self, ISBNDetails):
        with grpc.insecure_channel(str(self.IPaddress) + ":" + str(self.port)) as channel:
            stub = book_inventory_pb2_grpc.BookInventoryStub(channel)
            GetBookresponse = stub.GetBook(book_inventory_pb2.GetBookRequest(ISBN = ISBNDetails))
            return GetBookresponse


if __name__ == '__main__':
    logging.basicConfig()
    bic = BookInventoryClient(IPaddress= "localhost", port= 50051)
    bic.CreateBook({ "ISBN" : "6", "title" : "Khaithi", "author" : "Arjun khan", "type" : 3, "publishingYear" : 2015})
    bic.GetBook(ISBNDetails = "3")
