"""Metrics that separate acknowledgment, delivery, and side effects."""

def summarize(result, total):
    if total < 1: raise ValueError('total must be positive')
    return {
        'strategy': result.strategy,
        'operations': total,
        'acknowledged': len(result.completed_ids),
        'completion_pct': round(100 * len(result.completed_ids) / total, 2),
        'attempts': len(result.attempts),
        'side_effects': len(result.side_effect_ids),
        'duplicate_effects': result.duplicate_effects,
    }
