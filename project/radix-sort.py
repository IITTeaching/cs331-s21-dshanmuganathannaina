import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radixSort(arr, length, position, n_buckets = 128):
  sortedArray = len[arr] * [None]
  occurrences = n_buckets * [0]

  for i in arr:
    char = 0
    if (length + position - len(i)) < 0:
      char = i[length + position] + 1
    occurrences[char] += 1
  
  for i in range (len(occurrences) - 1):
    occurrences[i+1] = occurrences[i+1] + occurrences[i]
  
  for i in range(len(arr) - 1, -1, -1):
    char = 0
    if (length + position - len(arr[i])) < 0:
      char = arr[i][length + position] + 1
    sortedArray[occurrences[char] - 1] = arr[i]
    occurrences[char] -= 1
  
  return sortedArray

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    sortedBook = book_to_words(book_url)
    length = 0
    for i in sortedBook:
        if len(i) > length:
            length = len(i)
    position = -1
    while (length + position) >= 0:
        sortedBook = radixSort(sortedBook, length, position)
        position = position - 1
    for i in sortedBook:
        yield i.decode('ascii')
