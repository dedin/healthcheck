from abc import ABCMeta, abstractmethod


class BaseTrendAnalyzer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_trend(self, resolution, threshold, interval, results_list):
        pass
