from django.shortcuts import render
from .romanizer import RomanizationModel

# Initialize the model globally
ai_model = RomanizationModel()

def index(request):
    context = {}
    
    if request.method == "POST":
        input_text = request.POST.get("text_input", "").strip()
        
        if input_text:
            # Process the text using the auto-detect function from the notebook
            result = ai_model.process(input_text)
            
            context['original_text'] = input_text
            context['romanized_output'] = result['output']
            context['target_lang'] = result['target_script']
            
    return render(request, "index.html", context)
