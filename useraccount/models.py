from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User, AbstractUser
import datetime
from django.utils.timezone import now as utcnow


class bird_hit_form(models.Model):
    time_stamp = models.DateTimeField(default=utcnow())
    submitted_by = models.CharField(max_length=100, default='Null')
    air_operator = models.CharField(max_length=100, default='Null')
    # air_operator = models.CharField(max_length=100)
    air_type_series = models.CharField(max_length=50, default='Null')
    air_reg = models.CharField(max_length=50, default='Null')
    flight_no = models.CharField(max_length=50, default='Null')
    engine_model = models.CharField(max_length=50, default='Null')
    date_of_occ = models.DateField('date published', default= datetime.date.today())
    time_of_occ = models.TimeField('time published', default=datetime.datetime.utcnow())
    duration_choice = (
        ('Dawn', 'Dawn'),
        ('Day', 'Day'),
        ('Dusk', 'Dusk'),
        ('Night', 'Night'),
    )
    duration_time = models.CharField(max_length=10, choices=duration_choice, default='NULL')
    aerod_depart = models.CharField(max_length=100, default='NUll')
    aerod_intend_arr = models.CharField(max_length=100, default='Null')
    aerod_occ = models.CharField(max_length=100, default='Null')
    runway_in_use = models.CharField(max_length=10, default='Null')
    altitude_AGL = models.IntegerField(max_length=10, default=0)
    speed = models.IntegerField(max_length=10, default=0)
    position = models.CharField(max_length=100, default='Null')

    ATC_informed_choice = (
        ('YES', 'YES'),
        ('NO', 'No'),
    )

    ATC_inform = models.CharField(max_length=5, choices=ATC_informed_choice, default='Null')

    phase_of_flight_choices = (
        ('Taxi', 'Taxi'),
        ('Take-off run', 'Take-off run'),
        ('Climb', 'Climb'),
        ('En-route', 'En-route'),
        ('Descend', 'Descend'),
        ('Approach', 'Approach'),
        ('Landing roll', 'Landing roll'),
        ('Ground Checks', 'Ground Checks'),
    )

    phase_of_flight = models.CharField(max_length=20, choices=phase_of_flight_choices, default='Null')
    # check_choice = models.CharField(max_length=200,  default='Null')
    struck_parts = models.CharField(max_length=500, default='Null')
    damage_parts = models.CharField(max_length=500, default='Null')
    struck_others = models.CharField(max_length=100, default='Null')
    damage_others = models.CharField(max_length=100, default='Null')
    effect_on_flight = models.CharField(max_length=200, default='Null')
    effect_others = models.CharField(max_length=100, default='Null')
    other_report_raised = models.CharField(max_length=50, default='Null')
    other_reports = models.CharField(max_length=100, default='Null')

    precipitation = models.CharField(max_length=100, default='Null')
    sky_cond_choices = (
        ('No cloud', 'No cloud'),
        ('Some cloud', 'Some cloud'),
        ('Over cloud', 'Over cloud'),
    )
    sky_condition = models.CharField(choices=sky_cond_choices, max_length=10, default='Null')
    wildlife_desc = models.CharField(max_length=100, default='Null')
    bird_remains_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    bird_remains = models.CharField(choices=bird_remains_choices, max_length=5, default='Null')
    bird_seen_choices = (
        ('1', '1'),
        ('2-10', '2-10'),
        ('11-100', '11-100'),
        ('100+', '100+'),
    )
    bird_seen = models.CharField(choices=bird_seen_choices, max_length=10, default='Null')
    bird_struck = models.CharField(choices=bird_seen_choices, max_length=10, default='Null')
    pilot_warned = models.CharField(choices=bird_remains_choices, max_length=10, default='Null')
    bird_size_choices = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    bird_size = models.CharField(choices=bird_size_choices, max_length=10, default='Null')
    remarks = models.CharField(max_length=1000, default='Null')
    aircraft_tos = models.IntegerField(default=0)
    est_cost_of_repair = models.IntegerField(default=0)
    est_other = models.IntegerField(default=0)
    operation_department = models.CharField(max_length=1, default='n')
    ATC_mark = models.CharField(max_length=1, default='n')
    DGCA_mark = models.CharField(max_length=1, default='n')

    def month_published(self):
        return self.date_of_occ.strftime('%b')


