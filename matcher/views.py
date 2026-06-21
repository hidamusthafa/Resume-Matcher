from django.shortcuts import render
from groq import Groq

client = Groq(api_key="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")

def index(request):
    result = None
    
    if request.method == 'POST':
        resume = request.POST.get('resume', '')
        job_description = request.POST.get('job_description', '')
        
        prompt = f"""
        You are an expert HR consultant and resume analyst.
        
        Analyse this resume against the job description and provide:
        1. A match score out of 100
        2. Top 3 strengths that match the job
        3. Top 3 missing skills or gaps
        4. 3 specific suggestions to improve the resume for this job
        
        Resume:
        {resume}
        
        Job Description:
        {job_description}
        
        Format your response clearly with headings for each section.
        """
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        result = response.choices[0].message.content
    
    return render(request, 'matcher/index.html', {'result': result})