from django.shortcuts import render, redirect
from . import models
from userApp.models import LibraryUser

def examine_list(request):

    comments = models.Comments.objects.filter(is_finished=False)

    return render(request, "examine_list.html", {'comments': comments})


def reject_op(request):
    comment_id = request.GET.get("comment_id")
    comment = models.Comments.objects.get(id=comment_id)
    user = LibraryUser.objects.get(id=comment.user_id)
    user.Comment = False
    user.save()
    comment.delete()
    return redirect('/examine/list')


def accept_op(request):
    comment_id = request.GET.get("comment_id")
    models.Comments.objects.filter(id=comment_id).update(is_finished=True)
    return redirect('/examine/list')
# Create your views here.
