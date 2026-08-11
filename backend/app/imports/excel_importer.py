"""Excel import center for marketplace order files."""

SUPPORTED_TYPES = ["xlsx", "csv"]


def detect_file_type(filename: str):
    if filename.endswith('.xlsx'):
        return 'xlsx'
    if filename.endswith('.csv'):
        return 'csv'
    return 'unknown'


def create_import_job(filename: str, platform: str | None = None):
    return {
        "filename": filename,
        "platform": platform,
        "status": "pending"
    }
