from django.shortcuts import render, redirect, HttpResponse

turtles = {
"blue" : "ninjas/img/leonardo.jpg",
"orange" : "ninjas/img/michelangelo.jpg",
"red" : "ninjas/img/raphael.jpg",
"purple" : "ninjas/img/donatello.jpg",
"other" : "ninjas/img/notapril.jpg"
}

def index(request):
    if request.method == 'GET':
        response = HttpResponse("No Ninjas Here")
        return HttpResponse(response)
        return render(request, 'ninjas/index.html')

def ninjas (request):
    context = turtles
    return render(request, 'ninjas/index.html', context)

def solo(request, color):
    if color == 'red' or color == 'orange' or color == 'blue' or color == 'purple':
        context = {"selection" : turtles[color]}
        return render(request, 'ninjas/results.html', context)
    else:
        pic = turtles["other"]
        context2 = {"selection" : pic}
        print context2
        return render(request, 'ninjas/results.html', context2)

def april(request):
    pic = turtles["other"]
    context2 = {"selection" : pic}
    print context2
    return render(request, 'ninjas/results.html', context2)
