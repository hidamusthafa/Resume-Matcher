from django.shortcuts import render
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6KKdvb6v_UnTlE70kuxXS7k6a36HXPC_QqTY4u3Ikuttw")

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
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        result = response.text
    
    return render(request, 'matcher/index.html', {'result': result})