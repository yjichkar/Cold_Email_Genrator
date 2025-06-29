import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-70b-8192")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the
        following keys: `role`, `experience`, `skills` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """

           ### JOB DESCRIPTION:
        {job_description}

        ### INSTRUCTION:
        You are Yashwant, a skilled Business Analyst with a strong foundation in data analysis, product analytics, and business strategy.
    You have worked with companies like Upstox and Digitize Matrix, where you helped reduce campaign costs and improve product performance using data-driven insights.
    You are proficient in tools like SQL, Excel, Power BI, Python, and Tableau, and have experience working on projects involving Airbnb data, Spotify SQL analysis,
    and employee performance dashboards. You understand how to translate business requirements into actionable solutions and communicate with stakeholders effectively.

    Your task is to write a cold email to a potential client or employer regarding the job mentioned above, showcasing how your background and skills are
    aligned with their requirements.

    Focus on:
    - How your past work and projects are relevant to the job.
    - Your ability to use data to drive decisions and optimize outcomes.
    - Your collaborative and problem-solving mindset.

    Add the most relevant links from the following portfolio items if helpful: {link_list}

    Do not include a preamble.
    ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))