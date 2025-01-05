import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi


class PentagonRadarChart:
    def __init__(self, categories, scores, title="Pentagon Radar Chart", num_levels=5):
        if len(categories) != 5 or len(scores) != 5:
            raise ValueError(
                "Both categories and scores must have exactly 5 elements")
        if not all(0 <= score <= 100 for score in scores):
            raise ValueError("Scores must be between 0 and 100")

        self.categories = categories
        self.scores = scores
        self.title = title
        self.num_levels = num_levels

        # Rotate angles to start from top (90 degrees)
        self.angles = [(n / float(len(categories)) * 2 * pi) + (pi/2)
                       for n in range(len(categories))]
        self.angles += [self.angles[0]]  # Complete the pentagon
        self.scores = scores + [scores[0]]  # Complete the scores

    @classmethod
    def from_csv(cls, csv_path: str, title: str = "Pentagon Radar Chart") -> 'PentagonRadarChart':
        """Create a PentagonRadarChart instance from a CSV file."""
        df = pd.read_csv(csv_path)
        categories = df['category'].tolist()
        scores = df['score'].tolist()
        return cls(categories, scores, title=title)

    def draw_pentagon_grid(self, ax, color="grey"):
        """Draw pentagon-shaped gridlines."""
        for level in range(1, self.num_levels + 1):
            values = [level / self.num_levels * 100] * len(self.categories)
            values += values[:1]  # Close the pentagon
            ax.plot(self.angles, values, color=color,
                    linestyle='dashed', linewidth=0.5, alpha=0.7)

    def draw_diagonal_lines(self, ax, color="grey"):
        """Draw diagonal lines from center to vertices."""
        for angle, score in zip(self.angles[:-1], self.scores[:-1]):
            ax.plot([angle, angle], [0, score], color=color,
                    linestyle='dashed', linewidth=0.5, alpha=0.7)

    def draw_chart(self, save_path=None):
        """Draw the pentagon radar chart."""
        # Create figure with a transparent background
        fig = plt.figure(figsize=(10, 10))
        fig.patch.set_alpha(0)

        ax = fig.add_subplot(111, projection='polar')
        ax.patch.set_alpha(0)

        # Plot the scores and fill the pentagon
        ax.plot(self.angles, self.scores, 'o-', linewidth=2)
        ax.fill(self.angles, self.scores, alpha=0.25)

        # Draw pentagon grid and diagonal lines
        self.draw_pentagon_grid(ax)
        self.draw_diagonal_lines(ax)

        # Remove all spines, labels, and ticks
        ax.spines['polar'].set_visible(False)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.grid(False)

        # Set limits
        ax.set_ylim(0, 100)

        # Define label positions (adjusted for clockwise order from top)
        # Define label positions (clockwise from top)
        label_radius = 105
        label_positions = [
            (pi/2, label_radius, 'center', 'bottom'),          # IAM (top, 90°)
            # Detection (right-top, 18°)
            (pi*0.1, label_radius, 'left', 'center'),
            # Data Protection (right-bottom, -54°)
            (-pi*0.3, label_radius, 'left', 'center'),
            # Infrastructure Protection (bottom, -90°)
            (pi*1.3, label_radius, 'center', 'top'),
            # Incident Response (left-top, 162°)
            (pi*0.9, label_radius, 'right', 'center'),
        ]

        # Add category labels
        for (angle, radius, ha, va), category in zip(label_positions, self.categories):
            ax.text(angle, radius, category,
                    ha=ha, va=va,
                    size=11)

        # Remove margins and make plot tight
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path,
                        bbox_inches='tight',
                        transparent=True,
                        dpi=300,
                        pad_inches=0.1)
            plt.close()
        else:
            plt.show()
