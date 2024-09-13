import subprocess
import os

def convert_mbox_to_pst(mbox_file, output_dir):
    """
    Convert MBOX to PST using readpst tool.
    :param mbox_file: Path to the MBOX file
    :param output_dir: Directory where PST files will be saved
    """
    # Check if the MBOX file exists
    if not os.path.exists(mbox_file):
        raise FileNotFoundError(f"The file {mbox_file} does not exist.")
    
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Run the readpst command to convert MBOX to PST
        subprocess.run(["readpst", "-r", "-o", output_dir, mbox_file], check=True)
        print(f"Conversion completed successfully! PST files saved in {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("readpst tool is not installed or not found in PATH.")

if __name__ == "__main__":
    # Example usage
   mbox_file = "C:/path/to/your/file.mbox"
output_dir = "C:/path/to/output/folder"
    
    convert_mbox_to_pst(mbox_file, output_dir)
