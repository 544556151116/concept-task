book_records = []
while True:
    record = input("Enter book record (format: 'Book Title - Days Borrowed') or 'done' to finish: ")
    if record.lower() == 'done':
        break
    book_records.append(record)
    book_dict = {}
    unique_titles = set()
for record in book_records:
    title, days = record.split(" - ")
    days = int(days)
    if title in book_dict:
        book_dict[title] += days
    else:
        book_dict[title] = days
        unique_titles.add(title)
most_borrowed = max(book_dict , key=book_dict.get)
print (f"The most borrowed book: {most_borrowed}")        
least_borrowed = min(book_dict , key=book_dict.get) 
print (f"The least borrowed book: {least_borrowed}")        
average = sum(book_dict.values()) / len(book_dict)
print (f"The average: {average}")
print(f"The unique book: {unique_titles}")
sorted_books = sorted(book_dict.items(), key=lambda x: x[1], reverse=True)
print (f"The books after sorting in descending order: {sorted_books}")
