import sys
import traceback

class BaseBackend(object):
    """Provides a base class that custom backends can subclass. Also provides basic
    traceback and message parsing.
    
    The ``__init__`` takes these keyword arguments:
    
        ``exp`` -- The exception generated by your failure.
        
        ``queue`` -- The queue in which the ``Job`` was enqueued when it failed.
        
        ``payload`` -- The payload that was passed to the ``Job``.
        
        ``worker`` -- The worker that was processing the ``Job`` when it failed.
    
    """
    def __init__(self, exp, queue, payload, worker=None):
        excc, _, tb = sys.exc_info()
        
        self._exception = excc
        self._traceback = traceback.format_exc()
        self._worker = worker
        self._queue = queue
        self._payload = payload
    
    
    def _parse_traceback(self, trace):
        """Return the given traceback string formatted for a notification."""
        return trace
    
    def _parse_message(self, exc):
        """Return a message for a notification from the given exception."""
        return '%s: %s' % (exc.__class__.__name__, str(exc))
    