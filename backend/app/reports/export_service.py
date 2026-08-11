"""
Report Export Service
Support future Excel/PDF/CSV exports.
"""


def export_excel(report):
    return {
        "format": "xlsx",
        "data": report
    }


def export_csv(report):
    return {
        "format": "csv",
        "data": report
    }


def export_pdf(report):
    return {
        "format": "pdf",
        "data": report
    }
