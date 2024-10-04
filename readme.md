# Team members
- Vadim Iarullin
- Aleksandr Efremov
- Nikita Sannikov
- Artur Lukianov
- Andrew Boronin

  
# Video Stream Processing with Pipes and Filters Pattern

This project implements the **Pipes and Filters** architectural pattern in Python. The application reads video frames either from a webcam or a video file and applies multiple filters (effects) in real time. Each filter is processed independently using threads, and a queue system passes frames between stages.

## Project Structure

- **video_source.py**: Captures video frames from the webcam or a video file.
- **filters.py**: Contains different filters to be applied (e.g., grayscale, mirror, resize, blur) and a `FilterPipeline` class that chains multiple filters.
- **display.py**: Displays the processed frames in a real-time window.
- **pipeline.py**: Manages the pipeline of stages (video capture, filter processing, display) and handles threading.
- **main.py**: The entry point that initializes the pipeline, defines the stages, and starts the application.


### Installing Dependencies

To install the required Python libraries:

```bash
pip install opencv-python
