class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None


def insert_end():
    global head

    value = int(input("Enter value to insert: "))

    new_node = Node(value)

    if head is None:
        head = new_node
    else:
        temp = head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    print(value, "inserted into the list.")


def delete_front():
    global head

    if head is None:
        print("List is empty!")
        return

    temp = head
    head = head.next

    print(temp.data, "deleted from the list.")


def display():
    if head is None:
        print("List is empty!")
        return

    temp = head

    print("List elements:", end=" ")

    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next

    print()


while True:
    print("\n--- Linked List Implementation ---")
    print("1. Insert at End")
    print("2. Delete from Front")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_end()

    elif choice == 2:
        delete_front()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
