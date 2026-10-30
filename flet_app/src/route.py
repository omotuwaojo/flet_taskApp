import flet as ft 
import asyncio


def main(page: ft.Page):
    page.title = "route example"
    page.scroll = "auto"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def route_change(route):
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
                                ft.FilledButton(
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
                                ft.TextField(
                                    label="Enter your name",
                                    autofocus=True,
                                    hint_text="Name",
                                    prefix_icon=ft.Icons.PERSON,
                                    ),
                                ft.TextField(
                                    label="Enter your email",
                                    hint_text="Email",
                                    autofocus=True,
                                    prefix_icon=ft.Icons.EMAIL,
                                    ),
                                ft.TextField(
                                    label="Enter your phone number",
                                    hint_text="Phone Number",
                                    autofocus=True,
                                    prefix_icon=ft.Icons.PHONE,
                                    ),
                                ft.TextField(
                                    label="Enter your password",
                                    hint_text="Password",
                                    password=True,
                                    autofocus=True,
                                    prefix_icon=ft.Icons.LOCK,
                                    can_reveal_password=True
                                    ),
                                ft.FilledButton(
                                    "Login",
                                    on_click=lambda e: asyncio.create_task(page.push_route("/dashboard"))
                                )
                                
                                    
                                
                            ]
                        )
                    ]
                )
            )
        elif page.route == "/dashboard":
            page.views.append(
                ft.View(
                    route="/dashboard",
                    controls=[
                        ft.Text("Welcome to Dashboard"),
                        ft.TextButton(
                            "Go back to Welcome Screen",
                            on_click=lambda e: asyncio.create_task(page.push_route("/"))
                        )
                    ]
                )
            )
        page.update()
        
    async  def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)
            
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    route_change(None)
    
ft.run(main)