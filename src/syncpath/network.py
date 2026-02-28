"""Network availability, delays, and loss sampled deterministically."""
import random

class Network:
    def __init__(self, windows, seed=0):
        self.windows = tuple(sorted(windows, key=lambda w:w.start_ms))
        self.rng = random.Random(seed)

    def at(self, time_ms):
        for window in self.windows:
            if window.start_ms <= time_ms < window.end_ms:
                return window
        return None

    def transmit(self, at_ms):
        window = self.at(at_ms)
        if window is None or not window.available:
            return False, 0, 'offline'
        if self.rng.random() < window.packet_loss:
            return False, window.latency_ms, 'packet-loss'
        # Transmission succeeds only if connectivity lasts through transit.
        arrival = at_ms + window.latency_ms
        end_window = self.at(max(at_ms, arrival - 1))
        if end_window is None or not end_window.available:
            return False, window.latency_ms, 'handoff-interruption'
        return True, window.latency_ms, 'delivered'
