from django import forms
from .models import bird_hit_form, incident_form
import datetime, time
from django.contrib.auth.models import User, AbstractUser


class bird_hit_formForm(forms.Form):
    # ts = time.time()
    # time_stamp = forms.DateTimeField(initial=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

    submitted_by = forms.CharField(max_length=100, required=False)
    air_operator = forms.CharField(max_length=100, required=False)
    air_type_series = forms.CharField(max_length=50, required=False)
    air_reg = forms.CharField(max_length=50, required=False)
    flight_no = forms.CharField(max_length=50, required=False)
    engine_model = forms.CharField(max_length=50, required=False)
    date_of_occ = forms.DateField(required=False)
    time_of_occ = forms.TimeField(required=False)
    duration_time = forms.ChoiceField(choices=bird_hit_form.duration_choice, required=False, widget=forms.RadioSelect)
    aerod_depart = forms.CharField(max_length=100, required=False)
    aerod_intend_arr = forms.CharField(max_length=100, required=False)
    aerod_occ = forms.CharField(max_length=100, required=False)
    runway_in_use = forms.CharField(max_length=10, required=False)
    altitude_AGL = forms.IntegerField(max_value=10, required=False)
    speed = forms.IntegerField(max_value=10, required=False)
    position = forms.CharField(max_length=100, required=False)
    ATC_inform = forms.ChoiceField(choices=bird_hit_form.ATC_informed_choice, required=False, widget=forms.RadioSelect)
    phase_of_flight = forms.ChoiceField(choices=bird_hit_form.phase_of_flight_choices, required=False,
                                        widget=forms.RadioSelect)
    # choice = (
    #     ('Yes', 'Yes'),
    #     ('Hello','Hello'),
    #     ('No', 'No'),
    # )
    #
    # check_choice = forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)

    struck_parts_choices = (
        ('Radome', 'Radome'),
        ('Windshield', 'Windshield'),
        ('Nose', 'Nose'),
        ('Engine 1', 'Engine 1'),
        ('Engine 2', 'Engine 2'),
        ('Engine 3', 'Engine 3'),
        ('Engine 4', 'Engine 4'),
        ('Wing', 'Wing'),
        ('Rotor', 'Rotor'),
        ('Fuselage', 'Fuselage'),
        ('Landing Gear', 'Landing Gear'),
        ('Tail', 'Tail'),
        ('Lights', 'Lights'),
    )

    struck_parts = forms.MultipleChoiceField(choices=struck_parts_choices, required=False,
                                             widget=forms.CheckboxSelectMultiple)
    others = forms.CharField(max_length=100, required=False)
    damage_parts = forms.MultipleChoiceField(choices=struck_parts_choices, required=False,
                                             widget=forms.CheckboxSelectMultiple)
    Others = forms.CharField(max_length=100, required=False)
    effect_on_choices = (
        ('None', 'None'),
        ('Precautionary Landing', 'Precautionary Landing'),
        ('Aborted T/O', 'Aborted T/O'),
        ('Engine Shut Down', 'Engine Shut Down'),
    )
    effect_on_flight = forms.MultipleChoiceField(choices=effect_on_choices, required=False,
                                                 widget=forms.CheckboxSelectMultiple)
    other_effects = forms.CharField(max_length=100, required=False)
    other_report_choices = (
        ('Flight safety incident report', 'Flight safety incident report'),
    )
    other_report_raised = forms.MultipleChoiceField(choices=other_report_choices, widget=forms.CheckboxSelectMultiple,
                                                    required=False)
    other_reports = forms.CharField(max_length=100, required=False)

    precipitation_choices = (
        ('None', 'None'),
        ('Fog', 'Fog'),
        ('Rain', 'Rain'),
        ('Snow', 'Snow'),
    )
    precipitation = forms.MultipleChoiceField(choices=precipitation_choices, widget=forms.CheckboxSelectMultiple,
                                              required=False)
    sky_condition = forms.ChoiceField(choices=bird_hit_form.sky_cond_choices, widget=forms.RadioSelect, required=False)
    wildlife_description = forms.CharField(max_length=100, required=False)
    bird_remains_sent_for_identification = forms.ChoiceField(choices=bird_hit_form.bird_remains_choices,
                                                             widget=forms.RadioSelect, required=False)
    number_of_birds_seen = forms.ChoiceField(choices=bird_hit_form.bird_seen_choices, widget=forms.RadioSelect,
                                             required=False)
    number_of_birds_struck = forms.ChoiceField(choices=bird_hit_form.bird_seen_choices, widget=forms.RadioSelect,
                                               required=False)
    pilot_warned_of_birds = forms.ChoiceField(choices=bird_hit_form.bird_remains_choices, widget=forms.RadioSelect,
                                              required=False)
    bird_size = forms.ChoiceField(choices=bird_hit_form.bird_size_choices, widget=forms.RadioSelect, required=False)
    remarks = forms.CharField(max_length=1000, required=False)
    aircraft_time_out_of_service = forms.IntegerField(required=False)
    estimated_cost_of_repair = forms.IntegerField(required=False)
    estimated_other_cost = forms.IntegerField(required=False)

    operation_department_choice = (
        ('y', 'Operation Department'),
    )
    operation_department = forms.MultipleChoiceField(choices=operation_department_choice,
                                                     widget=forms.CheckboxSelectMultiple, required=False)
    ATC_choices = (
        ('y', 'ATC'),
    )
    ATC_mark = forms.MultipleChoiceField(choices=ATC_choices, widget=forms.CheckboxSelectMultiple, required=False)
    DGCA_choices = (
        ('y', 'DGCA'),
    )
    DGCA_mark = forms.MultipleChoiceField(choices=DGCA_choices, widget=forms.CheckboxSelectMultiple, required=False)

    # class Meta:
    #     model = bird_hit_form
    #     fields = ('air_operator', 'air_type_series', 'air_reg', 'flight_no', 'engine_model', 'date_of_occ', 'time_of_occ', 'duration_time', 'aerod_depart', 'aerod_intend_arr', 'aerod_occ', 'runway_in_use', 'altitude_AGL', 'speed', 'position', 'ATC_inform', 'check_choice')
    # #
    # def __init__(self, *args, **kwargs):
    #     super(bird_hit_formForm, self).__init__(*args, **kwargs)
    #     self.fields['check_choice'].queryset = choice
    #     self.fields['check_choice'].widget = CheckboxSelectMultiple()


