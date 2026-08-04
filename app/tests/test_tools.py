from app.engine.tools.summary_tool import BookTools

tools = BookTools()

summary = tools.get_summary_by_title(
    "The Hobbit"
)

print(summary)