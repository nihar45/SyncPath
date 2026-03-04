"""Remote endpoint model, supporting optional idempotent writes."""

class Server:
    def __init__(self, idempotent=False):
        self.idempotent = idempotent
        self.applied = []
        self.seen = set()

    def receive(self, operation):
        if self.idempotent and operation.id in self.seen:
            return False
        self.applied.append(operation.id)
        self.seen.add(operation.id)
        return True
