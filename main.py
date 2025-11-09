from typing import List


def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def train_file_list_to_json(
    english_file_list: List[str], german_file_list: List[str]
) -> List[str]:
    """Converts two lists of file paths into a list of JSON strings."""

    def process_file(name: str) -> str:
        # escape backslashes, slashes, and quotes
        name = name.replace("\\", "\\\\").replace("/", "\\/").replace('"', '\\"')
        return name

    template = '{{"English":"{}","German":"{}"}}'

    processed = []
    for eng, ger in zip(english_file_list, german_file_list):
        eng = process_file(eng)
        ger = process_file(ger)
        processed.append(template.format(eng, ger))
    return processed


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line."""
    with open(path, "w", encoding="utf-8") as f:
        for item in file_list:
            f.write(item + "\n")


if __name__ == "__main__":
    base_path = "./"
    english_path = "./english.txt"
    german_path = "./german.txt"

    english_files = path_to_file_list(english_path)
    german_files = path_to_file_list(german_path)

    processed = train_file_list_to_json(english_files, german_files)
    write_file_list(processed, base_path + "concated.json")
