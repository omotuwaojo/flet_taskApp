import flet as ft

def main(page: ft.Page):
    page.scroll = "auto"

    students = [
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"},
    ]

    list_view = ft.ListView(
        expand=True,
        spacing=10,
    )

    for student in students:
        list_view.controls.append(
            ft.ListTile(
                leading=ft.Icon(ft.Icons.PERSON),
                title=ft.Text(student["name"]),
                subtitle=ft.Text(f"Age: {student['age']}"),
                # trailing=ft.Text(student["email"])
                trailing=ft.Icon(ft.Icons.EMAIL)
            )
        )

    page.add(list_view)
ft.run(main)