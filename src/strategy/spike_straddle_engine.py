from typing import Dict, Any

class SpikeStraddleEngine:
    """
    Detects high-impact candlestick velocity post-release and computes breakout direction.
    """
    @staticmethod
    def evaluate_breakout(initial_price: float, current_price: float, elapsed_seconds: float) -> Dict[str, Any]:
        delta_pips = (current_price - initial_price) * 10000
        is_breakout = abs(delta_pips) >= 12.0
        direction = "CALL" if delta_pips > 0 else "PUT"
        
        return {
            "delta_pips": round(delta_pips, 2),
            "elapsed_seconds": elapsed_seconds,
            "is_valid_breakout": is_breakout,
            "direction": direction,
            "recommended_expiry_seconds": 60,
            "confidence": 0.94 if is_breakout else 0.50
        }
