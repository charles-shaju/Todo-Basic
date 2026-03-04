import json

from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from .models import Todo


def home(request):
	return render(request, 'core/home.html')


@require_http_methods(['GET', 'POST'])
def todos(request):
	if request.method == 'GET':
		data = [
			{'id': t.id, 'text': t.text, 'done': t.done, 'created_at': t.created_at.isoformat()}
			for t in Todo.objects.all()
		]
		return JsonResponse({'items': data})

	try:
		payload = json.loads(request.body.decode('utf-8') or '{}')
	except json.JSONDecodeError:
		return HttpResponseBadRequest('Invalid JSON')

	text = (payload.get('text') or '').strip()
	if not text:
		return HttpResponseBadRequest('text is required')

	todo = Todo.objects.create(text=text)
	return JsonResponse({'id': todo.id, 'text': todo.text, 'done': todo.done}, status=201)


@require_http_methods(['POST'])
def toggle_todo(request, todo_id: int):
	todo = get_object_or_404(Todo, pk=todo_id)
	todo.done = not todo.done
	todo.save(update_fields=['done'])
	return JsonResponse({'id': todo.id, 'done': todo.done})

