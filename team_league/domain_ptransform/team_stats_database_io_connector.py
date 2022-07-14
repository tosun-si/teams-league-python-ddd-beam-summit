from abc import abstractmethod, ABCMeta

from apache_beam import PTransform


class TeamStatsDatabaseIOConnector(metaclass=ABCMeta):

    @abstractmethod
    def write_team_stats(self) -> PTransform:
        pass
