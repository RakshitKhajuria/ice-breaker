from tools.tools import get_profile_url
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType


def lookup(name: str) -> str:
    """
    Look up a person's name and return their LinkedIn profile URL.

    Args:
        name (str): The full name of the person.

    Returns:
        str: The URL of the person's LinkedIn profile page.
    """
    # Create a ChatOpenAI instance with specific settings
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Template for the prompt to generate the request for LinkedIn profile URL
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL"""

    # Create a Tool object for getting the LinkedIn profile URL
    tools_for_agent1 = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        ),
    ]

    # Initialize the agent with the necessary tools and settings
    agent = initialize_agent(
        tools_for_agent1, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    # Create a PromptTemplate object for the prompt with input variables
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    # Run the agent with the generated prompt and the person's name
    linkedin_username = agent.run(prompt_template.format_prompt(name_of_person=name))

    # Return the LinkedIn profile URL
    return linkedin_username
