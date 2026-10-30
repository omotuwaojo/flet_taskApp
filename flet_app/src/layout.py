# Layout 
import flet as ft

def main(page: ft.Page):
    page.scroll=ft.ScrollMode.AUTO
    
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("First"),
                ft.Text("First"),
                ft.Text("First"),
            ]
        ),
        ft.Row(
            controls=[
                ft.Text("Row Display"),
                ft.Text("Row Display"),
                ft.Text("Row Display"),
            ]
        ),
        # Nesting Row and Column
        
        ft.Column(
            controls=[
                ft.Text("Dashboard"),
                
                ft.Row(
                    controls=[
                        ft.Button("Profile"),
                        ft.Button("Home")
                    ]
                ),
                ft.Text("Welcome to Nesting components")
            ]
        ),
        
        # Horizontal Alignments
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.HOME),
                ft.Icon(ft.Icons.SEARCH),
                ft.Icon(ft.Icons.SETTINGS),
            ]
        ),
        
        # vertical Alignment
        
        ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.HOME),
                ft.Text("Home")
            ]
        ),
        
        # Spacing
        ft.Column(
            spacing=50,
            controls=[
                ft.Text("Name"),
                ft.Text("Email"),
                ft.Text("Phone"),
            ]
        ),
        
        # Container 
        
        ft.Container(
            width= 500,
            height=250,
            padding=100,
            margin=100,
            border_radius=20,
            # border=ft.border.all(5, ft.Colors.RED),
            bgcolor=ft.Colors.BLUE,
            content=ft.Text(
                "Hello",
                color=ft.Colors.WHITE
            )
            
        ),
        
        # Box shadow
        ft.Container(
            width=200,
            height=100,
            padding=20,
            margin=40,
            bgcolor=ft.Colors.BLUE_200,
            border=ft.Border.all(2, ft.Colors.RED_400),
            shadow=ft.BoxShadow(
                blur_radius=20,
                color=ft.Colors.RED_400,
                offset=ft.Offset(5,5)),
            content=ft.Text(
                "This is a container",
                size=20,
                color=ft.Colors.RED_400,
                font_family="sans-serif",
                weight=ft.FontWeight.BOLD,
            ),
           
        ),
        
        # gradient background 
        ft.Container(
            width=200,
            height=100,
            padding=20,
            margin=40,
            border_radius=10,
            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_RIGHT,
                end=ft.Alignment.BOTTOM_LEFT,
                colors=[ft.Colors.RED_400, ft.Colors.BLUE_400],
            ),
            content=ft.Text(
                "This is a container",
                size=20,
                color=ft.Colors.WHITE,
                font_family='sans-serif',
                weight=ft.FontWeight.BOLD,
            ),
        ),
        
    )
ft.run(main)