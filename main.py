
books = []

while True:
    user_prompt = input("Type add, show, edit, remove or exit: ")
    user_prompt = user_prompt.strip()

    match user_prompt:
        case 'add':
            book_name = input("Enter a todo: ")
            books.append(book_name)
        case 'show':
            for data in books:
                print(data)
        case 'edit':
            number = int(input("Number of the todo to edit :"))
            number = (number + 1) - 1
            updated_todo = input("Enter updated todo: ")
            books[number] = updated_todo
        case 'remove':
            number = int(input("Number of the todo to remove :"))
            books.pop(number - 1)
        case 'exit':
            break

print("Bye!")