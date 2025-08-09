import os
import json 

json_outputs = os.environ['JSON_OUT']

def write_outputs_to_json(
    file_name: str, 
    canvas_id: str,
    canvas_x: int,
    canvas_y: int,
    canvas_width: int,
    canvas_height: int,
    canvas_type: str,   # (text, file, link, group)
    canvas_color: int = None,
    edge_from: str = None,
    edge_to: str = None,
    edge_label: str = None,
    *args
    ):

    json_file = os.path.join(json_outputs, file_name)

    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)

    if canvas_id and canvas_type:
        node_data = {
            "id": canvas_id,
            "type": canvas_type,
            "x": canvas_x,
            "y": canvas_y,
            "width": canvas_width,
            "height": canvas_height,
            "color": canvas_color
        }
        node_data = {k: v for k, v in node_data.items() if v is not None}
        data["nodes"].append(node_data)

    with open(json_file, 'a') as file:
        # whatever writing needs to go in here...
        pass 