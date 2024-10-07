from dotenv import load_dotenv
load_dotenv()
#model 
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#prompts
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer. Follow the instructions.{instructions}"),
    ("user", "{user_ask}")
]) 



input = "how can langchain help with testing?"
instruct = "Write in 20 words"
chain=prompt | llm

# chain = prompt
result = chain.invoke({"user_ask": input,"instructions":instruct})
print(result)
