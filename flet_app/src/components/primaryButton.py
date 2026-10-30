import flet as ft

def primary_button(text, on_click):
    return ft.FilledButton(
        text,
        on_click=on_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=ft.Padding(10, 20, 10, 20),
            text_style=ft.TextStyle(size=16, color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE_500,
            overlay_color=ft.Colors.BLUE_700,
        ),
    )