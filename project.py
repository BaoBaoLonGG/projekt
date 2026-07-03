import sys
import os
import json
import yaml
import xmltodict

if __name__ == '__main__':
    #(Task 1)
    if len(sys.argv) != 3:
        print("BŁĄD: Podaj plik wejściowy i wyjściowy!")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    #(Task 2, 4, 6)
    ext_in = os.path.splitext(input_file)[1].lower()
    with open(input_file, 'r', encoding='utf-8') as f:
        if ext_in == '.json': data = json.load(f)
        elif ext_in in ['.yml', '.yaml']: data = yaml.safe_load(f)
        elif ext_in == '.xml': data = xmltodict.parse(f.read())
        else: raise ValueError("Nieznany format wejściowy")

    #(Task 3, 5, 7)
    ext_out = os.path.splitext(output_file)[1].lower()
    with open(output_file, 'w', encoding='utf-8') as f:
        if ext_out == '.json': json.dump(data, f, indent=4)
        elif ext_out in ['.yml', '.yaml']: yaml.dump(data, f)
        elif ext_out == '.xml': f.write(xmltodict.unparse(data, pretty=True))
        else: raise ValueError("Nieznany format wyjściowy")

    print("Gotowe")