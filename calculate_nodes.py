def calculate_node_size(text: str):
    text_length = len(text)
    node_size_height = text_length - (text_length / 3)
    node_size_width = 400

    node_position_y = node_size_height + 20 

    return node_size_height, node_size_width, node_position_y
