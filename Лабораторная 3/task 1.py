class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError(f'Неправильное количество страниц: {pages!r}')
        else:
            raise AttributeError(f'Неправильный тип для страниц: {pages!r}')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author} Страницы: {self.pages}"


class AudioBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = None
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
