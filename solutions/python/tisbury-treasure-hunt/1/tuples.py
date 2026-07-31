"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """
    # Arrange
    # record = ('treasure','coordinate')
    # Act
    extracted_coord = record[1]
    # Assert
    # print(extracted_coord)
    return extracted_coord


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """
    # Arrange
    # coordinate = '1C'
    # Act
    split_coord = tuple(coordinate)
    # Assert
    # print(split_tuple)
    return split_coord

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """
    # Arrange
    # azara_record = ('Amethyst Octopus', '1C') # Data given in README.md
    # rui_record = ('Seaside Cottages', ('1', 'C'), 'Blue')
    # Act
    azara_coord = tuple(azara_record[1])
    rui_coord = rui_record[1]
    # Assert
    return rui_coord == azara_coord


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    # Arrange
    # azara_record = ('Amethyst Octopus', '1C') # Data given in README.md
    # rui_record = ('Seaside Cottages', ('1', 'C'), 'Blue')
    # Act
    # print(compare_records(azara_record,rui_record))
    combined_record = azara_record + rui_record if compare_records(azara_record,rui_record) else "not a match"
    # Assert
    # print(combined_record)
    return combined_record

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """
    # Arrange
    combined_record_group = (
                    ('Scrimshawed Whale Tooth', '2A',
                        'Deserted Docks', ('2', 'A'), 'Blue'),
                    ('Brass Spyglass', '4B',
                        'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
                    ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
                    ('Glass Starfish', '6D',
                        'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
                    ('Vintage Pirate Hat', '7E',
                        'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
                    ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)',
                        ('7', 'F'), 'Orange'),
                    ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
                    ('Model Ship in Large Bottle', '8A',
                        'Harbor Managers Office', ('8', 'A'), 'Purple'),
                    ('Angry Monkey Figurine', '5B',
                        'Stormy Breakwater', ('5', 'B'), 'Purple'),
                    ('Carved Wooden Elephant', '8C',
                        'Foggy Seacave', ('8', 'C'), 'Purple'),
                    ('Amethyst  Octopus', '1F',
                        'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
                    ('Antique Glass Fishnet Float', '3D',
                        'Spiky Rocks', ('3', 'D'), 'Yellow'),
                    ('Silver Seahorse', '4E',
                        'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
            )
    record= ''
    for outer_tuple in combined_record_group:
        removed_element = outer_tuple[1]
        cleaned_tuple = tuple(element for element in outer_tuple if element != removed_element)
        # print(f'input tuple is {outer_tuple}')
        record += f'{cleaned_tuple}\n'
        # Assert
    # print(record)
    return record