def create_user(name, *, age, is_admin=False):
    print(f"Name: {name}, Age: {age}, Admin: {is_admin}")

create_user("Alice", age=30, is_admin=True)
create_user("Bob", 25)