class incident_form(models.Model):
    time_stamp = models.DateTimeField(default=utcnow())
    submitted_by = models.CharField(max_length=100, default='Null')
    aircraft_identification = models.CharField(max_length=1000, default='Null')
    type_of_incident_choices = (
        ('AirProx', 'AirProx'),
        ('Obstruction on Runway', 'Obstruction on Runway'),
        ('Runway Incursion', 'Runway Incursion'),
        ('Procedure', 'Procedure'),
        ('Facility', 'Facility'),
    )
    type_of_incident = models.CharField(choices=type_of_incident_choices, max_length=20, default='Null')
    date_of_incident = models.DateField('date published', default= datetime.date.today())
    time_of_incident = models.TimeField('time published', default=datetime.datetime.utcnow())
    pos = models.CharField(max_length=100, default='Null')
    head_and_route = models.CharField(max_length=100, default='Null')
    true_airspeed = models.IntegerField(max_length=10, default=0)
    speed_measured_choices = (
        ('kt','kt'),
        ('km/h','km/h'),
    )
    speed_measured = models.CharField(choices=speed_measured_choices, max_length=20, default='Null')
    air_climb_choices = (
        ('Level flight','Level flight'),
        ('climbing','climbing'),
        ('Descending','Descending'),
    )
    air_climb = models.CharField(choices=air_climb_choices, max_length=20, default='Null')
    air_bank_choices = (
        ('wings level','wings level'),
        ('slight bank','slight bank'),
        ('moderate bank','moderate bank'),
        ('steep bank','steep bank'),
        ('inverted','inverted'),
        ('unknown','unknown'),
    )
    air_bank = models.CharField(choices=air_bank_choices, max_length=20, default='Null')
    air_dir_choices = (
        ('left','left'),
        ('right','right'),
        ('unknown','unknown'),
    )
    air_dir = models.CharField(choices=air_dir_choices, max_length=20, default='Null')
    restr_visib_choices = (
        ('Sun Glare', 'Sun Glare'),
        ('Wind Screen Pillar', 'Wind Screen Pillar'),
        ('Dirty Wind Screen', 'Dirty Wind Screen'),
        ('Other cockpit structure', 'Other cockpit structure'),
        ('None', 'None'),
    )
    restr_visib = models.CharField(choices=restr_visib_choices, max_length=200, default='Null')
    air_light_choices = (
        ('Navigation Lights', 'Navigation Lights'),
        ('Strobe Lights', 'Strobe Lights'),
        ('Cabin Lights', 'Cabin Lights'),
        ('Red anti-collision light', 'Red anti-collision light'),
        ('Landing/Taxi Lights', 'Landing/Taxi Lights'),
        ('Logo Light', 'Logo Light'),
        ('Other', 'Other'),
        ('None', 'None'),
    )
    air_light = models.CharField(choices=air_light_choices, max_length=500, default='Null')
    traffic_advice_choices = (
        ('yes, based on radar','yes, based on radar'),
        ('yes, based on visual sighting','yes, based on visual sighting'),
        ('yes, based on other information','yes, based on other information'),
        ('no','no'),

    )
    traffic_advice = models.CharField(choices=traffic_advice_choices, max_length=50, default='Null')
    traffic_info_choices = (
        ('yes, based on radar', 'yes, based on radar'),
        ('yes, based on visual sighting', 'yes, based on visual sighting'),
        ('yes, based on other information', 'yes, based on other information'),
        ('no', 'no'),
    )
    traffic_info = models.CharField(choices=traffic_info_choices, max_length=50, default='Null')
    ACAS_choices = (
        ('Not Carried','Not Carried'),
        ('Type','Type'),
        ('Traffic advisory issued','Traffic advisory issued'),
        ('Resolution advisory issued','Resolution advisory issued'),
        ('Traffic or resolution advisory not issued ','Traffic or resolution advisory not issued '),

    )
    ACAS = models.CharField(choices=ACAS_choices, max_length=50, default='Null')
    radar_choices = (
        ('No radar available','No radar available'),
        ('Radar identification','Radar identification'),
        ('No radar identification','No radar identification'),
    )
    radar = models.CharField(choices=radar_choices, max_length=50, default='Null')
    other_aircraft_choices = (
        ('yes','yes'),
        ('no','no'),
        ('wrong aircraft sighted','wrong aircraft sighted'),
    )
    other_aircraft = models.CharField(choices=other_aircraft_choices, max_length=50, default='Null')
    avoid_action_choices = (
        ('yes','yes'),
        ('no','no'),

    )
    avoid_action = models.CharField(choices=avoid_action_choices, max_length=50, default='Null')
    type_flight_choices = (
        ('IFR','IFR'),
        ('VFR','VFR'),
        ('none','none'),
    )
    type_of_flight_plan = models.CharField(choices=type_flight_choices, max_length=20, default='Null')
    type_and_call_sign = models.CharField(max_length=100, default='Null')
    other_available_details = models.CharField(max_length=500, default='Null')
    aircraft_reg = models.CharField(max_length=150, default='Null')
    aircraft_type = models.CharField(max_length=150, default='Null')
    operator = models.CharField(max_length=150, default='Null')
    aero_depart = models.CharField(max_length=150, default='Null')
    aero_first_landing = models.CharField(max_length=150, default='Null')
    destination = models.CharField(max_length=150, default='Null')
    operation_department = models.CharField(max_length=1, default='n')
    ATC_mark = models.CharField(max_length=1, default='n')
    DGCA_mark = models.CharField(max_length=1, default='n')



