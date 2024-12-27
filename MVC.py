# Реалізація шаблону MVC (Model-View-Controller) на Python

# Model: відповідає за управління даними
class Model:
    def __init__(self):
        self.data = "Привіт, світ!"

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

# View: відповідає за відображення даних користувачеві
class View:
    @staticmethod
    def display_data(data):
        print(f"Дані: {data}")

    @staticmethod
    def display_message(message):
        print(message)

# Controller: зв'язує Model та View
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_data(self, new_data):
        self.model.set_data(new_data)
        self.view.display_message("Дані оновлено!")

    def show_data(self):
        data = self.model.get_data()
        self.view.display_data(data)

# Основна програма
if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)

    # Відображення початкових даних
    controller.show_data()

    # Оновлення даних через контролер
    new_data = "Привіт, MVC!"
    controller.update_data(new_data)

    # Відображення оновлених даних
    controller.show_data()
