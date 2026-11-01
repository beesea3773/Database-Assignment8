class Contact:
    """Stores a contact's name and phone number."""

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    """Stores a contact in a linked list."""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Stores contacts using a hash table with separate chaining."""

    def __init__(self, size=10):
        if size <= 0:
            raise ValueError("Hash table size must be positive.")

        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        # Convert each character into a number and find an index.
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        # Create the contact and find its position.
        contact = Contact(key, value)
        index = self.hash_function(key)

        current = self.data[index]

        # Search the linked list for an existing name.
        while current is not None:
            if current.key == key:
                current.value = contact
                return
            current = current.next

        # Add a new node at the beginning of the linked list.
        new_node = Node(key, contact)
        new_node.next = self.data[index]
        self.data[index] = new_node

    def search(self, key):
        # Find the correct index for the name.
        index = self.hash_function(key)
        current = self.data[index]

        # Search through the linked list.
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        # Display all indexes and their stored contacts.
        for index in range(self.size):
            current = self.data[index]

            if current is None:
                print(f"Index {index}: Empty")
            else:
                contacts = []

                while current is not None:
                    contacts.append(str(current.value))
                    current = current.next

                print(f"Index {index}: - " + " - ".join(contacts))


# Test the hash table.
if __name__ == "__main__":
    table = HashTable(10)

    print("Empty Hash Table:")
    table.print_table()

    print("\nAdding Contacts:")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\nSearching for John:")
    print("Search result:", table.search("John"))

    print("\nTesting Collisions:")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    print("\nUpdating Rebecca:")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\nSearching for a Missing Contact:")
    print(table.search("Chris"))


# For this assignment, I created a contact management system using a hash table in Python. A hash table is
# useful because it makes searching for information faster. Instead of going through every contact one
# at a time, the program uses a hash function to figure out where a contact should be stored. This makes it
# easier to find someone by their name, especially when there are a lot of contacts.
# One problem with hash tables is that two different
# names can end up at the same index. This is called a collision. To handle this, I used separate chaining
# with linked lists. When two contacts have the same index, the program stores both contacts in a linked
# list at that location. For example, Amy and May ended up at the same index during my testing. The program
# was still able to store both contacts without losing their information. I also made sure that adding a
# contact with an existing name updates the phone number instead of creating another contact.
# A programmer might choose a hash table over a list or tree when they need to search for information
# quickly using a specific key. Lists are simpler, but searching through them can take longer as they
# grow. Trees can be useful for keeping information sorted, but a hash table is a good choice when fast
# searching and updating are more important than keeping everything in order.
