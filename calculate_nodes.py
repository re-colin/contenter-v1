
def calculate_node_size(text: str):
    text_length = len(text)
    node_size_y = text_length * 3
    node_size_x = node_size_y + 200

    return node_size_y, node_size_x 