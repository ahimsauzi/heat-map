from pentagon_radar_chart import PentagonRadarChart
import argparse


def run_direct_input_example(output_path=None):
    """Example using direct input of categories and scores"""
    categories = ["IAM", "Detection", "Data Protection",
                  "Infrastructure Protection", "Incident Response"]
    scores = [75, 60, 85, 70, 65]

    chart = PentagonRadarChart(
        categories, scores, title="Security Posture Assessment")
    chart.draw_chart(save_path=output_path)


def run_csv_example(csv_path, title="Security Posture from CSV", output_path=None):
    """Example using CSV input"""
    chart = PentagonRadarChart.from_csv(csv_path, title=title)
    chart.draw_chart(save_path=output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate Pentagon Radar Chart')
    parser.add_argument('--csv', type=str, help='Path to CSV file')
    parser.add_argument('--title', type=str, default="Security Posture Assessment",
                        help='Title for the chart')
    parser.add_argument('--output', type=str,
                        help='Output file path (e.g., chart.png)')

    args = parser.parse_args()

    if args.csv:
        run_csv_example(args.csv, args.title, args.output)
    else:
        run_direct_input_example(args.output)
