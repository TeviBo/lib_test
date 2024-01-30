def get_keyboard_positions(keyboard: list, requested_position: int) -> int:
    """
    Get position from android keyboard
        :type keyboard: list
        :param keyboard: keyboard to evaluate and take the positions
        :type requested_position: int
        :param requested_position: position to be found
        :return: position index
    """
    return keyboard.index(requested_position)


def transform_input_string(string_password: str, keyboard: list[int]) -> list:
    """
    Transform input string to an array of positions based on keyboard mapping
    :type string_password: str
    :param string_password: input string with numbers
    :type keyboard: list
    :param keyboard: keyboard layout
    :return: array of positions
    """
    positions_array = []
    for char in string_password:
        # position = get_keyboard_positions(keyboard, int(char))
        position = keyboard.index(int(char))
        positions_array.append(position)
    return positions_array
