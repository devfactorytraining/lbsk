from dotenv import load_dotenv
load_dotenv()

#model 
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system","You are good with summarizing text. Follow these instructions: {instructions}"),
    ("user","{text}")
])

quest = "Kerala (English: /ˈkɛrələ/ ⓘ/ KERR-ə-lə), called Keralam in Malayalam (Malayalam: [keːɾɐɭɐm] ⓘ), is a state on the Malabar Coast of India.[15] It was formed on 1 November 1956, following the passage of the States Reorganisation Act, by combining Malayalam-speaking regions of the erstwhile regions of Cochin, Malabar, South Canara, and Travancore.[16][17] Spread over 38,863 km2 (15,005 sq mi), Kerala is the 21st largest Indian state by area. It is bordered by Karnataka to the north and northeast, Tamil Nadu to the east and south, and the Lakshadweep Sea[18] to the west. With 33 million inhabitants as per the 2011 census, Kerala is the 13th-largest Indian state by population. It is divided into 14 districts with the capital being Thiruvananthapuram. Malayalam is the most widely spoken language and is also the official language of the state.[19]The Chera dynasty was the first prominent kingdom based in Kerala. The Ay kingdom in the deep south and the Ezhimala kingdom in the north formed the other kingdoms in the early years of the Common Era (CE). The region had been a prominent spice exporter since 3000 BCE.[20] The region's prominence in trade was noted in the works of Pliny as well as the Periplus around 100 CE. In the 15th century, the spice trade attracted Portuguese traders to Kerala, and paved the way for European colonisation of India. At the time of Indian independence movement in the early 20th century, there were two major princely states in Kerala: Travancore and Cochin. They united to form the state of Thiru-Kochi in 1949. The Malabar region, in the northern part of Kerala,"
instruct = "Tell is 3 sentences"

#Output Parser
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# result = chain.invoke({"question":"What is langchain","instructions": "Tell in 5 sentences"})

result= chain.invoke({"instructions":instruct, "text":quest})
print(result)





