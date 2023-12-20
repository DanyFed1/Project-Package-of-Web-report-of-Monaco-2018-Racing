#### F1 Q1 Lap Time Report Generator
This Python package provides a command-line interface (CLI) to generate a report of Formula 1 Q1 lap times. It processes log files containing start and end times of laps and driver abbreviations to rank drivers based on their lap times.

#### Features
Read and process start and end times from log files.
Integrate driver information from an abbreviation file.
Rank drivers based on lap times and generate a formatted report.
Command-line interface for easy interaction.

#### Installation
Before you begin, ensure you have Python installed on your system. This package is compatible with Python 3.8 and above.

#### Usage
The package can be run from the command line. It requires the path to a folder containing three specific files: start.log, end.log, and abbreviations.txt.

#### Command-Line Arguments
--files: (Required) Path to the folder containing the log files and abbreviations file.
--order: (Optional) Order of lap times (asc for ascending, desc for descending). Default is asc.
--driver: (Optional) Get lap time information for a specific driver.

###### Examples
1. Generate a report with lap times in ascending order: python report_gen_cli.py --files /path/to/data/files
2. Generate a report with lap times in descending order: python report_gen_cli.py --files /path/to/data/files --order desc
3. Get lap time information for a specific driver:

python report_gen_cli.py --files /path/to/data/files --driver "Sebastian Vettel"

Replace /path/to/data/files with the actual path to your data files.

##### File Formats
start.log and end.log
These files should contain the start and end times of each lap, respectively. Each line in these files follows the format:

[Driver Abbreviation][Date][Time]

Example: SVF2018-05-24_12:02:58.917

abbreviations.txt
This file contains the driver abbreviations along with the full driver name and team. Each line in this file follows the format:

[Driver Abbreviation][Full Driver Name][Team]

Example: SVF_Sebastian Vettel_FERRARI
