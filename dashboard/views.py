from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse_lazy

from braces.views import LoginRequiredMixin

from django.views.generic import CreateView, DeleteView, UpdateView, FormView, TemplateView, View

from .forms import CreateBookmarkForm, EditBookmarkForm
from .models import Bookmark, Tag, BookmarkTag
from django.contrib.auth.models import User


class DashboardIndex(LoginRequiredMixin, CreateView):

    template_name = 'dashboard/index.html'
    login_url = 'action:login'
    raise_exception = False
    form_class = CreateBookmarkForm

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        bookmark.save()

        user_tags = form.cleaned_data.get('tags').replace(" ", "").split(",")
        for u_tag in user_tags:
            try:
                tag = Tag.objects.get(tag=u_tag)
            except:
                new_tag = Tag(tag=u_tag.lower())
                new_tag.save()
                tag = new_tag

            bookmark_tag = BookmarkTag(bookmark=bookmark, tag=tag)
            bookmark_tag.save()

        return redirect('dashboard:dashboard')

    def get_context_data(self):
        context = super(DashboardIndex, self).get_context_data()
        context['bookmarks'] = Bookmark.objects.filter(user_id=self.request.user.id).order_by('-updated')
        return context


class DeleteBookmark(LoginRequiredMixin, DeleteView):

    success_url = reverse_lazy('dashboard:dashboard')
    model = Bookmark
    login_url = 'action:login'
    raise_exception = False


class EditBookmark(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        bookmark_form = CreateBookmarkForm(self.request.POST)
        if bookmark_form.is_valid():
            bookmark = Bookmark.objects.get(pk=kwargs['pk'], user=self.request.user)
            bookmark.title = bookmark_form.cleaned_data.get('title')
            bookmark.link = bookmark_form.cleaned_data.get('link')
            bookmark.save()

            BookmarkTag.objects.filter(bookmark=bookmark).delete()

            user_tags = bookmark_form.cleaned_data.get('tags').replace(" ", "").split(",")
            for u_tag in user_tags:
                try:
                    tag = Tag.objects.get(tag=u_tag)
                except:
                    new_tag = Tag(tag=u_tag.lower())
                    new_tag.save()
                    tag = new_tag

                bookmark_tag = BookmarkTag(bookmark=bookmark, tag=tag)
                bookmark_tag.save()

            return redirect('dashboard:dashboard')
