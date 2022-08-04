from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.
def index(request):
    return render(request, 'index.html')

def check_regex(request):
    print(request.POST)

    user_input_dict = request.POST
    regex_string = str(user_input_dict['regex'])
    text_string = str(user_input_dict['text'])
    check = "0"
    try:
        check = request.POST["check"]  #causing error when unchecked
    except:
        pass
    count = 0

    string_list = text_string.split("\r\n")
    #print(string_list)
    output_text = list()
    if check == '1':
        for i in string_list:
            if bool(re.search(regex_string,i,re.IGNORECASE)):
                output_text.append(i)
                count+=1
    else:
        for i in string_list:
            if bool(re.search(regex_string,i)):
                output_text.append(i)
                count+=1
    print(count)

    return render(request, 'index.html', {'output' : output_text})