from django.core.management.base import BaseCommand
from api_pets.models import User, Pet
import random
import logging

# python manage.py seed --mode=refresh
logger = logging.getLogger(__name__)

""" Clear all data and create initial database """
MODE_REFRESH = 'refresh'

""" Clear all data """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete tables instances")
    User.objects.all().delete()
    Pet.objects.all().delete()


def create_pets(index):
    """Creates Pets object combining different elements from the list"""
    logger.info("Creating Pets")
    pets_names = ["Puppy", "Juana", "Rocco", "Otto", "Messi", "Diego", "Gabana","Africa", "Roma"]
    pets_birth = ['2020-06-20', '2020-07-28', '2009-04-17', '2010-09-21', '2015-03-25', '2016-01-10', '2015-11-30', '2021-07-30', '2018-10-30', '2012-02-06']
    pets_aprox = [True, False]

    pet = Pet(
        name=pets_names[index],
        birth_date=random.choice(pets_birth),
        is_birth_approximate=random.choice(pets_aprox),
    )
    pet.save()
    logger.info("{} pet created.".format(pet))


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return
    
    # Create Users
    admin = User(
        username = 'admin',
        first_name = 'admin',
        last_name = 'admin_lastname',
        email = 'admin@admin.com',
        is_admin = True,
        password = 'admin123'
        )
    admin.save()
    
    guest = User(
        username = 'guest',
        first_name = 'guest',
        last_name = 'guest_lastname',
        email = 'guest@guest.com',
        is_admin = False,
        password = 'guest123'
        )
    guest.save()

    # Creating 9 pets
    for i in range(9):
        create_pets(i)