class incident_formForm(forms.Form):
    submitted_by = forms.CharField(max_length=100, required=False)
    aircraft_identification = forms.CharField(max_length=1000, required=False)
    type_of_incident = forms.ChoiceField(choices=incident_form.type_of_incident_choices, widget=forms.RadioSelect)
    date_of_incident = forms.DateField(required=False)
    time_of_incident = forms.TimeField(required=False)
    pos = forms.CharField(max_length=100)
    heading_and_route = forms.CharField(max_length=100)
    true_airspeed = forms.IntegerField(max_value=5)
    speed_measured = forms.ChoiceField(choices=incident_form.speed_measured_choices, widget=forms.RadioSelect)
    air_climb = forms.ChoiceField(choices=incident_form.air_climb_choices, widget=forms.RadioSelect)
    air_bank = forms.ChoiceField(choices=incident_form.air_bank_choices, widget=forms.RadioSelect)
    air_dir = forms.ChoiceField(choices=incident_form.air_dir_choices, widget=forms.RadioSelect)
    restr_visib = forms.MultipleChoiceField(choices=incident_form.restr_visib_choices, widget=forms.CheckboxSelectMultiple)
    air_light = forms.MultipleChoiceField(choices=incident_form.air_light_choices, widget=forms.CheckboxSelectMultiple)
    traffic_advice = forms.ChoiceField(choices=incident_form.traffic_advice_choices, widget=forms.RadioSelect)
    traffic_info = forms.ChoiceField(choices=incident_form.traffic_info_choices, widget=forms.RadioSelect)
    ACAS = forms.ChoiceField(choices=incident_form.ACAS_choices, widget=forms.RadioSelect)
    radar = forms.ChoiceField(choices=incident_form.radar_choices, widget=forms.RadioSelect)
    other_aircraft = forms.ChoiceField(choices=incident_form.other_aircraft_choices, widget=forms.RadioSelect)
    avoid_action = forms.ChoiceField(choices=incident_form.avoid_action_choices, widget=forms.RadioSelect)
    type_of_flight_plan = forms.ChoiceField(choices=incident_form.type_flight_choices, widget=forms.RadioSelect)
    type_and_call_sign = forms.CharField(max_length=100)
    other_available_details = forms.CharField(max_length=500)
    aircraft_reg = forms.CharField(max_length=150)
    aircraft_type = forms.CharField(max_length=150)
    operator = forms.CharField(max_length=150)
    aero_depart = forms.CharField(max_length=150)
    aero_first_landing = forms.CharField(max_length=150)
    destination = forms.CharField(max_length=150)

    operation_department_choice = (
        ('y', 'Operation Department'),
    )
    operation_department = forms.MultipleChoiceField(choices=operation_department_choice,
                                                     widget=forms.CheckboxSelectMultiple, required=False)
    ATC_choices = (
        ('y', 'ATC'),
    )
    ATC_mark = forms.MultipleChoiceField(choices=ATC_choices, widget=forms.CheckboxSelectMultiple, required=False)
    DGCA_choices = (
        ('y', 'DGCA'),
    )
    DGCA_mark = forms.MultipleChoiceField(choices=DGCA_choices, widget=forms.CheckboxSelectMultiple, required=False)


class bird_hit_analysis_form(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    departure = forms.CharField(max_length=50, required=False)
    arrival = forms.CharField(max_length=50, required=False)
    occurrence = forms.CharField(max_length=50, required=False)
    air_operator = forms.CharField(max_length=50, required=False)
    runway_in_use = forms.CharField(max_length=50, required=False)
