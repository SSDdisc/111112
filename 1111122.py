import sqlite3

def connect_db():
    return sqlite3.connect("films.db")

def search_by_title(title):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM films WHERE title LIKE ?", ('%'+title+'%',))
    results = cursor.fetchall()
    connection.close()
    return results

def search_by_genre(genre):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM films WHERE genre = ?", (genre,))
    results = cursor.fetchall()
    connection.close()
    return results

def search_by_year(year):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM films WHERE year = ?", (year,))
    results = cursor.fetchall()
    connection.close()
    return results

def search_by_rating(rating):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM films WHERE rating >= ?", (rating,))
    results = cursor.fetchall()
    connection.close()
    return results

def search_by_age_rating(age_rating):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM films WHERE age_rating >= ?", (age_rating,))
    results = cursor.fetchall()
    connection.close()
    return results

def display_results(results):
    if not results:
        print("Нет фильмов, соответствующих запросу.")
        return
    print(f"{'Title':<60}{'Year':<10}{'Duration':<10}{'Rating':<10}{'Age rating':<10}")
    print("-" * 100)
    for row in results:
        print(f"{row[0]:<60}{row[1]:<10}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

def main():
    print("Добро пожаловать в программу поиска фильмов!")
    while True:
        print("\nВыберите вариант поиска:")
        print("1) По названию фильма")
        print("2) По жанру")
        print("3) По году")
        print("4) По рейтингу фильма")
        print("5) По возрастному рейтингу")
        choice = input("Введите номер поиска (1-5): ")

        if choice == '1':
            title = input("Введите название фильма: ")
            results = search_by_title(title)
        elif choice == '2':
            genre = input("Введите жанр: ")
            results = search_by_genre(genre)
        elif choice == '3':
            year = input("Введите год: ")
            results = search_by_year(year)
        elif choice == '4':
            rating = input("Введите минимальный рейтинг: ")
            results = search_by_rating(rating)
        elif choice == '5':
            age_rating = input("Введите минимальный возрастной рейтинг: ")
            results = search_by_age_rating(age_rating)
        else:
            print("Некорректный выбор, попробуйте снова.")
            continue

        display_results(results)
        continue_search = input("Продолжить поиск? (y/n): ") or 'n'
        if continue_search.lower() != 'y':
            break

if __name__ == "__main__":
    main()
