
BOOK_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_summary_by_title",
            "description": (
                "Returns the complete summary of a book based on its exact title."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": (
                            "The exact title of the recommended book."
                        ),
                    }
                },
                "required": ["title"],
            },
        },
    }
]
