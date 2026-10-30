import flet as ft

def main(page: ft.Page):
    page.title="Text Controls"
    page.scroll=ft.ScrollMode.ADAPTIVE
    
    page.add(
        ft.Column(
            controls=[
                ft.Text("Welcome to flet", size=50),
                ft.Text("Secound Text", size=40, color=ft.Colors.RED_600, italic=True),
                ft.Text(
                    value="Third Text with value and bg color",
                    size=50,
                    color=ft.Colors.BLUE,
                    bgcolor=ft.Colors.GREEN_400,
                    weight=ft.FontWeight.W_200
                ),
                # selectable text
                ft.Text(
                    value="Selected Text",
                    size= 60,
                    weight=ft.FontWeight.BOLD,
                    selectable=True
                ),
                # long text limiting
                ft.Text(
                    "limit long text to 1 line with ellipisisbjwebkjgbekjgkjwbekjgbwegjkbekjwjgbjbwkbgjbw;geabg;oabweqppwjepigiheowhgsioreuotyoreywtrnuyri qoqpywqtyowqyptphwsnaknasdfa,mnkljsafkwisiuf;awhsfluwehfiuwseguiwaegsiuafgweaifsafihohafiuwgaiufgaiuifigaiegiflwgakjhfailugaluigwgfiuwgaifugaiug",
                    theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                ),
                ft.Text(
                    value=(
                        "lhlhglhaglhelahglkhslkdghldshglhsalkdghlkah;dsgggggggioehroighoihegoihwiehgeoijgaewkvnkdsnknkvnskdvkjdjsndjkbsnkjdfkjsbgkjdbsgjbskjdbgbkjsegskehiuwuherighoioerhoushdgoheroghkdsgndf,gnksndkjgsneiuhgoh'ahhg'ha;ohsgshiea'ghoi'hehglihaweieoghsaph'wgiohoaewhgpwphepghwpiwesgnsldknndaninsngaisdnfvnoifnoiwifjweoiefjaoihweiohgihwoeiighohgoiihehgoihweoihgiojwepighwhgoiehwoighoehgoeghwohgohoiwgoeioigheoihgoihiogoiehgoiwheeiighiwihegioheowhoghoihgoiwheoigihoiwhegiooigshoeoghwoiigoi"
                    ),
                    max_lines=2,
                ),
                # icon Button and FloatActionButton
                ft.Button(
                    "Create Account",
                    icon=ft.Icons.PERSON,
                    color=ft.Colors.RED,
                    icon_color=ft.Colors.RED,
                ),
                ft.FloatingActionButton(
                    icon=ft.Icons.WHATSHOT_SHARP
                )
            ]
        )
    )
    
ft.run(main)