from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from transformers import pipeline

@csrf_exempt
def summarize(request):
    summarizer = pipeline("summarization")

    if request.method == 'POST':
        article = request.POST.get('article', '')
        print(f"Input Article: {article}")

        if article:
            try:
                summary_result = summarizer(article, max_length=130, min_length=30, do_sample=False)
                print(f"summary_result[0]: {summary_result[0]}")

                if summary_result:
                    summary = summary_result[0].get('summary_text', 'Default Summary')
                else:
                    summary = 'No summary available'
                return render(request, 'nlp/summary.html', {'article': article, 'summary': summary})
            except IndexError:
                # Handle the case when the summary_result list is empty
                print("IndexError: summary_result list is empty")
                return render(request, 'nlp/summary.html', {'article': article, 'summary': 'No summary available'})
            except KeyError:
                # Handle the case when 'summary_text' key is not present
                print("KeyError: 'summary_text' key is not present")
                return render(request, 'nlp/summary.html', {'article': article, 'summary': 'Default Summary'})

    return render(request, 'nlp/summarize.html')
