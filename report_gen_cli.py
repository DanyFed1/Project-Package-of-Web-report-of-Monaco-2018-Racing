import argparse
import report_gen as rpg

def main():
    """Uses instance of report_gen classes to create the desired CLI report
    generation behavior"""
    parser = argparse.ArgumentParser(description="F1 Q1 Lap time Report Generator")
    parser.add_argument("--files", type=str, required=True,
                        help='Folder path containing start.log, end.log and abbreviation.txt files')
    parser.add_argument('--order', choices=['asc', 'desc'], default='asc',
                        help='Order of lap times (ascending or descending)')
    parser.add_argument('--driver', type=str, help='Get lap time information for a specific driver')

    args = parser.parse_args()

    processor = rpg.Q1Processor(args.files)
    report_generator = rpg.Q1ReportGenerator(processor)

    if args.driver:
        print(report_generator.driver_info(args.driver))
    else:
        report_generator.print_report(args.order)

if __name__ == "__main__":
    main()

# #Example usage:
# python report_gen_cli.py --files /Users/daniilfjodorov/Desktop/CodingProjects/Foxminded/Task_6_Report_of_Monaco_2018_Racing/pythonProject/files
# python report_gen_cli.py --files /Users/daniilfjodorov/Desktop/CodingProjects/Foxminded/Task_6_Report_of_Monaco_2018_Racing/pythonProject/files --order desc
# python report_gen_cli.py --files /Users/daniilfjodorov/Desktop/CodingProjects/Foxminded/Task_6_Report_of_Monaco_2018_Racing/pythonProject/files --driver "Sebastian Vettel"
