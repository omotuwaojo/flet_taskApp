import flet as ft
import asyncio
from components.primaryButton import primary_button
from components.statCard import statCard


def create_welcome_view(page: ft.Page):
    page.title = "Welcome"
    page.scroll = "auto"
    page.padding = 20
    page.bgcolor = ft.Colors.TEAL_50
    
    
    
    def route_change(e):
        page.views.clear()
        
        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.SafeArea(
                            expand=True,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.CircleAvatar(foreground_image_src="download.webp", width=200, height=200),
                                
                                ft.Text("Welcome to RukatechPay"),
                                primary_button(
                                    "Go to Home Page",
                                    on_click=lambda e: asyncio.create_task(page.push_route("/home"))
                                )
                            ]
                        ),
                        ),
                    ]
                )
            )
        elif page.route == "/home":
            page.views.append(
                ft.View(
                    route="/home",
                    
                    controls=[
                        ft.Column(
                            [
                                statCard("Total Users", "1,234", ft.Icons.PEOPLE, ft.Colors.BLUE),
                                statCard("Total Revenue", "$12,345", ft.Icons.MONEY, ft.Colors.GREEN),
                                statCard("Active Sessions", "567", ft.Icons.HOME, ft.Colors.ORANGE),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ]
                )
            )
        page.update()
    
    async def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    route_change(None)  # Initialize the first view based on the current route
    
    
ft.run(create_welcome_view)