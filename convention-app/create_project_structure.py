import os

# Define the directory structure
directory_structure = {
    "convention-app": {
        "frontend": {
            "kivy_app": {
                "main.py": "",
                "main.kv": "",
                "screens": {
                    "login_screen.py": "",
                    "home_screen.py": "",
                    "event_schedule.py": "",
                    "map_screen.py": "",
                },
                "widgets": {
                    "custom_button.py": "",
                    "qr_code_widget.py": "",
                },
                "utils": {
                    "api_client.py": "",
                    "qr_code_generator.py": "",
                    "authentication.py": "",
                },
                "assets": {
                    "images": {},
                    "fonts": {},
                    "icons": {},
                },
                "data": {
                    "local_db.json": "",
                },
                "tests": {
                    "test_login.py": "",
                    "test_qr_code.py": "",
                },
                "requirements.txt": "",
                "README.md": "",
            },
            "docs": {
                "frontend_documentation.md": "",
            },
        },
        "backend": {
            "app": {
                "__init__.py": "",
                "models": {
                    "user.py": "",
                    "event.py": "",
                    "route.py": "",
                },
                "routes": {
                    "auth_routes.py": "",
                    "event_routes.py": "",
                    "qr_code_routes.py": "",
                },
                "schemas": {
                    "user_schema.py": "",
                    "event_schema.py": "",
                },
                "services": {
                    "authentication.py": "",
                    "qr_code_service.py": "",
                },
                "utils": {
                    "database.py": "",
                    "security.py": "",
                },
                "config.py": "",
                "main.py": "",
            },
            "tests": {
                "test_auth.py": "",
                "test_events.py": "",
            },
            "migrations": {},
            "requirements.txt": "",
            "README.md": "",
        },
        "shared": {
            "scripts": {
                "deployment_script.py": "",
            },
            "documentation": {
                "API_DOC.md": "",
            },
            "configs": {
                "dev_config.yaml": "",
                "prod_config.yaml": "",
            },
            "utilities": {
                "logger.py": "",
            },
        },
        "docker": {
            "frontend.Dockerfile": "",
            "backend.Dockerfile": "",
            "docker-compose.yml": "",
        },
        ".gitignore": "",
        "README.md": "",
        "LICENSE": "",
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Start creating the directory structure
create_structure('.', directory_structure)