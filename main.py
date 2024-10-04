from filters import (
    BlackWhiteFilter,
    MirrorFilter,
    ResizeFilter,
    BlurFilter,
    FilterPipeline,
)
from stages.video_source import VideoSource
from stages.display import Display
from stages.filter_stage import filter_stage
from core.pipeline import Pipeline


def video_source_stage(input_queue, output_queue):
    video_source = VideoSource(0)
    video_source.start(output_queue)


def display_stage(input_queue, output_queue):
    display = Display()
    display.start(input_queue)


def main():
    filters = [BlackWhiteFilter(), MirrorFilter(), ResizeFilter(640, 480), BlurFilter()]
    filter_pipeline = FilterPipeline(filters)

    stages = [
        video_source_stage,
        lambda in_q, out_q: filter_stage(in_q, out_q, filter_pipeline),
        display_stage,
    ]

    pipeline = Pipeline(stages)
    pipeline.start()

    try:
        pipeline.threads[0].join()
    except KeyboardInterrupt:
        pass

    pipeline.stop()


if __name__ == "__main__":
    main()
