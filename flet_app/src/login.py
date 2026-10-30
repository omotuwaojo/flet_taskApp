import flet as ft

def main(page: ft.Page):
    page.title ="Login Form"
    page.vertical_alignment =ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    
    def login(e):
        username = username_field.value
        password = password_field.value
        if username == "Admin" and password == "admin1":
            result.value = "Login successful!"
        else:
            result.value = "Admin only can sign Here!"
        page.update()
    
    username_field = ft.TextField(
        label="Username", 
        autofocus=True,
    )
    password_field = ft.TextField(
        label="Password", password=True,
        can_reveal_password=True,
    )
    login_button = ft.Button(
        "Login",
        color=ft.Colors.WHITE,
        on_click=login,
        bgcolor=ft.Colors.BLUE_400,
        icon=ft.Icons.PERSON
        
    )
    
    result = ft.Text()
    
    
    page.add(
     
        username_field,
        password_field,
        login_button,
        result 
        
        
    )
ft.run(main)