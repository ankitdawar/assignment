import os
import sys
import re

def validate_date(date_str):
    """
    Validates the date format to ensure it's in YYYY-MM-DD format.
    
    Args:
        date_str (str): The date string to validate.
        
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", date_str))

def ensure_output_dir_exists(output_dir):
    """
    Ensures the output directory exists. If not, it creates the directory.
    
    Args:
        output_dir (str): The path to the output directory.
    """
    os.makedirs(output_dir, exist_ok=True)

def extract_logs_by_date(file_path, target_date, output_dir="output"):
    """
    Extracts all logs for a specific date from a large log file and writes them to an output file.
    
    Args:
        file_path (str): Path to the log file.
        target_date (str): The date (YYYY-MM-DD) for which to extract logs.
        output_dir (str): Directory where the output file will be saved.
    """
    # Ensure the output directory exists
    ensure_output_dir_exists(output_dir)

    # Construct the output file path
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        # Open the input log file and output file
        with open(file_path, "r") as input_file, open(output_file, "w") as outfile:
            line_count = 0
            extracted_count = 0
            for line in input_file:
                line_count += 1

                # Check if the line starts with the target date
                if line.startswith(target_date):
                    outfile.write(line)
                    extracted_count += 1

                # Provide progress feedback every 100,000 lines processed
                if line_count % 100000 == 0:
                    print(f"Processed {line_count} lines... {extracted_count} logs extracted.")

        print(f"\nLogs for {target_date} have been written to {output_file}.")
        print(f"Total lines processed: {line_count}, Total logs extracted: {extracted_count}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while accessing '{file_path}' or '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    date_to_extract = sys.argv[1]

    # Validate the date format
    if not validate_date(date_to_extract):
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    log_file_path = 'test_logs.log'

    # Run the extraction function
    extract_logs_by_date(log_file_path, date_to_extract)

if __name__ == "__main__":
    main()
