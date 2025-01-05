import random
#Реализация Стэка
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def stack_items(self):
        return self.items

#Реализация очереди
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def queue_items(self):
        return self.items

#Тестирование стэка
stack = Stack()
print('Стэк пустой?: ',stack.is_empty())

for i in range(1,5):
    stack.push(random.randint(1,100))
print('Заполнили стэк: ', stack.stack_items())

print('Стэк пустой?: ',stack.is_empty())

print('Забираем два элемента стэка: ')
print(stack.pop())
print(stack.pop())
print('Оставшийся стэк: ', stack.stack_items())

#Тестирование очереди
print('\n')

queue = Queue()
print('Очередь пустая?: ',queue.is_empty())

for i in range(1,5):
    queue.enqueue(f'Действие {i}')
print('Заполнили очередь: ', queue.queue_items())

print('Очередь пустая?: ',queue.is_empty())

print('Выполняем два действия очереди: ')
print(queue.dequeue())
print(queue.dequeue())
print('Оставшиеся действия в очереди: ', queue.queue_items())