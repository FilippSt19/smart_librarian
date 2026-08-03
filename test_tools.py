from app.tools import BookTools

tools = BookTools()

summary = tools.get_summary_by_title(
    "The Hobbit"
)

print(summary)