import json
import csv


def distribute_books(users, books):

    user_count = len(users)
    book_per_user = len(books) // user_count
    remainder = len(books) % user_count

    current_book_index = 0

    for i in range(user_count):
        user_books = []

        for _ in range(book_per_user):
            user_books.append(books[current_book_index])
            current_book_index += 1

        if remainder > 0:
            user_books.append(books[current_book_index])
            current_book_index += 1
            remainder -= 1

        users[i]['books'] = user_books

    return users


def filter_users(users):

    filtered_users = []
    for user in users:
        filtered_user = {
            "name": user.get("name"),
            "gender": user.get("gender"),
            "address": user.get("address"),
            "age": user.get("age")
        }
        filtered_users.append(filtered_user)
    return filtered_users


def main():
    with open("users.json", "r") as file:
        users = json.load(file)
        users = filter_users(users)

    books = []
    with open("books.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append({
                "title": row["Title"],
                "author": row["Author"],
                "pages": int(row["Pages"]),
                "genre": row["Genre"]
            })

    distributed_users = distribute_books(users, books)

    output = {"users": distributed_users}
    with open("result.json", "w") as file:
        json.dump(output, file, indent=4)


if __name__ == "__main__":
    main()