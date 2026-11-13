"""Temporal knowledge graph with time-bounded fact validity."""
import time
from typing import Dict, List, Optional, Tuple, Any

class TemporalFact:
    def __init__(self, subject: str, predicate: str, obj: str, valid_from: float, valid_to: Optional[float] = None):
        self.subject = subject
        self.predicate = predicate
        self.obj = obj
        self.valid_from = valid_from
        self.valid_to = valid_to  # None implies indefinitely valid into future

    def is_valid_at(self, query_time: float) -> bool:
        if query_time < self.valid_from:
            return False
        if self.valid_to is not None and query_time > self.valid_to:
            return False
        return True

class TemporalKnowledgeGraph:
    """Anchors facts to explicit temporal validity intervals."""

    def __init__(self):
        self.facts: List[TemporalFact] = []

    def assert_fact(self, subject: str, predicate: str, obj: str, valid_from: float, valid_to: Optional[float] = None) -> TemporalFact:
        # Check if an existing open fact for subject+predicate exists and cap its interval
        if valid_to is None:
            for f in self.facts:
                if f.subject == subject and f.predicate == predicate and f.valid_to is None:
                    f.valid_to = valid_from

        fact = TemporalFact(subject, predicate, obj, valid_from, valid_to)
        self.facts.append(fact)
        return fact

    def query(self, subject: str, predicate: str, at_time: float) -> Optional[str]:
        for f in self.facts:
            if f.subject == subject and f.predicate == predicate and f.is_valid_at(at_time):
                return f.obj
        return None

    def history(self, subject: str, predicate: str) -> List[Tuple[float, Optional[float], str]]:
        res = []
        for f in self.facts:
            if f.subject == subject and f.predicate == predicate:
                res.append((f.valid_from, f.valid_to, f.obj))
        res.sort(key=lambda x: x[0])
        return res
