import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .forms import bird_hit_formForm, incident_formForm, bird_hit_analysis_form
from .models import bird_hit_form, incident_form
from django.contrib.auth.middleware import get_user
import numpy
from .off import *


def home(request):
    if request.user.is_authenticated:
        user = get_user(request)
        username = user.get_username()
        offline_mode()
        forms_submitted = bird_hit_form.objects.filter(submitted_by__contains=username)
        months = []
        for i in forms_submitted:
            months.append(bird_hit_form.month_published(i))
        uniques, counts = numpy.unique(months, return_counts=True)
        categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        months_data = [0] * 12
        for m in range(len(uniques)):
            if uniques[m] in categories:
                index = list(categories).index(uniques[m])
                months_data[index] = counts[m]

        if username == "admin@aai.com":
            users = User.objects.all()
            total_forms = bird_hit_form.objects.all()
            birds, runway, aero_occ, air_opp = [], [], [], []
            for form in total_forms:
                if str(form.wildlife_desc) != "":
                    birds.append(str(form.wildlife_desc))
                if str(form.runway_in_use) != "":
                    runway.append(str(form.runway_in_use))
                if str(form.aerod_occ) != "":
                    aero_occ.append(str(form.aerod_occ))
                if str(form.air_operator) != "":
                    air_opp.append(str(form.air_operator))

            # print(birds, runway, aero_occ, air_opp)
            max_data, max_cat = [], []
            uniques, counts = numpy.unique(birds, return_counts=True)
            max_count = max(counts)
            max_index = list(counts).index(max_count)
            max_cat.append(uniques[max_index])
            max_data.append(counts[max_index])

            uniques, counts = numpy.unique(aero_occ, return_counts=True)
            max_count = max(counts)
            max_index = list(counts).index(max_count)
            max_cat.append(uniques[max_index])
            max_data.append(counts[max_index])

            uniques, counts = numpy.unique(runway, return_counts=True)
            max_count = max(counts)
            max_index = list(counts).index(max_count)
            max_cat.append(uniques[max_index])
            max_data.append(counts[max_index])

            uniques, counts = numpy.unique(air_opp, return_counts=True)
            max_count = max(counts)
            max_index = list(counts).index(max_count)
            max_cat.append(uniques[max_index])
            max_data.append(counts[max_index])

            print(max_cat, max_data)
            return render(request, 'useraccount/user_account.html', {
                'data': forms_submitted,
                'users': users,
                'months_data': months_data,
                'months_cat': categories,
                'max_cat' : max_cat,
                'max_data': max_data
            })

        else:
            return render(request, 'useraccount/user_account.html', {'data': forms_submitted,
                                                                     'months_data': months_data,
                                                                     'months_cat':categories})
        # return render(request, 'useraccount/user_account.html')
    return HttpResponse("Not Logged In")


def view_max_stats(request):
    if request.user.is_authenticated:
        user = get_user(request)
        username = user.get_username()
        if username == "admin@aai.com":
            users = User.objects.all()
            total_forms = bird_hit_form.objects.all()
            birds, runway, aero_occ, air_opp = [], [], [], []
            for form in total_forms:
                if str(form.wildlife_desc) != "":
                    birds.append(str(form.wildlife_desc))
                if str(form.runway_in_use) != "":
                    runway.append(str(form.runway_in_use))
                if str(form.aerod_occ) != "":
                    aero_occ.append(str(form.aerod_occ))
                if str(form.air_operator) != "":
                    air_opp.append(str(form.air_operator))

            # print(birds, runway, aero_occ, air_opp)
            max_data, max_cat = [], []
            uniques, counts = numpy.unique(birds, return_counts=True)
            max_count = max(counts)
            max_index = list(counts).index(max_count)
            max_cat.append(uniques[max_index])
            max_data.append(counts[max_index])

            uniques, counts = numpy.unique(aero_occ, return_counts=True)
            max_count = max(counts)
            max_index = list(counts).index(max_count)
            max_cat.append(uniques[max_index])
            max_data.append(counts[max_index])

            uniques, counts = numpy.unique(runway, return_counts=True)
            max_count = max(counts)
            max_index = list(counts).index(max_count)
            max_cat.append(uniques[max_index])
            max_data.append(counts[max_index])

            uniques, counts = numpy.unique(air_opp, return_counts=True)
            max_count = max(counts)
            max_index = list(counts).index(max_count)
            max_cat.append(uniques[max_index])
            max_data.append(counts[max_index])

            print(max_cat, max_data)
            return render(request, 'useraccount/user_account.html', {
                'max_cat' : max_cat,
                'max_data': max_data
            })


    else:
        return HttpResponse("Not Logged In")

