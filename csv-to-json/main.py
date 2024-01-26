from utils import convert_to_json
import pandas as pd
import sys

def main():
    # Check if the expected number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <csv_source_path> <json_output_path>")
        sys.exit(1)

    # Get file paths from command line arguments
    csv_source_path = sys.argv[1]
    json_output_path = sys.argv[2]

    print("csv_source_path: {}".format(csv_source_path))
    print("json_output_path: {}".format(json_output_path))

    df = pd.read_csv(csv_source_path, delimiter=';', decimal=',')

    # Call the convert_to_json() function with the CSV path and write the result to the specified JSON file
    json_result = convert_to_json(df)

    with open(json_output_path, 'w') as json_file:
        json_file.write(json_result)

if __name__ == "__main__":
    main()
