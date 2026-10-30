import flet as ft 
import re


def main(page: ft.Page):
    
    Email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    
    def is_valid_email(email):
        return re.match(Email_regex, email) is not None
    
    name_input = ft.TextField(
        label="Name"
    )
    
    email_input = ft.TextField(
        label="Email",
    )
    
    age_input = ft.TextField(
        label="Age",
    )
    
    submit_button = ft.FilledButton(
        "Submit",
        
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
        submit_button,
        error_message
    )
    
    
ft.run(main)