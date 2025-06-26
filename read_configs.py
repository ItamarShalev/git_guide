import json
import toml
import yaml
import xml.etree.ElementTree as ET

def read_toml(path):
    return toml.load(path)

def read_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def read_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def read_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    def parse_value(text):
        if res := text.strip().lower() in ('true', 'false'):
            return res == 'true'
        try:
            return int(text)
        except (ValueError, TypeError):
            return text

    def xml_to_dict(elem):
        d = {}
        for child in elem:
            if child.tag == 'items':
                d['items'] = [parse_value(item.text) for item in child.findall('item')]
            elif len(child):
                d[child.tag] = xml_to_dict(child)
            else:
                d[child.tag] = parse_value(child.text)
        return d
    return {root.tag: xml_to_dict(root)}

def main():
    base = "config/"
    files = [
        ("TOML", read_toml, base + "config.toml"),
        ("JSON", read_json, base + "config.json"),
        ("YAML", read_yaml, base + "config.yaml"),
        ("XML", read_xml, base + "config.xml"),
    ]
    files_values = {
        "TOML": read_toml(base + "config.toml"),
        "JSON": read_json(base + "config.json"),
        "YAML": read_yaml(base + "config.yaml"),
        "XML": read_xml(base + "config.xml"),
    }
    for name, data in files_values.items():
        print(f"--- {name} ---")
        print(data)
        print()

    toml_value = files_values.pop("TOML")
    for value in files_values.values():
        if toml_value != value:
            print(f"Values differ for {name} and TOML")
            exit(1)


def test_main():
    main()


if __name__ == "__main__":
    main()
