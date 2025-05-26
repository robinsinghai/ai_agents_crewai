from crewai import Agent
from tools import yt_tool
import os

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_MODEL_NAME'] = "gpt-4o"

## Create a  senior blog content researcher

blog_reseracher = Agent(
    role="Blog reseracher from youtube videos",
    goal=" get the relevant video content from the topic {topic} from yt channel",
    verbose=True,
    memory=True,
    backstory="Expert in understanding videos in AI Data Science, Machine Learning and Gen AI and providing suggestion",
    tools=[yt_tool],
    allow_delegation=True
)


## Creating a senior blog writing agent with yt tool

blog_writer = Agent(
     role="Blog Writer",
     goal = 'Narrate compelling tech stories about the video {topic} from yt channel',
     verbose=True,
     memory=True,
     backstory="""With a flair for simplifying complex topics, you craft"
         "engaging narratives that captivate and educate, bringing new"
         "discoveries to ligth in an accessible manner.""",
     tools=[yt_tool],
     allow_delegation=False
)