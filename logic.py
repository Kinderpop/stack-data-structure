from typing import Any

class Node:
    """Узел для хранения данных и ссылки на следующий элемент."""
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Node | None = None

class Stack:
    """Класс стека на основе одногосвязного списка."""
    def __init__(self) -> None:
        self.head: Node | None = None
        self._size: int = 0

    def push(self, n: Any) -> str:
        """Добавить элемент на вершину стека."""
        new_node: Node = Node(n)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        return "ok"

    def pop(self) -> Any | str:
        """Удалить и вернуть элемент с вершины стека."""
        if self._size == 0:
            return "Удалять нечего, стек пустой"
        removed_value: Any = self.head.value
        self.head = self.head.next if self.head else None
        self._size -= 1
        return removed_value

    def back(self) -> Any | str:
        """Вернуть значение вершины стека без удаления."""
        if self._size == 0:
            return "Возвращать нечего, стек пустой"
        return self.head.value if self.head else "Возвращать нечего, стек пустой"

    def size(self) -> int:
        """Вернуть текущее количество элементов."""
        return self._size

    def clear(self) -> str:
        """Очистить стек."""
        self.head = None
        self._size = 0
        return "ok"