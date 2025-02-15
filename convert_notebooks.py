import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_marimo() -> bool:
    """Verify marimo is installed and accessible."""
    try:
        subprocess.run(['marimo', '--version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        logging.error("marimo is not installed or not accessible. Please install it using: pip install marimo")
        return False

def find_ipynb_files(lab_dirs: List[str]) -> List[Path]:
    """Find all .ipynb files in the specified directories."""
    ipynb_files = []
    for lab_dir in lab_dirs:
        if not os.path.exists(lab_dir):
            logging.warning(f"Directory not found: {lab_dir}")
            continue
        
        for root, _, files in os.walk(lab_dir):
            for file in files:
                if file.endswith('.ipynb'):
                    ipynb_files.append(Path(root) / file)
    
    return ipynb_files

def convert_notebook(ipynb_path: Path) -> Tuple[bool, str]:
    """Convert a single notebook to marimo format."""
    output_path = ipynb_path.with_suffix('.py')
    
    try:
        result = subprocess.run(
            ['marimo', 'convert', str(ipynb_path), '-o', str(output_path)],
            capture_output=True,
            text=True,
            check=True
        )
        return True, f"Successfully converted {ipynb_path}"
    except subprocess.CalledProcessError as e:
        return False, f"Error converting {ipynb_path}: {e.stderr}"

def main():
    # Lab directories to process
    lab_dirs = ['lab1_fa24', 'lab2_fa24', 'lab3_fa24', 'lab5_fa24']
    
    if not setup_marimo():
        sys.exit(1)
    
    logging.info("Starting notebook conversion process...")
    
    # Find all notebooks
    ipynb_files = find_ipynb_files(lab_dirs)
    if not ipynb_files:
        logging.error("No .ipynb files found in the specified directories")
        sys.exit(1)
    
    logging.info(f"Found {len(ipynb_files)} notebook(s) to convert")
    
    # Track results
    successful = []
    failed = []
    
    # Convert each notebook
    for ipynb_path in ipynb_files:
        success, message = convert_notebook(ipynb_path)
        if success:
            successful.append(str(ipynb_path))
            logging.info(message)
        else:
            failed.append(str(ipynb_path))
            logging.error(message)
    
    # Print summary
    print("\nConversion Summary:")
    print(f"Successfully converted: {len(successful)}")
    print(f"Failed conversions: {len(failed)}")
    
    if failed:
        print("\nFailed notebooks:")
        for notebook in failed:
            print(f"- {notebook}")

if __name__ == "__main__":
    main() 