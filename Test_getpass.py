from getpass import getpass

def login():
    username = input("Benutzername: ")
    password = getpass("Passwort: ")

    # Überprüfung der Benutzerdaten
    if username == "admin" and password == "admin123":
        print("Erfolgreich eingeloggt!")
    else:
        print("Ungültige Anmeldeinformationen.")

login()