def form_view(request, form_id):
    if id is not None:
        dataset = bird_hit_form.objects.get(id=form_id)
        return render(request, 'useraccount/bird_hit_form_view.html', {'data': dataset})
    else:
        return HttpResponse("No ID found")


def user_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.POST['aai-users']
            forms_submitted = bird_hit_form.objects.filter(submitted_by__contains=user)
            # forms_submitted = bird_hit_form.objects.filter(submitted_by__contains=username)
            months = []
            for i in forms_submitted:
                months.append(bird_hit_form.month_published(i))
            uniques, counts = numpy.unique(months, return_counts=True)
            categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            months_data = [0] * 12
            for m in range(len(uniques)):
                if uniques[m] in categories:
                    index = list(categories).index(uniques[m])
                    months_data[index] = counts[m]
            return render(request, 'useraccount/user_account_view_admin.html', {
                'data': forms_submitted,
                'user': user,
                'months_data': months_data
            })

        else:
            return render(request, 'useraccount/user_account_view_admin.html')

    else:
        return HttpResponse('Not Logged In')


def map_view(request):
    if request.user.is_authenticated:
        return render(request, 'useraccount/state_wise_india_map.html')


def bird_form_submitted(request):
    return render(request, 'useraccount/form_submitted.html')


def bird_hit_form_func(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = bird_hit_formForm(request.POST)
            # get_list = bird_hit_formForm(request.POST.getlist('check_choice'))
            if form.is_valid():
                obj = bird_hit_form()
                user = get_user(request)
                obj.submitted_by = user.get_username()
                obj.air_operator = form.cleaned_data['air_operator']
                obj.air_type_series = form.cleaned_data['air_type_series']
                obj.air_reg = form.cleaned_data['air_reg']
                obj.engine_model = form.cleaned_data['engine_model']
                obj.flight_no = form.cleaned_data['flight_no']
                obj.date_of_occ = form.cleaned_data['date_of_occ']
                obj.time_of_occ = form.cleaned_data['time_of_occ']
                obj.duration_time = form.cleaned_data['duration_time']
                obj.aerod_depart = form.cleaned_data['aerod_depart']
                obj.aerod_intend_arr = form.cleaned_data['aerod_intend_arr']
                obj.aerod_occ = form.cleaned_data['aerod_occ']
                obj.runway_in_use = form.cleaned_data['runway_in_use']
                obj.altitude_AGL = form.cleaned_data['altitude_AGL']
                obj.speed = form.cleaned_data['speed']
                obj.ATC_inform = form.cleaned_data['ATC_inform']
                obj.position = form.cleaned_data['position']
                obj.phase_of_flight = form.cleaned_data['phase_of_flight']
                # obj.check_choice = form.cleaned_data.get('check_choice')
                obj.struck_parts = form.cleaned_data.get('struck_parts')
                obj.struck_others = form.cleaned_data['others']
                obj.damage_parts = form.cleaned_data.get('damage_parts')
                obj.damage_others = form.cleaned_data['Others']
                obj.effect_on_flight = form.cleaned_data.get('effect_on_flight')
                obj.effect_others = form.cleaned_data['other_effects']
                obj.other_report_raised = form.cleaned_data.get('other_report_raised')
                obj.other_reports = form.cleaned_data['other_reports']
                obj.precipitation = form.cleaned_data['precipitation']
                obj.sky_condition = form.cleaned_data['sky_condition']
                obj.wildlife_desc = form.cleaned_data['wildlife_description']
                obj.bird_remains = form.cleaned_data['bird_remains_sent_for_identification']
                obj.bird_seen = form.cleaned_data['number_of_birds_seen']
                obj.bird_remains = form.cleaned_data['number_of_birds_struck']
                obj.pilot_warned = form.cleaned_data['pilot_warned_of_birds']
                obj.bird_size = form.cleaned_data['bird_size']
                obj.remarks = form.cleaned_data['remarks']
                obj.aircraft_tos = form.cleaned_data['aircraft_time_out_of_service']
                obj.est_cost_of_repair = form.cleaned_data['estimated_cost_of_repair']
                obj.est_other = form.cleaned_data['estimated_other_cost']
                obj.operation_department = form.cleaned_data.get('operation_department')
                obj.ATC_mark = form.cleaned_data.get('ATC_mark')
                obj.DGCA_mark = form.cleaned_data.get('DGCA_mark')
                obj.save()
                return render(request, 'useraccount/form_submitted.html')

        else:
            form = bird_hit_formForm()
        return render(request, 'useraccount/bird_hit_form.html', {'form': form})
    return HttpResponse("Not logged in!")


def incident_form_func(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = incident_formForm(request.POST)
            if form.is_valid():
                obj = incident_form()
                user = get_user(request)
                obj.submitted_by = user.get_username()
                obj.aircraft_identification = form.cleaned_data['aircraft_identification']
                obj.type_of_incident = form.cleaned_data['type_of_incident']
                obj.date_of_incident = form.cleaned_data['date_of_incident']
                obj.time_of_incident = form.cleaned_data['time_of_incident']
                obj.pos = form.cleaned_data['pos']
                obj.head_and_route = form.cleaned_data['heading_and_route']
                obj.true_airspeed = form.cleaned_data['true_airspeed']
                obj.speed_measured = form.cleaned_data['speed_measured']
                obj.air_climb = form.cleaned_data['air_climb']
                obj.air_bank = form.cleaned_data['air_bank']
                obj.air_dir = form.cleaned_data['air_dir']
                obj.restr_visib = form.cleaned_data.get('restr_visib')
                obj.air_light = form.cleaned_data.get('air_light')
                obj.traffic_advice = form.cleaned_data['traffic_advice']
                obj.traffic_info = form.cleaned_data['traffic_info']
                obj.ACAS = form.cleaned_data['ACAS']
                obj.radar = form.cleaned_data['radar']
                obj.other_aircraft = form.cleaned_data['other_aircraft']
                obj.avoid_action = form.cleaned_data['avoid_action']
                obj.type_of_flight_plan = form.cleaned_data['type_of_flight_plan']
                obj.type_and_call_sign = form.cleaned_data['type_and_call_sign']
                obj.other_available_details = form.cleaned_data['other_available_details']
                obj.aircraft_reg = form.cleaned_data['aircraft_reg']
                obj.aircraft_type = form.cleaned_data['aircraft_type']
                obj.operator = form.cleaned_data['operator']
                obj.aero_depart = form.cleaned_data['aero_depart']
                obj.aero_first_landing = form.cleaned_data['aero_first_landing']
                obj.destination = form.cleaned_data['destination']
                obj.operation_department = form.cleaned_data.get('operation_department')
                obj.ATC_mark = form.cleaned_data.get('ATC_mark')
                obj.DGCA_mark = form.cleaned_data.get('DGCA_mark')
                obj.save()
                return render(request, 'useraccount/form_submitted.html')
            # return HttpResponse("Submit your Incident here !")
        else:
            form = incident_formForm()

        return render(request, 'useraccount/incident_form.html', {'form': form})
    return HttpResponse("Not Logged In")


def bird_hit_analysis(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = bird_hit_analysis_form(request.POST)
            if form.is_valid():
                values_returned = {}
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                aerod_occurrence = form.cleaned_data['occurrence']
                aerod_departure = form.cleaned_data['departure']
                aerod_arrival = form.cleaned_data['arrival']
                runway_in_use = form.cleaned_data['runway_in_use']
                aircraft_operator = form.cleaned_data['air_operator']
                dataset = bird_hit_form.objects.filter(date_of_occ__range=[start_date, end_date], aerod_occ__contains=aerod_occurrence, aerod_depart__contains=aerod_departure,
                                                       air_operator__contains=aircraft_operator, runway_in_use__contains=runway_in_use, aerod_intend_arr__contains=aerod_arrival)

                # else:
                #     dataset = bird_hit_form.objects.filter(date_of_occ__range=[start_date, end_date])
                wildlife = []
                # wildlife.append(str(p.wildlife_desc))
                for i in dataset:
                    if i.wildlife_desc != None:
                        wildlife.append(i.wildlife_desc)
                uniques, counts = numpy.unique(wildlife, return_counts=True)
                data = []
                for i in range(len(uniques)):
                    if uniques[i] == "":
                        pass
                    else:
                        # species_counts.append(counts[i])
                        # species.append(uniques[i])
                        data.append([str(uniques[i]), int(counts[i]), str("")])

                if len(data) != 0:
                    data[0][2] = True
                    data[0].append(True)

                return render(request, 'useraccount/bird_hit_analysis_result.html', {
                    'data': json.dumps(data)
                })
                # return HttpResponse(data)

                # return render(request, 'useraccount/bird_hit_analysis_result.html', {'wildlife_count':wildlife_count})
        else:
            form = bird_hit_analysis_form()
        return  render(request, 'useraccount/bird_hit_analysis.html', {'form':form})
    return HttpResponse("NOT LOGGED IN!")
