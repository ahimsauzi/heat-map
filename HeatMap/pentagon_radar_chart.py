import matplotlib.pyplot as plt
from math import pi


class PentagonRadarChart:
    def __init__(self, categories, scores, title="Pentagon Radar Chart", num_levels=5):
        """
        Initialize the radar chart parameters.

        :param categories: List of category names (labels on the axes).
        :param scores: List of scores corresponding to each category.
        :param title: Title of the chart.
        :param num_levels: Number of grid levels (concentric pentagons).
        """
        self.categories = categories
        self.scores = scores + scores[:1]  # Close the polygon
        self.title = title
        self.num_levels = num_levels
        self.angles = [n / float(len(categories)) *
                       2 * pi for n in range(len(categories))] + [0]

    def draw_pentagon_grid(self, ax, color="grey"):
        """
        Draw pentagon-shaped gridlines.

        :param ax: Matplotlib axis object.
        :param color: Color of the gridlines.
        """
        for level in range(1, self.num_levels + 1):
            values = [level / self.num_levels * 100] * len(self.categories)
            values += values[:1]  # Close the pentagon
            ax.plot(self.angles, values, color=color,
                    linestyle='dashed', linewidth=0.5, alpha=0.7)

    def draw_diagonal_lines(self, ax, color="grey"):
        """
        Draw diagonal lines connecting the center to the vertices.

        :param ax: Matplotlib axis object.
        :param color: Color of the diagonal lines.
        """
        for angle in self.angles[:-1]:  # Exclude the repeated angle for the closing point
            ax.plot([angle, angle], [0, 100], color=color,
                    linestyle='dashed', linewidth=0.5, alpha=0.7)

    def draw_chart(self):
        """
        Draw the pentagon radar chart.
        """
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

        # Plot the scores and fill the polygon
        ax.plot(self.angles, self.scores, linewidth=2,
                linestyle='solid', label='Scores')
        ax.fill(self.angles, self.scores, alpha=0.4)

        # Draw pentagon-shaped gridlines and diagonal lines
        self.draw_pentagon_grid(ax)
        self.draw_diagonal_lines(ax)

        # Remove the outer circle
        ax.spines['polar'].set_visible(False)

        # Remove radial percentage labels
        ax.set_yticks([])

        # Set the positions of the categories as pentagon corners
        ax.set_xticks(self.angles[:-1])
        ax.set_xticklabels(self.categories, size=12)

        # Adjust axis for aesthetics
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Title and legend
        ax.set_title(self.title, size=14, y=1.1)
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        # Show the chart
        plt.show()


# Example usage
categories = ["IAM", "Detection", "Data Protection",
              "Infrastructure Protection", "Incident Response"]
scores = [75, 60, 85, 70, 65]

# Create the chart object
radar_chart = PentagonRadarChart(
    categories, scores, title="Security Posture Assessment")
# Draw the chart
radar_chart.draw_chart()
