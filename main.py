import sys
import logic

def main() -> None:
    '''Запустить программу'''
    stack: logic.Stack = logic.Stack()

    print("Команды управления стеком:\n1. push <n> - Добавление <n> в стек\n2. pop - Удаление последнего элемента стека \
и его вывод\n3. back - Вывод последнего элемента стека\n4. size - Вывод кол-ва элементов в стеке\n5. clear - \
Очистка стека\n6. exit - Выход из программы")
    
    for line in sys.stdin:
        parts: list[str] = line.strip().split()
        if not parts:
            print("Пожалуйста введите команду...")
            continue
        
        command: str = parts[0]
        
        if command == "push":
            try:
                n: int = int(parts[1])
                print(stack.push(n))
            except ValueError:
                print('Пожалуйста введите число...')
        elif command == "pop":
            print(stack.pop())
        elif command == "back":
            print(stack.back())
        elif command == "size":
            print(stack.size())
        elif command == "clear":
            print(stack.clear())
        elif command == "exit":
            print("bye")
            break
        else:
            print('Введена некорректная команда\nПопробуйте снова...')

if __name__ == "__main__":
    main()