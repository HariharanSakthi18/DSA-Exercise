class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


head = None


# Insert at Front
def insert_front():
    global head

    value = int(input("Enter value: "))

    new_node = Node(value)

    new_node.prev = None
    new_node.next = head

    if head is not None:
        head.prev = new_node

    head = new_node

    print(value, "inserted at front.")


# Delete at End
def delete_end():
    global head

    if head is None:
        print("List is empty!")
        return

    temp = head

    # Only one node
    if temp.next is None:
        print(temp.data, "deleted from end.")
        head = None
        return

    # Move to the last node
    while temp.next is not None:
        temp = temp.next

    # Remove the last node
    temp.prev.next = None

    print(temp.data, "deleted from end.")


# Display the list
def display():
    if head is None:
        print("List is empty!")
        return

    temp = head

    print("List:", end=" ")

    while temp is not None:
        print(temp.data, "<->", end=" ")
        temp = temp.next

    print("NULL")


# Main menu
while True:
    print("\n--- Doubly Linked List Menu ---")
    print("1. Insert at Front")
    print("2. Delete at End")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_front()

    elif choice == 2:
        delete_end()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
