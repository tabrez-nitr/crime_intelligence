from langchain_core.messages import SystemMessage

from app.ai.llm import llm
from app.ai.prompts import SYSTEM_PROMPT


def agent_node(state):

    messages = [

        SystemMessage(
            content=SYSTEM_PROMPT
        ),

        *state["messages"]

    ]

    response = llm.invoke(messages)

    return {

        "messages": [response]

    }