def filter_stage(input_queue, output_queue, filter_pipeline):
    while True:
        frame = input_queue.get()
        if frame is None:
            break
        processed_frame = filter_pipeline.apply(frame)
        output_queue.put(processed_frame)
