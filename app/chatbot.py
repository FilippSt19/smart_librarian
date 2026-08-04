import json

from openai import OpenAI

from app.tests.config.settings import Config
from app.prompts import SYSTEM_PROMPT
from app.rag import RAGRetriever
from app.tools import BookTools


BOOK_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_summary_by_title",
            "description": (
                "Returns the complete summary of a book "
                "based on its exact title."
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


class SmartLibrarian:
    """
    AI chatbot that recommends books using
    Retrieval-Augmented Generation (RAG)
    and OpenAI Function Calling.
    """

    def __init__(self):

        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY
        )

        self.retriever = RAGRetriever()

        self.tools = BookTools()

    def build_context(
        self,
        documents: list[dict],
    ) -> str:
        """
        Build a context string from retrieved documents.
        """

        context_parts = []

        for document in documents:

            context_parts.append(
                (
                    f"Title: {document['title']}\n"
                    f"{document['document']}"
                )
            )

        return "\n\n".join(context_parts)

    def chat(
        self,
        query: str,
    ) -> str:
        """
        Generate a recommendation using
        RAG + Function Calling.
        """
        
        # Retrieve relevant documents

        documents = self.retriever.retrieve(
            query=query,
            n_results=Config.DEFAULT_N_RESULTS,
        )

        context = self.build_context(documents)

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"""
Context:

{context}

User request:

{query}
""",
            },
        ]
        
        # First LLM Call

        response = self.client.chat.completions.create(
            model=Config.CHAT_MODEL,
            temperature=Config.TEMPERATURE,
            messages=messages,
            tools=BOOK_TOOLS,
            tool_choice="auto",
        )

        message = response.choices[0].message

        # Normal response
    
        if not message.tool_calls:
            return message.content or "No response generated."
        
        # Tool Calling

        tool_call = message.tool_calls[0]

        function_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        tool_functions = {
            "get_summary_by_title":
                self.tools.get_summary_by_title,
        }

        if function_name not in tool_functions:
            raise ValueError(
                f"Unsupported tool: {function_name}"
            )

        tool_result = tool_functions[
            function_name
        ](**arguments)

       
        # Append assistant message
       
        messages.append(message)
        
        # Append tool result

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": tool_result,
            }
        )

        # Final LLM Call
        
        final_response = self.client.chat.completions.create(
            model=Config.CHAT_MODEL,
            temperature=Config.TEMPERATURE,
            messages=messages,
        )

        return (
            final_response
            .choices[0]
            .message
            .content
            or "No response generated."
        )