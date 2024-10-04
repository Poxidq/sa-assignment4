from video_source import VideoSource
from filters import (
    BlackWhiteFilter,
    MirrorFilter,
    ResizeFilter,
    BlurFilter,
    FilterPipeline,
)
from display import Display
from pipeline import Pipeline


def video_source_stage(input_queue, output_queue):
    video_source = VideoSource(0)
    video_source.start(output_queue)


def filter_stage(input_queue, output_queue, filter_pipeline):
    while True:
        frame = input_queue.get()
        if frame is None:
            break
        processed_frame = filter_pipeline.apply(frame)
        output_queue.put(processed_frame)


def display_stage(input_queue, output_queue):
    display = Display()
    display.start(input_queue)


def main():
    # Define filters to be applied
    filters = [BlackWhiteFilter(), MirrorFilter(), ResizeFilter(640, 480), BlurFilter()]
    filter_pipeline = FilterPipeline(filters)

    # Create stages
    stages = [
        video_source_stage,  # Capture video from webcam
        lambda in_q, out_q: filter_stage(in_q, out_q, filter_pipeline),  # Apply filters
        display_stage,  # Display processed frames
    ]

    # Setup and run the pipeline
    pipeline = Pipeline(stages)
    pipeline.start()

    # Wait for threads to finish
    try:
        pipeline.threads[0].join()  # Wait for the video source thread to finish
    except KeyboardInterrupt:
        pass  # Gracefully handle Ctrl+C

    # Stop all threads and clean up
    pipeline.stop()


if __name__ == "__main__":
    main()
