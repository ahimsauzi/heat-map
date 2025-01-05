# Pentagon Radar Chart Generator

A Python tool for generating pentagon-shaped radar charts, primarily designed for security posture assessments. The chart displays five categories in a clockwise order from the top: IAM, Detection, Data Protection, Infrastructure Protection, and Incident Response.

## Features

- Generate pentagon radar charts with customizable scores and titles
- Support for direct input or CSV file loading
- Transparent PNG output
- Configurable chart appearance
- Command-line interface

## Example Usage

### Direct Python Usage

```python
# Using direct values
categories = ["IAM", "Detection", "Data Protection",
             "Infrastructure Protection", "Incident Response"]
scores = [75, 60, 85, 70, 65]

radar_chart = PentagonRadarChart(
    categories, scores, title="Security Posture Assessment")
radar_chart.draw_chart()

# From CSV file
radar_chart = PentagonRadarChart.from_csv("security_scores.csv")
radar_chart.draw_chart()
```

### Command Line Usage

Basic usage:

```bash
python generate_chart.py --output chart.png
```

With title:

```bash
python generate_chart.py --output chart.png --title "My Security Assessment"
```

Using CSV input:

```bash
python generate_chart.py --csv input.csv --output chart.png --title "Security Assessment from CSV"
```

Save to specific directory:

```bash
mkdir -p output
python generate_chart.py --output ./output/chart.png
```

## CSV File Format

The CSV file should be structured as follows:
| category | score |
|----------|-------|
| IAM | 75 |
| Detection | 60 |
| Data Protection | 85 |
| Infrastructure Protection | 70 |
| Incident Response | 65 |

Note: Categories in the CSV should follow the clockwise order from top: IAM, Detection, Data Protection, Infrastructure Protection, Incident Response.
