import os 

json_output_dir = os.environ['JSON_OUT']

def write_outputs_to_json(file_name: str):

    json_outputs = os.path.join('json_output_dir', file_name)

    with open(json_outputs, 'a') as file:
        pass    