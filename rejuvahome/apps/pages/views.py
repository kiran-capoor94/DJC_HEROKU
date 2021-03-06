from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm
from apps.blogs.models import Blog


def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    contact_form = ContactForm(request.POST or None)
    confirm_message = None
    posts = Blog.objects.published().order_by('-timestamp')[0:3]
    context = {
        "title": "Rejuva Aesthetica | Home",
        # "content":" Welcome to the homepage.",
        "form": contact_form,
        "blog": posts,

    }
    if contact_form.is_valid():
        # print(contact_form.cleaned_data)
        # Adding contact form functionality
        full_name = contact_form.cleaned_data['full_name']
        content = contact_form.cleaned_data['content']
        phone_number = contact_form.cleaned_data['phone_number']
        subject = 'Sent from RejuvaAesthetica.com'
        emailFrom = contact_form.cleaned_data['email']
        message = '%s %s %s %s' % (content, full_name, emailFrom, phone_number)
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
        confirm_message = "Thanks for the message. We will get right back to you."  # noqa

        if request.is_ajax():
            return JsonResponse({"message": confirm_message})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')  # noqa
    # if request.user.is_authenticated():
    #     context["premium_content"] = "YEAHHHHHH"
    return render(request, "templates/index.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    confirm_message = None
    context = {
        "title": "Rejuva Aesthetica | Contact",
        "form": contact_form,
        "message": confirm_message,
    }

    if contact_form.is_valid():
        # print(contact_form.cleaned_data)
        # Adding contact form functionality
        full_name = contact_form.cleaned_data['full_name']
        content = contact_form.cleaned_data['content']
        phone_number = contact_form.cleaned_data['phone_number']
        subject = 'Sent from RejuvaAesthetica.com'
        emailFrom = contact_form.cleaned_data['email']
        message = 'Message: %s  Name: %s  From:%s  PhoneNumber:%s' % (content, full_name, emailFrom, phone_number)
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
        confirm_message = "Thanks for the message. We will get right back to you."  # noqa

        if request.is_ajax():
            return JsonResponse({"message": confirm_message})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')  # noqa

    return render(request, 'contact/view.html', context)


def about_page(request):
    context = {
        "title": "Rejuva Aesthetica | About Page",
    }
    return render(request, "about.html", context)


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy-policy.html'


class TnCView(TemplateView):
    template_name = 'tnc.html'


class HairTreatmentsView(TemplateView):
    template_name = 'services/hair-treatment.html'


class FaceTreatmentsView(TemplateView):
    template_name = 'services/face-treatment.html'


class BodyTreatmentsView(TemplateView):
    template_name = 'services/body-treatment.html'


class SkinTreatmentsView(TemplateView):
    template_name = 'services/skin-treatment.html'


class CosmeticTreatmentsView(TemplateView):
    template_name = 'services/cosmetic-treatment.html'


class BreastTreatmentsView(TemplateView):
    template_name = 'services/breast-treatment.html'


class LaserTreatmentsView(TemplateView):
    template_name = 'services/laser.html'


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


class SiteMapView(TemplateView):
    template_name = 'sitemap.xml'
    content_type = 'text/xml'
