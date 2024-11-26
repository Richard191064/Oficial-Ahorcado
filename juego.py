import random


class User:
    """Clase que representa a un usuario."""
    def __init__(self, username, password):
        self.username = username
        self.password = password


class LoginSystem:
    """Clase que maneja el sistema de login."""
    def __init__(self):
        self.users = {}  # Almacena los usuarios registrados (username: User).

    def register_user(self, username, password):
        """Registra un nuevo usuario."""
        if username in self.users:
            print("El usuario ya existe.")
        else:
            self.users[username] = User(username, password)
            print(f"Usuario '{username}' registrado exitosamente.")

    def authenticate(self, username, password):
        """Autentica al usuario."""
        user = self.users.get(username)
        if user and user.password == password:
            print("Inicio de sesión exitoso.")
            return True
        print("Credenciales incorrectas.")
        return False


class HangmanGame:
    """Clase que representa el juego del ahorcado."""
    def __init__(self):
        self.words = ["python", "objetos", "programacion", "ahorcado", "interfaz", "artificial"]
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = set()
        self.max_attempts = 6
        self.attempts = 0
        self.hangman_stages = [
            """
               ------
               |    |
                    |
                    |
                    |
                    |
            =========
            """,
            """
               ------
               |    |
               O    |
                    |
                    |
                    |
            =========
            """,
            """
               ------
               |    |
               O    |
               |    |
                    |
                    |
            =========
            """,
            """
               ------
               |    |
               O    |
              /|    |
                    |
                    |
            =========
            """,
            """
               ------
               |    |
               O    |
              /|\\   |
                    |
                    |
            =========
            """,
            """
               ------
               |    |
               O    |
              /|\\   |
              /     |
                    |
            =========
            """,
            """
               ------
               |    |
               O    |
              /|\\   |
              / \\   |
                    |
            =========
            """
        ]

    def display_hangman(self):
        """Muestra el estado actual del ahorcado."""
        print(self.hangman_stages[self.attempts])

    def display_word(self):
        """Muestra el estado actual de la palabra con guiones."""
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.word_to_guess
        )

    def play(self):
        """Lógica principal del juego del ahorcado."""
        print("\n--- Bienvenido al juego del ahorcado ---")

        while self.attempts < self.max_attempts:
            self.display_hangman()
            print("\nPalabra: ", self.display_word())
            guess = input("Adivina una letra: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Por favor, ingresa una sola letra.")
                continue

            if guess in self.guessed_letters:
                print("Ya intentaste esa letra.")
                continue

            self.guessed_letters.add(guess)

            if guess in self.word_to_guess:
                print("¡Correcto!")
                if all(letter in self.guessed_letters for letter in self.word_to_guess):
                    print("\n¡Felicidades! Adivinaste la palabra:", self.word_to_guess)
                    return
            else:
                self.attempts += 1
                print(f"Letra incorrecta. Intentos restantes: {self.max_attempts - self.attempts}")

        # Si llega aquí, ha perdido.
        self.display_hangman()
        print("\nHas perdido. La palabra era:", self.word_to_guess)


# Simulación del programa principal
if __name__ == "__main__":
    # Crear el sistema de login
    login_system = LoginSystem()

    # Registrar usuarios
    login_system.register_user("ricardo", "191064180")
    login_system.register_user("user1", "password")

    # Intentar iniciar sesión
    username = input("Ingresa tu nombre de usuario: ")
    password = input("Ingresa tu contraseña: ")

    if login_system.authenticate(username, password):
        # Redirigir al juego del ahorcado
        game = HangmanGame()
        game.play()
    else:
        print("No se pudo iniciar sesión.")
