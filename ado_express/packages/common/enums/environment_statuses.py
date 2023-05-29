from .base_enum import BaseEnum


class ReleaseEnvironmentStatuses:
    class InProgress(BaseEnum):
        IN_PROGRESS = 'inProgress'
        QUEUED = 'queued'
        SCHEDULED = 'scheduled'

    class Succeeded(BaseEnum):
        SUCCEEDED = 'succeeded'
        PARTIALLY_SUCCEEDED = 'partiallySucceeded'
        
    class NotStarted(BaseEnum):
        NOT_STARTED = 'notStarted'

    class Failed(BaseEnum):
        FAILED = 'failed'
        CANCELED = 'canceled'
        REJECTED = 'rejected'
    
    class Undefined(BaseEnum):
        UNDEFINED = 'undefined'