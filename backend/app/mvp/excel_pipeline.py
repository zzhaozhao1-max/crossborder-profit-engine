"""
V4.3 Excel processing pipeline
Handles uploaded order, settlement and cost files.
"""

class ExcelPipeline:
    def process(self, files):
        return {
            "status": "ready",
            "files": files,
            "steps": [
                "detect_platform",
                "parse_orders",
                "match_settlement",
                "calculate_profit"
            ]
        }
