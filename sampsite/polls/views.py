from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


# Create your views here.
class IndexView(generic.ListView):
    ''' Index view of the polls page '''
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        ''' Return the last five published questions '''
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    ''' Detail view of the polls page '''
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        ''' Exclude questions that aren't published yet '''
        return Question.objects.filter(pub_date__lte=timezone.now()) 
    
class ResultsView(generic.DetailView):
    ''' Results view of the polls page '''
    model = Question
    template_name = 'polls/results.html'


# def index(request):
#     ''' Polls index page '''
#     # - shows here sort descending by pub_date
#     latest_questions_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_questions_list': latest_questions_list
#     }
#     return render(request, 'polls/index.html', context)

#     # output = '\n'.join(q.question_text for q in latest_questions_list)
#     # return HttpResponse(output)
#     # return HttpResponse("Hello, world. You're at the polls index.")


# def detail(request, question_id):
#     ''' Polls detail page '''
#     print(f"detail: {question_id}")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     #return HttpResponse(f"You're looking at question {question_id}.")


# def results(request, question_id):
#     ''' Polls results page '''
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # response = f"You're looking at the results of question {question_id}."
#     # return HttpResponse(response)


def vote(request, question_id):
    ''' Polls vote page '''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    #     # return HttpResponse(f"You're voting on question {question_id}.")
    # return HttpResponse(f"You're voting on question {question_id}.")
