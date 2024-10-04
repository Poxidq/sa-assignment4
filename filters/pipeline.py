class FilterPipeline:
    def __init__(self, filters):
        self.filters = filters

    def apply(self, frame):
        for filter_obj in self.filters:
            frame = filter_obj.apply(frame)
        return frame
