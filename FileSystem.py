from collections import deque

class Entity:
    def __init__(self, id, type, name, size, children):
        self.id = id
        self.type = type
        self.name = name
        self.size = size
        self.children = children

class FileSystem:
    def __init__(self):
        self.id_to_entity = self.build_dict()

    def entity_size(self, entity_id: int) -> int:
        # Returns the size of the file or directory associated with entity_id
        if entity_id not in self.id_to_entity:
            return -1  # Entity ID not found

        entity = self.id_to_entity[entity_id]

        # If the entity is a directory, calculate its total size recursively
        if entity.type == 'directory':
            return self.dfs(entity)

        # If the entity is a file, return its size
        if entity.type == 'file':
            return entity.size

        return 0

    def build_dict(self):
        # Initialize the file system structure
        entities = [
            Entity(id=1, type='directory', name="root", size=0, children=[2, 3]),
            Entity(id=2, type='directory', name="dir", size=0, children=[4, 5]),
            Entity(id=3, type='file', name="file1", size=300, children=[]),
            Entity(id=4, type='file', name="file2", size=100, children=[]),
            Entity(id=5, type='file', name="file3", size=200, children=[])
        ]

        # Create a dictionary to store entities by their ID for quick lookup
        entity_dict = {}
        for entity in entities:
            entity_dict[entity.id] = entity

        return entity_dict

    def dfs(self, entity):
        # Perform DFS to calculate the total size of a directory
        if entity.type == 'file':
            return entity.size

        if entity.type == 'directory' and len(entity.children) == 0:
            return 0

        total_size = 0
        for child_id in entity.children:
            total_size += self.dfs(self.id_to_entity[child_id])

        return total_size

def main():
    # Initialize the file system
    fs = FileSystem()

    # Test cases
    test_cases = [
        (1, 600),  # Root directory, expected size: 600 (sum of all files)
        (2, 300),  # Directory "dir", expected size: 300 (sum of file2 and file3)
        (3, 300),  # File "file3", expected size: 300
        (4, 100),  # File "file1", expected size: 100
        (5, 200),  # File "file2", expected size: 200
        (10, -1)   # Non-existent entity ID, expected size: -1
    ]

    # Run tests
    for entity_id, expected_size in test_cases:
        result = fs.entity_size(entity_id)
        print(f"Entity ID: {entity_id}, Expected Size: {expected_size}, Calculated Size: {result}")
        assert result == expected_size, f"Test failed for Entity ID {entity_id}. Expected {expected_size}, got {result}"

    print("All tests passed!")

# Run the main function
if __name__ == "__main__":
    main()
