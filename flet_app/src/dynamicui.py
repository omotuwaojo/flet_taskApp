import flet as ft 

def main(page: ft.Page):
    page.scroll = "auto"
    
    students = [
        {"name": "John Doe", "age": 20, "email": "john.doe@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"},
        {"name": "Alice Johnson", "age": 22, "email": "alice.johnson@example.com"},
        {"name": "Bob Brown", "age": 30, "email": "bob.brown@example.com"},
        {"name": "Charlie Davis", "age": 28, "email": "charlie.davis@example.com"}
    ]
    
    grid = ft.GridView(
        expand=True,
        max_extent=350,
        child_aspect_ratio=1.5,
        spacing=10,
        run_spacing=10,
        runs_count=2,
    )
    
    for student in students:
       grid.controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                      controls=[
                            ft.Icon(ft.Icons.PERSON, size=50),
                            ft.Text(student["name"], size=20, weight="bold"),
                            ft.Text(f"Age: {student['age']}"),
                            ft.Text(f"Email: {student['email']}"),
                        ]
                    )
                )
            )
        )

    page.add(
        grid
    )
ft.run(main)