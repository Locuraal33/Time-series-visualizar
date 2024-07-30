# This entrypoint file to be used in development. Start by reading README.md
import time_series_visualizer
from unittest import main

# Test your function by calling it here
time_series_visualizer.draw_line_plot(filtered_df)
time_series_visualizer.draw_bar_plot(filtered_df)
time_series_visualizer.draw_box_plot(filtered_df)

# Run unit tests automatically
main(module='test_module', exit=False)