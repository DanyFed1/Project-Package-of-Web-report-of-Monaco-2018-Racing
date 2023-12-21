#### F1 Q1 Lap Time Report Generator
This Python package provides a command-line interface (CLI) to generate a report of Formula 1 Q1 lap times. It processes log files containing start and end times of laps and driver abbreviations to rank drivers based on their lap times.

#### Features
Read and process start and end times from log files.
Integrate driver information from an abbreviation file.
Rank drivers based on lap times and generate a formatted report.
Command-line interface for easy interaction.

#### Installation
Before you begin, ensure you have Python installed on your system. This package is compatible with Python 3.8 and above.
You can install using pip install --index-url https://test.pypi.org/simple/ --no-deps f1-q1-report-generator-df1

#### Usage
The package can be run from the command line. It requires the path to a folder containing three specific files: start.log, end.log, and abbreviations.txt.

#### Command-Line Arguments
--files: (Required) Path to the folder containing the log files and abbreviations file.
--order: (Optional) Order of lap times (asc for ascending, desc for descending). Default is asc.
--driver: (Optional) Get lap time information for a specific driver.

###### Examples
1. Generate a report with lap times in ascending order: python -m report_gen_cli --files /path/to/data/files
2. Generate a report with lap times in descending order:  python -m report_gen_cli --files /path/to/data/files --order desc
3. Get lap time information for a specific driver: python -m report_gen_cli --files /path/to/data/files --driver "Sebastian Vettel"

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

###### PyPi page: 
https://test.pypi.org/project/f1-q1-report-generator-df1/0.0.7/

#### Example Generated Report:
1. Sebastian Vettel     | FERRARI                        | 0:01:04.415000
2. Valtteri Bottas      | MERCEDES                       | 0:01:12.434000
3. Stoffel Vandoorne    | MCLAREN RENAULT                | 0:01:12.463000
4. Kimi Räikkönen       | FERRARI                        | 0:01:12.639000
5. Fernando Alonso      | MCLAREN RENAULT                | 0:01:12.657000
6. Charles Leclerc      | SAUBER FERRARI                 | 0:01:12.829000
7. Sergio Perez         | FORCE INDIA MERCEDES           | 0:01:12.848000
8. Romain Grosjean      | HAAS FERRARI                   | 0:01:12.930000
9. Pierre Gasly         | SCUDERIA TORO ROSSO HONDA      | 0:01:12.941000
10. Carlos Sainz         | RENAULT                        | 0:01:12.950000
11. Nico Hulkenberg      | RENAULT                        | 0:01:13.065000
12. Brendon Hartley      | SCUDERIA TORO ROSSO HONDA      | 0:01:13.179000
13. Marcus Ericsson      | SAUBER FERRARI                 | 0:01:13.265000
14. Lance Stroll         | WILLIAMS MERCEDES              | 0:01:13.323000
15. Kevin Magnussen      | HAAS FERRARI                   | 0:01:13.393000
------------------------------------ELIMINATED------------------------------------
16. Esteban Ocon         | FORCE INDIA MERCEDES           | NO TIME COULD BE DETERMINED BASED ON INPUT FILES
17. Sergey Sirotkin      | WILLIAMS MERCEDES              | NO TIME COULD BE DETERMINED BASED ON INPUT FILES
18. Daniel Ricciardo     | RED BULL RACING TAG HEUER      | NO TIME COULD BE DETERMINED BASED ON INPUT FILES
19. Lewis Hamilton       | MERCEDES                       | NO TIME COULD BE DETERMINED BASED ON INPUT FILES
