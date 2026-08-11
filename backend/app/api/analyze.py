from datetime import datetime


def analyze_business(files):
    """MVP analysis entry point.
    Accepts uploaded business files and returns analysis task result.
    """
    return {
        "status": "completed",
        "created_at": datetime.utcnow().isoformat(),
        "files": files,
        "metrics": {
            "revenue": 0,
            "cost": 0,
            "profit": 0,
            "margin": 0
        }
    }
