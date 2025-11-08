# import dependencies
from typing import TypedDict, List, Literal
from langchain_core.messages import BaseMessage
from pydantic import BaseModel,Field

# Pydantic schemas for structured output
class RouteDecision(BaseModel):
  route: Literal["rag","web","answer","end"]
  reply: str | None = Field(None, description="Filled only when route == 'end' ")

class RagJudge(BaseModel):
  sufficient: bool = Field(..., description="True if reterived information is sufficient to answer the user's question,False otherwise.")



#state: Shared data structure for agent
class AgentState(TypedDict,total=False):
  messages=List[BaseMessage]
  route: Literal["rag","web","answer","end"]
  rag:str
  web:str
  web_search_enabled: bool

# Node: for individual functions
