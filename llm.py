from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List
llm = Ollama(model="llama2")

async def generate_summary(content:str,skills:List[str])->str:
    prompt_template='''
    Analyze the following resume and provide a concise summary:
    Resume: {resume_text}
    Skills:{skills}
    
    Summary should include:
    1. Key skills and technologies
    2. Educational background
    '''
    prompt=PromptTemplate(
        input_variables=['resume_text','skills'],
        template=prompt_template,
    )
    chain=LLMChain(llm=llm,prompt=prompt)
    summary=chain.run(resume_text=content,skills=skills)
    return summary
def get_match(summary:str,jd_summary)->str:
    template="""Give me only a match score number and suggest a few short improvements for the the following JD and the Following resume summary.Use Depp contexts
    {JD}:
    {resume_summary}:"""
    prompt=PromptTemplate(
        input_variables=['JD',"resume_summary"],
        template=template
    )
    chain=LLMChain(llm=llm,prompt=prompt)
    score=chain.run(JD=jd_summary,resume_summary=summary)
    return score
if __name__=="__main__":
    print(generate_summary(content="""""",
                     skills=[]))
    print(get_match(jd_summary="We are looking for a Backend Developer who is proficient in Python and has experience with frameworks like FastAPI or Flask. The ideal candidate should have experience working with databases like MongoDB and PostgreSQL, as well as knowledge of Docker and CI/CD pipelines."
                    ,summary="Based on the provided resume, here is a concise summary of Akash S H's skills and experiences:\n\nKey Skills and Technologies:\n\n* Strong proficiency in Python, Java, Bash, and various frameworks (Django, Flask, Spring, FastAPI)\n* Experience with cloud platforms (AWS, Docker) and databases (MySQL, PostgreSQL, RDS)\n* Proficient in using machine learning libraries (PyTorch) and API testing tools (Postman)\n* Knowledgeable about security protocols (OAuth, JWT) and containerization (Docker)\n\nEducational Background:\n\n* Currently pursuing B.E. in Computer Science and Engineering at RNS Institute Of Technology Bangalore\n* Relevant coursework in algorithms and data structures, machine learning, operating systems, and database management systems\n\nExperience:\n\n* Project Intern at Samskrithi Foudation -NGO / Social Services, where he developed a crowd-sourced digital library using Django REST framework and managed services on AWS EC2\n* Developed a back-end task management system for efficient task creation, updates, and notifications using Twilio and implemented real-time notifications via polling and messaging services\n* Built an automated system for generating text for social media platforms using T5 and developed a scalable backend infrastructure using FastAPI, PostgreSQL, and Docker\n* Developed an image classifier using PyTorch and trained models (VGG-16, AlexNet, ResNet) on 120 flower types\n* Enhanced video framerates using frame interpolation with U-Net architecture and PyTorch\n\nExtra-Curricular Activities:\n\n* Participated in SUITS Hackathon and built a cryptographic system for secure real-time communication between client and server using WebSockets, achieving top 9 out of 20 teams.\n* Practiced Karate to hone discipline and focus while enjoying the thrill of tournaments and training sessions."))

