from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from iot.models import Device, DeviceType

class IndexView(generic.ListView):
	template_name = 'iot/index.html'
	context_object_name = 'device_list'

	def get_queryset(self):
		"""Return list of devices."""
		return Device.objects.select_related('device_type').all()
		
class DeviceDetailView(generic.DetailView):
	model = Device
	template_name = 'iot/device_detail.html'
	context_object_name = 'device'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(DeviceDetailView, self).get_context_data(**kwargs)

		# Need to add current data points.  Should use api to ajax load historical vals and make chart
		# Add the related Pin objects  #pins are old news
		# context['device'].pins = Pin.objects.filter(device=self.object).order_by("name")
		return context


## from Polls tut for reference...still a noob

# class ResultsView(generic.DetailView):
# 	model = Poll
# 	template_name = 'polls/results.html'

# """
# def index(request):
# 	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]	
# 	context = {'latest_poll_list': latest_poll_list}
# 	return render(request, 'polls/index.html', context)    

# def detail(request, poll_id):
# 	poll = get_object_or_404(Poll, pk=poll_id)
# 	return render(request, 'polls/detail.html', {'poll': poll})

# def results(request, poll_id):
# 	poll = get_object_or_404(Poll, pk=poll_id)
# 	return render(request, 'polls/results.html', {'poll': poll})
# """
# def vote(request, poll_id):
# 	p = get_object_or_404(Poll, pk=poll_id)
# 	try:
# 		selected_choice = p.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):
# 		# Redisplay the poll voting form.
# 		return render(request, 'polls/detail.html', {
# 			'poll': p,
# 			'error_message': "You didn't select a choice.",
# 		})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		# Always return an HttpResponseRedirect after successfully dealing
# 		# with POST data.  This prevents data from being posted twice if a
# 		# user hits the back button.
# 		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
