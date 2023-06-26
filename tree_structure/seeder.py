import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StaffHierarchy.settings')
django.setup()

from django_seed import Seed
from tree_structure.models import TopManager, Director, RegionalManager, DistrictManager, Teamlead, Specialist, Trainee

def db_seeder(level, upper_level, quantity):
    seeder = Seed.seeder()
    seeder.add_entity(level, quantity, {
        'position': lambda x: seeder.faker.job(),
        'surname': lambda x: seeder.faker.last_name(),
        'name': lambda x: seeder.faker.first_name(),
        'email': lambda x: seeder.faker.email(),
        'employment_date': lambda x: seeder.faker.date_this_year(),
        'head': lambda x: seeder.faker.random_element(upper_level.objects.all())
    })
    seeder.execute()

db_seeder(Director, TopManager, 3)
db_seeder(RegionalManager, Director, 9)
db_seeder(DistrictManager, RegionalManager, 30)
db_seeder(Teamlead, DistrictManager, 90)
db_seeder(Specialist, Teamlead, 300)
db_seeder(Trainee, Specialist, 300)