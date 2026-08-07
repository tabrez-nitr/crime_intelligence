from typing import Annotated , TypedDict

from langgraph.graph.message import add_message 
from langchain_core.messages import AnyMessage 

class CrimeAgentState(TypedDict):

    messages : Annotated[
        list[AnyMessage],
        add_messages, # add merge messages in the list 
    ]