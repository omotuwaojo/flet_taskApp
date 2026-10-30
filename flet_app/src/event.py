import flet as ft

def main(page: ft.Page):
    
    message = ft.Text()
    text =ft.Text()
    sign_in = ft.Text()
    
    def button_clicked(e):
        sign_in.value = "Signed In "
        page.update()
        print("Signed In ")
    
    def screen_msg(e):
        text.value= " This is a screen message"
        page.update()
    
    def greet(e):
        message.value = "Let's Build with flet "
        page.update()
        
    page.add(
        message,
        text,
        sign_in,
        ft.Text("Welecome to flet", size=30),
        ft.Button(
            "Click Here!",
            on_click=greet
            ),
        ft.Button(
            "Create Account",
            icon=ft.Icons.PERSON,
            icon_color=ft.Colors.RED,
            on_click=screen_msg
        ),
        ft.FilledButton(
            "Sign_In",
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.RED,
            on_click=button_clicked
        ),
        
        
    )
ft.run(main)