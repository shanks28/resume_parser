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
async def get_match(summary:str,jd_summary:str):
    pass
if __name__=="__main__":
    print(generate_summary(content="""""",
                     skills=[]))
