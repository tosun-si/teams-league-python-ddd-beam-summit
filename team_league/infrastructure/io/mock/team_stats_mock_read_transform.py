from typing import List

import apache_beam as beam
from apache_beam import PTransform
from apache_beam.pvalue import PBegin

from team_league.domain.team_scorer_raw import TeamScorerRaw
from team_league.domain.team_stats_raw import TeamStatsRaw

psg_scorers: List[TeamScorerRaw] = [
    TeamScorerRaw(scorerFirstName="Kylian", scorerLastName="Mbappe", goals=15, goalAssists=6, games=13),
    TeamScorerRaw(scorerFirstName="Sa Silva", scorerLastName="Neymar", goals=11, goalAssists=7, games=12),
    TeamScorerRaw(scorerFirstName="Angel", scorerLastName="Di Maria", goals=7, goalAssists=8, games=13),
    TeamScorerRaw(scorerFirstName="Lionel", scorerLastName="Messi", goals=12, goalAssists=8, games=13),
    TeamScorerRaw(scorerFirstName="Marco", scorerLastName="Verrati", goals=3, goalAssists=10, games=13)
]

real_scorers: List[TeamScorerRaw] = [
    TeamScorerRaw(scorerFirstName="Karim", scorerLastName="Benzema", goals=14, goalAssists=7, games=13),
    TeamScorerRaw(scorerFirstName="Junior", scorerLastName="Vinicius", goals=9, goalAssists=6, games=12),
    TeamScorerRaw(scorerFirstName="Luca", scorerLastName="Modric", goals=5, goalAssists=9, games=11),
    TeamScorerRaw(scorerFirstName="Silva", scorerLastName="Rodrygo", goals=7, goalAssists=5, games=13),
    TeamScorerRaw(scorerFirstName="Marco", scorerLastName="Asensio", goals=6, goalAssists=3, games=13)
]

team_stats: List[TeamStatsRaw] = [
    TeamStatsRaw(teamName="PSG", teamScore=30, scorers=psg_scorers),
    TeamStatsRaw(teamName="Real", teamScore=25, scorers=real_scorers)
]


class TeamStatsMockReadTransform(PTransform):

    def __init__(self):
        super().__init__()

    def expand(self, inputs: PBegin):
        return inputs | 'Read mocked teams stats raw' >> beam.Create(team_stats)
