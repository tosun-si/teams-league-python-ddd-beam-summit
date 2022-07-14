from abc import abstractmethod, ABCMeta

from apache_beam import PTransform


class TeamStatsInMemoryIOConnector(metaclass=ABCMeta):

    @abstractmethod
    def read_team_stats(self) -> PTransform:
        pass
