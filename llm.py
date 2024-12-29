from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from typing import List
async def generate_summary(content:str,skills:List[str]):
    llm=Ollama(model="llama2")
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
if __name__=="__main__":
    print(generate_summary(content="""Akash S H
♂phone+91 9480591537 /envel⌢pe1rn21cs016.akash@gmail.com
/githubgithub.com/shanks28 /codeleetcode.com/u/shanks28
Education
RNS Institute Of Technology Bangalore Dec 2021 – present
B.E. in Computer Science and Engineering
Experience
Project Intern Jan 2024 – April 2024
Samskrithi Foudation -NGO / Social Services Remote
•Developed a crowd sourced Digital Library , Veda-Vault, using Django REST framework, Postman .
•Managed and hosted services on AWS EC2 , performed troubleshooting, and interacted with EBS volumes to increase storage
capacity.
•Wrote Django code for user login and authentication.
•Digitized, validated, and preserved ancient Indian texts, making them globally accessible.
Certifications
•AWS Certified Cloud Practitioner.
•Programming, Data Structures, and Algorithms Using Python (NPTEL-Top 5% in Course).
•Java Programming Nanodegree (Udacity).
•AI Programming with Python Nanodegree (Udacity).
Projects
•AI For Content Repurposing |Python, FastAPI, Docker, OAuth 2.0, PostgreSQL, AWS, JWT
•Developed an automated system for generating text for social media platforms using Open-Souce models such as T5.
•Built a scalable backend infrastructure using FastAPI ,PostgreSQL , and Docker .
•Implemented OAuth 2.0 and JWT for authorization and authentication, ensuring safe access to user data.
•Reduced manual post rewriting time by 70%.
•Image Classifier |Python, Pytorch, VGG-16, AlexNet, ResNet, CNNs
•Created a Python application for training and predicting models on 120 different types of flowers.
•Utilized PyTorch for constructing and training Neural Networks .
•Applied techniques for image Normalization .
•Used Machine Learning concepts like Backpropagation and Feedforward propagation.
•Video Frame Interpolation (FILM) |Python, PyTorch, U-Net, AWS (S3)
•Enhanced video framerates using frame interpolation with the U-Net architecture and PyTorch .
•Developed a pipeline for video preprocessing , intermediate frame generation, and post-processing.
•Integrated AWS S3 for efficient storage and retrieval of large video files.
•Recognized as an innovative project for improving video smoothness and quality.
Skills
•Languages: Python,Java,Bash.
•Technologies and Frameworks: Spring Boot, JPA, Docker, Flask, Django, FastAPI, GitHub Actions, Git, PyTorch, Postman (API
Testing), JWT, Maven, Redis ,MatplotLib, Seaborn, Numpy,Pytorch.
•Cloud Platforms: AWS (EC2, EBS, S3).
•Database Experience: AWS RDS with MySQL, PostgreSQL and SQL scripting.
•Relevant Course work: Data Structures, Design and Analysis of Algorithms, Operating Systems (Linux), Database Management
Systems, Computer Networks, NoSQL.
Extra-Curricular Activities
•SUITS Hackathon:Built a cryptographic system for secure real-time communication between client and server using
WebSockets , achieving top 9 out of 20 teams.).
•Practiced Karate , honing discipline and focus while enjoying the thrill of tournaments and training sessions.""",
                     skills=['Python', 'Java', 'R', 'Django', 'Flask', 'Spring', 'SQL', 'PostgreSQL', 'MySQL', 'Redis', 'AWS', 'Docker', 'Git', 'PyTorch', 'Seaborn', 'Linux', 'Bash', 'GitHub', 'Postman', 'WebSockets', 'OAuth', 'JWT']))