from django.shortcuts import render, get_object_or_404, redirect
from .models import ChatGroup, GroupMessage
from django.contrib.auth.decorators import login_required
from .forms import ChatmessageCreateForm

# Create your views here.
@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    chat_messages = chat_group.chat_messages.all().order_by('-created')[:30]
    form = ChatmessageCreateForm()

    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message':message,
                'user': request.user
            }
            return render(request, 'a_rtchat/partials/chat_messages_p.html', context)

    print(f'Xabarlar soni: {chat_messages.count()}')
    return render(request, 'a_rtchat/chat.html', {'chat_messages': chat_messages, 'user':request.user, 'form':form})


# for g in ChatGroup.objects.all():
#     print(g.id, g.group_name)

# # Har bir xabar qaysi guruhga tegishli
# for m in GroupMessage.objects.all():
#     print(f"{m.body} -> {m.group.group_name}")