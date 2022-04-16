import os

from appdirs import unicode
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.lib.units import inch
from django.contrib.auth.decorators import login_required

import sk_profiling.settings
from sk_profiling import settings
from .models import Profile
from django.utils.text import slugify
from .forms import profile_form
# TODO: Try using forms and add class to it
# Create your views here.


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def landing_page(response):
    return render(response, "landing_page/index.html")

@login_required
def dashboard(response):
    current_user = response.user


    high_school_count = Profile.objects.filter(education_level="High School").count()
    elementary_count = Profile.objects.filter(education_level="Elementary").count()
    college_count = Profile.objects.filter(education_level="College").count()
    out_of_school_count = Profile.objects.filter(education_level="Out of School").count()
    graduates_count = Profile.objects.filter(education_level="Graduates").count()
    all_count = Profile.objects.all().count()
    g1 = Profile.objects.filter(education_year="Grade 1").count()
    g2 = Profile.objects.filter(education_year="Grade 2").count()
    g3 = Profile.objects.filter(education_year="Grade 3").count()
    g4 = Profile.objects.filter(education_year="Grade 4").count()
    g5 = Profile.objects.filter(education_year="Grade 5").count()
    g6 = Profile.objects.filter(education_year="Grade 6").count()
    g7 = Profile.objects.filter(education_year="Grade 7").count()
    g8 = Profile.objects.filter(education_year="Grade 8").count()
    g9 = Profile.objects.filter(education_year="Grade 9").count()
    g10 = Profile.objects.filter(education_year="Grade 10").count()
    g11 = Profile.objects.filter(education_year="Grade 11").count()
    g12 = Profile.objects.filter(education_year="Grade 12").count()
    y1 = Profile.objects.filter(education_year="1st Year").count()
    y2 = Profile.objects.filter(education_year="2nd Year").count()
    y3 = Profile.objects.filter(education_year="3rd Year").count()
    y4 = Profile.objects.filter(education_year="4th Year").count()

    print(g7, g8, g9, g10, g11, g12)









    return render(response, "dashboard/index.html",{
        "current_user":current_user,
        "hs_count":high_school_count,
        "elem_count":elementary_count,
        "col_count":college_count,
        "oos_count":out_of_school_count,
        "grad_count":graduates_count,
        "all_count":all_count,
        "g1":g1,
        "g2":g2,
        "g3":g3,
        "g4":g4,
        "g5":g5,
        "g6":g6,
        "g7":g7,
        "g8":g8,
        "g9":g9,
        "g10":g10,
        "g11":g11,
        "g12":g12,
        "y1":y1,
        "y2":y2,
        "y3":y3,
        "y4":y4,



    })
@login_required
def profile(response):
    datas = Profile.objects.all().order_by(Lower('last_name'))
    current_user = response.user

    return render(response, "profiles/profiles.html",{
        'datas':datas,
        'current_user': current_user,

    })
@login_required
def profile_filter_year(response):
    datas = Profile.objects.all().order_by('education_year')
    current_user = response.user

    return render(response, "profiles/profiles-filter-year.html",{
        'datas':datas,
        'current_user': current_user,

    })
@login_required
def profile_filter_level(response):
    datas = Profile.objects.all().order_by('education_level')
    print(datas)
    current_user = response.user

    return render(response, "profiles/profiles-filter-level.html",{
        'datas':datas,
        'current_user': current_user,

    })
@login_required
def profile_page(response, slug):

    data = get_object_or_404(Profile, slug=slug)
    current_user = response.user
    print(data.id)
    if response.method == "POST":
        if response.POST.get("delete") != "":
            data.delete()
            return redirect('profiles')
    return render(response, "profiles/profile_page.html",{
        "data":data,
        'current_user': current_user,

    })
