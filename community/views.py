from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Community
from .forms import CommunityForm
from django.views.generic import ListView, DetailView,TemplateView

# Create your views here.

def community(request):
    contents = Community.objects.all()
    community_list = Community.objects.all().order_by('-id')
    paginator = Paginator(community_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'community_home.html', {'contents': contents, 'posts':posts})

def detail(request, id):
    data = get_object_or_404(Community, pk = id)
    return render(request, 'community_detail.html', {'data':data})

def new(request):
    if request.method == 'POST':
        community_form = CommunityForm(request.POST, request.FILES)
        if community_form.is_valid():
            community = community_form.save(commit=False)
            community.date = timezone.now() 
            community.author = request.user
            community.save()
            tags = request.POST.get('tags', '').split(',') 
            for tag in tags:
                tag = tag.strip()
                community.tags.add(tag)
            return redirect('community:community')
    else:
        community_form = CommunityForm()
        return render(request, 'community_new.html', {'form':community_form})

def edit(request, id):
    post = get_object_or_404(Community, pk = id)
    if request.method == 'GET':
        community_form = CommunityForm(instance = post)
        return render(request, 'community_edit.html', {'edit_community' : community_form, 'community' : post})
    else:
        community_form = CommunityForm(request.POST, request.FILES, instance = post)
        if community_form.is_valid():
            community = community_form.save(commit=False)
            community.date = timezone.now() 
            community.save()
            tags = request.POST.get('tags', '').split(',') 
            for tag in tags:
                tag = tag.strip()
                community.tags.add(tag)
        return redirect('community:community_detail', community.id)

def delete(request, id):
    erase_community = Community.objects.get(id = id)
    if request.user == erase_community.author:
        erase_community.delete()
    return redirect('community:community')

# ArchiveView

class TagCloudTV(TemplateView):
    template_name = 'taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit_post_list.html'
    model = Community

    def get_queryset(self):
        return Community.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context