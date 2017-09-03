from dao.OrientDBDao import OrientDBDao

# class OrientDBDao2:
#     def __init__(self):
#         print "Calling " + str(self.__class__) + " "
#         # print "Calling constructor"

dao = OrientDBDao()

### Read Bible CSV ###
# TODO


dao.listDB()

# dao.insertTextNode({'TextID':'anthony-1', 'BookName':'Bible', 'Book': 'anthony', 'Chapter' : '1', 'Verse' : '1', 'Text': 'Anthony' })
# texts = dao.findNode('anthony-1')
# for t in texts:
#     print t.TextID
#     print t.Book
#     print t.Chapter
#     print t.Verse
#     print t.Text
#     print '######'

lastChapter = None
lastBook = None
text = ""
for line in open('data/bible_data_set.csv'):
    linePart = line.split(",")
    book = linePart[1]
    chapter = linePart[2]
    verse = linePart[3]
    if lastChapter == None or lastBook == None:
        text += linePart[4]
    elif (chapter == lastChapter) and (book == lastBook):
        text += linePart[4]
    else:
        dao.insertBibleChapter(book, chapter,  text)
        text = linePart[4]
    print "%s %s %s" % (book, chapter, verse)
    lastChapter = chapter
    lastBook = book

if len(text) > 0:
    dao.insertBibleChapter(book, chapter,  text)

