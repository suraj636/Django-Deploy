from django.http import JsonResponse

def hello_view(request):
    return JsonResponse({'message': 'Hello'})

def sum_view(request):
    try:
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        return JsonResponse({'sum': num1 + num2})
    except ValueError:
        return JsonResponse({'error': 'Invalid numbers'}, status=400)
