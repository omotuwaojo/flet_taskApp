import flet as ft

def main(page: ft.Page):
    page.scroll = "auto"
    
    name_input = ft.TextField(
        label="Name",
        hint_text="Enter your name",
        prefix_icon=ft.Icons.PERSON,
        suffix_icon=ft.Icons.CHECK,
        autofocus=True,
        keyboard_type=ft.KeyboardType.TEXT
    )
    
    email_input = ft.TextField(
        label="Email",
        hint_text="Enter your email",
        prefix_icon=ft.Icons.EMAIL,
        suffix_icon=ft.Icons.CHECK,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    age_input = ft.TextField(
        label="Age",
        hint_text="Enter your age",
        prefix_icon=ft.Icons.CAKE,
        suffix_icon=ft.Icons.CHECK,
        keyboard_type=ft.KeyboardType.NUMBER
    )
    
    password_input = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        prefix_icon=ft.Icons.LOCK,
        # suffix_icon=ft.Icons.CHECK,
        password=True,
        can_reveal_password=True
    )
    
    password_confirm_input = ft.TextField(
        label="Confirm Password",
        hint_text="Confirm your password",
        prefix_icon=ft.Icons.LOCK,
        # suffix_icon=ft.Icons.CHECK,
        password=True,
        can_reveal_password=True
    )
    phone_input = ft.TextField(
        label="Phone Number",
        hint_text="Enter your phone number",
        prefix_icon=ft.Icons.PHONE,
        # suffix_icon=ft.Icons.CHECK,
        keyboard_type=ft.KeyboardType.PHONE
    )
    
    bio = ft.TextField(
        label="Bio",
        hint_text="Tell us about yourself",
        prefix_icon=ft.Icons.INFO,
        # suffix_icon=ft.Icons.CHECK,
        multiline=True,
        min_lines=3,
        max_lines=5
    )
    
    country = ft.Dropdown(
        label="Country",
        hint_text="Select your country",
        options=[
            ft.dropdown.Option("United States"),
            ft.dropdown.Option("Canada"),
            ft.dropdown.Option("United Kingdom"),
            ft.dropdown.Option("Australia"),
            ft.dropdown.Option("Other")
        ]
    )
    
    agree_terms = ft.Checkbox(
        label="I agree to the terms and conditions"
    )
    
    # hobbies = ft.CheckboxGroup(
    #     label="Hobbies",
    #     options=[
    #         ft.Checkbox(value="Reading", label="Reading"),
    #         ft.Checkbox(value="Swimming", label="Swimming"),
    #         ft.Checkbox(value="Cooking", label="Cooking"),
    #         ft.Checkbox(value="Traveling", label="Traveling")
    #     ]
    # )

    gender = ft.RadioGroup(
        # label="Gender",
        content=ft.Column(
        controls=[
            ft.Radio(value="Male", label="Male"),
            ft.Radio(value="Female", label="Female"),
            ft.Radio(value="Other", label="Other")
        ]
        )
    )
    
    dark_mode = ft.Switch(
        label="Dark Mode",
        value=False
    )
    
    volume_slider = ft.Slider(
        label="Volume",
        min=0,
        max=100,
        divisions=10,
        value=50
    )
    
    date_picker = ft.DatePicker()
    page.overlay.append(date_picker)
    
    def open_date_picker(e):
        date_picker.open = True
        page.update()
    
    
    

    submit_button = ft.FilledButton(
        "Submit",
        # on_click=validate_form
    )
    
    def validate_form(e):
        errors=[]
        if not name_input.value:
            errors.append("Name is required!")
        if not email_input.value:
            errors.append("Valid email is required")
        
        if not age_input.value or not age_input.value.isdigit():
            errors.append("Valid age is required")
            
        
        if errors:
            error_message.value = "\n".join(errors)
        else:
            error_message.value = "Form submitted successfully!"
        page.update()
        
    submit_button.on_click = validate_form
            
    error_message = ft.Text()
    
    page.add(
        name_input,
        email_input,
        age_input,
        password_input,
        password_confirm_input,
        phone_input,
        bio,
        country,
        agree_terms,
        # hobbies,
        ft.Text("Gender"),
        gender,
        dark_mode,
        volume_slider,
        ft.Text("Date of Birth"),
        ft.IconButton(ft.Icons.CALENDAR_MONTH, on_click=open_date_picker),
        ft.Button("Pick a date", on_click=open_date_picker),
        ft.FilledButton("Pick a date", on_click=open_date_picker),
        submit_button,
        # error_message/
    )
ft.run(main)