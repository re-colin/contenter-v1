def write_outputs_to_file(
    *args,
    output_file_name: str,
    output: str
):
    with open(f"{output_file_name}.md", "a", encoding="utf-8") as file:
        file.write(output)