from __future__ import print_function

import logging

import book_inventory_client

import grpc

def GetBookTitles(bic, ISBNList):
    booksTitles = []
    for i in ISBNList:
        bookRetrieved = bic.GetBook(ISBNDetails = str(i))
        booksTitles.append(bookRetrieved.book.title)
    return booksTitles


if __name__ == '__main__':
    logging.basicConfig()
    bic = book_inventory_client.BookInventoryClient(IPaddress="localhost", port= 50051)
    GetBookTitles(bic, ISBNList = [1, 2])
