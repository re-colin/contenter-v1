import os
import json 

json_outputs = os.environ['JSON_OUT']

def write_outputs_to_json(
    file_name: str,
    card_text: str, 
    canvas_type: str,   # (text, file, link, group)
    canvas_id: str,
    canvas_x: int,
    canvas_y: int,
    canvas_width: int,
    canvas_height: int,
    canvas_color: str = None,
    edge_id: str = None,
    edge_fromNode: str = None,
    edge_toNode: str = None,
    edge_fromSide: str = None,
    edge_toSide: str = None,
    edge_label: str = None,
    *args
    ):

    json_file = os.path.join(json_outputs, f"{file_name}.canvas")
    
    with open(json_file, 'r', encoding="utf-8") as file:
        node_data = json.load(file)
        print(node_data)

    if canvas_id and canvas_type:
        node_object = {
                    "id": canvas_id,
                    "type": canvas_type,
                    "x": canvas_x,
                    "y": canvas_y,
                    "width": canvas_width,
                    "height": canvas_height,
                    "text": card_text,
                    "color": canvas_color
                }
        

        if edge_id:
            pass
            # "edges": [
            #     {
            #         "id": edge_id,
            #         "fromNode": edge_fromNode,
            #         "toNode": edge_toNode,
            #         "fromSide": edge_fromSide,
            #         "toSide": edge_toSide,
            #         "label": edge_label 
            #     }
            # ]

    node_data['nodes'].append(node_object)

    print(f"NODE OBJECT {node_data}")

    with open(json_file, 'w', encoding="utf-8") as file:
        json.dump(node_data, file) 