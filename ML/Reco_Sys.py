import csv
import random

def load_books_from_csv(csv_file):
    books = {}
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            books[row[1]] = row[0]
    return books

def get_suggestions(user_history, book_database):
    suggestions = []
    
    if len(user_history) == 0:
        print("User history is empty!")
        return suggestions

    if len(user_history) == 1:
        book_name = user_history[0]
        if book_name not in book_database:
            print("Book not found in the database!")
            return suggestions
        
        genre = book_database[book_name]
        same_genre_books = [b for b, g in book_database.items() if g == genre and b != book_name]
        random.shuffle(same_genre_books)
        suggestions.extend(same_genre_books[:3])
    
    elif len(user_history) == 2:
        for book_name in user_history:
            if book_name not in book_database:
                print("Book not found in the database!")
                continue
                
            genre = book_database[book_name]
            same_genre_books = [b for b, g in book_database.items() if g == genre and b != book_name]
            random.shuffle(same_genre_books)
            suggestions.extend(same_genre_books[:3])
            
    else:
        latest_three_books = user_history[-3:]
        for book_name in latest_three_books:
            if book_name not in book_database:
                print("Book not found in the database!")
                continue
                
            genre = book_database[book_name]
            same_genre_books = [b for b, g in book_database.items() if g == genre and b != book_name]
            random.shuffle(same_genre_books)
            suggestions.extend(same_genre_books[:3])
        
        last_book_genre = book_database[user_history[-1]]
        last_genre_books = [b for b, g in book_database.items() if g == last_book_genre and b not in user_history]
        random.shuffle(last_genre_books)
        suggestions.append(last_genre_books[0])
        
    return suggestions

# Load book database from CSV
book_database = load_books_from_csv("ML/Book1.csv")

# Take user input for book history
user_history = []
while True:
    book_name = input("Enter a book name (press Enter to stop): ").strip()
    if not book_name:
        break
    user_history.append(book_name)

# Get recommendations based on the user's input
recommendations = get_suggestions(user_history, book_database)
print("Recommendations based on user's history:")
for i, book in enumerate(recommendations, 1):
    print(f"{i}. {book}")
