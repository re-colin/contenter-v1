import os 

json_output_dir = os.environ['JSON_OUT']

def write_outputs_to_json(
    file_name: str, 
    canvas_id: str,
    canvas_x: int,
    canvas_y: int,
    canvas_width: int,
    canvas_height: int,
    canvas_type: str,   # (text, file, link, group)
    canvas_color: int, 
    *args
    ):

    json_outputs = os.path.join('json_output_dir', file_name)

    with open(json_outputs, 'a') as file:
        pass    