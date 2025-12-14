"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)       

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    coordinates_from_azara = tuple(azara_record[1])
    coordinates_from_rui = rui_record[1]
    if coordinates_from_azara == coordinates_from_rui:
        return True
    return False

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    coordinates_from_azara = tuple(azara_record[1])
    coordinates_from_rui = rui_record[1]
    if coordinates_from_azara == coordinates_from_rui:
        return azara_record + rui_record
    return 'not a match'

def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    list_of_tuples = []
    multiline_string = ''
    for each_tuple in combined_record_group:
        new_tuple = each_tuple[:1] + each_tuple[2:]
        list_of_tuples.append(new_tuple)
    for each_tuple in list_of_tuples:
        multiline_string += str(each_tuple) + '\n' 
    return multiline_string