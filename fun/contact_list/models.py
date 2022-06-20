class Contact:
    def __init__(self, name: str, surname: str, phone_number: str) -> None:
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return f"User:\n\tname: {self.name}\n\tsurname: {self.surname}\n\tphone number: {self.phone_number}"


class UnknownContact(Contact):
    def __init__(self) -> None:
        super().__init__("Unknown", "Unknown", "Empty")
