import abc
import model

# Port AbstractRepository
# SOLID principle identified: Liskov Substitution 
class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, task: model.Task):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Task:
        raise NotImplementedError


# DESIGN PATTERN IMPLEMENTED: STRATEGY
class SqlAlchemyRepository():
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Batch).all()

class FakeRepository():
    def __init__(self, batches):
        self.batches = set(batches)        