@login_required
def profile_page_edit(response,slug):
    data = get_object_or_404(Profile, slug=slug)
    form = profile_form(response.POST or None, instance=data)
    current_user = response.user

    if response.method == "POST":
        form = profile_form(response.POST or None, instance=data)
        if form.is_valid():
            save = form.save(commit=False)

            if save.middle_name != None:
                full_name = save.first_name.title() + " " + save.middle_name[
                    0].title() + ". " + save.last_name.title()
                # slug = first_name.lower() + "-" + middle_name[0].lower() +"-"+ last_name.lower()
                slug = slugify(unicode(
                    '%s %s %s' % (save.first_name.lower(), save.middle_name.lower(), save.last_name.lower())))
                if Profile.objects.filter(first_name = save.first_name.title(), middle_name=save.middle_name.title(), last_name=save.last_name.title()).exists():
                    messages.error(response, full_name, "already exists.")
                    return HttpResponseRedirect(response.path)
            else:
                full_name = save.first_name.title() + " " + save.last_name.title()
                slug = slugify(unicode('%s %s' % (save.first_name.lower(), save.last_name.lower())))
                if Profile.objects.filter(first_name = save.first_name.title(), middle_name=save.middle_name.title(), last_name=save.last_name.title()).exists():
                    messages.error(response, full_name, "already exists.")
                    return HttpResponseRedirect(response.path)
            save.full_name = full_name
            save.slug = slug

            save.save()

        return redirect('profile_page', data.slug)

    return render(response, "profiles/profile_page_edit.html", {
        "data": data,
        "form":form,
        'current_user': current_user,

    })
@login_required
def add_profile(response):
    form = profile_form()
    current_user = response.user

    if response.method == "POST":
        form = profile_form(response.POST)

        if form.is_valid():
            save = form.save(commit=False)
            print(save.first_name.title())
            if save.middle_name != None:
                full_name = save.first_name.title() + " " + save.middle_name[0].title() +". "+ save.last_name.title()
                slug = slugify(unicode(' %s %s %s' % (save.first_name.lower(), save.middle_name.lower(), save.last_name.lower())))
                if Profile.objects.filter(first_name = save.first_name.title(), middle_name=save.middle_name.title(), last_name=save.last_name.title()).exists():
                    messages.error(response, full_name, "already exists.")
                    return HttpResponseRedirect(response.path)
            else:
                full_name = save.first_name.title() +" "+ save.last_name.title()
                slug = slugify(unicode(' %s %s' % ( save.first_name.lower(), save.last_name.lower())))
                if Profile.objects.filter(first_name = save.first_name.title(),  last_name=save.last_name.title()).exists():
                    messages.error(response, full_name, "already exists.")
                    return HttpResponseRedirect(response.path)
            save.full_name = full_name
            save.slug = slug
            save.save()

        return HttpResponseRedirect(response.path)

    return render(response,"profiles/add_profile.html",{
        "form":form,
        'current_user': current_user,

    })


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



from io import StringIO, BytesIO


val = None




@login_required
def generate_document(response):
    current_user = response.user

    if response.method == "POST":
        datas = response.POST.get("header_input")
        datas_code = slugify(datas)


        datas = {"header": datas, "code":datas_code}
    else:
        datas = ""
    global val
    def val():
        return datas
    profiles = Profile.objects.all()

    education_years = []
    for profile in profiles:
        years = profile.education_year

        if years not in education_years and profile.education_level != "College" and profile.education_level != "Graduates" and profile.education_level != "Out of School":
            education_years.append(years)
    if Profile.objects.filter(education_level="College"):
        education_years.append("College")
    if Profile.objects.filter(education_level="Graduates") :
        education_years.append("Graduates")
    if Profile.objects.filter(education_level="Out of School"):
        education_years.append("Out of School")
    print(education_years)
    templist = []
    for years in education_years:
        if years == "Out of School":
            year_code = years.replace(" ","")
        else:
            year_code = years.replace("Grade ","")
        # print(year_code)
        # print(year_code)
        templist.append({"grade":years, "code":year_code})

    print(templist)


    return render(response,'dashboard/generate_document.html',{
        'current_user': current_user,
        'datas':datas,
        'templist':templist,

    })

def pdf(response):
    return render(response,'pdf.html',{
    })

@login_required
def getPdfPage(request, grade, header):
    ok = val()
    print("OK", ok)
    print(type(ok))
    header = ok["header"]
    print(header)


    if grade == "College":
        records = Profile.objects.filter(education_level="College").order_by(Lower("last_name"))
    elif grade == "OutofSchool":
        records = Profile.objects.filter(education_level="Out of School").order_by(Lower("last_name"))
    elif grade == "Graduates":
        records = Profile.objects.filter(education_level="Graduates").order_by(Lower("last_name"))
    else:
        records = Profile.objects.filter(education_year="Grade " + grade).order_by(Lower("last_name"))

    data = {'record': records, "grade": grade, "header": header,}


    template = get_template("pdf.html")
    data_p = template.render(data)
    response = BytesIO()

    pdfPage = pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")), response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")

