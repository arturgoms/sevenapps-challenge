from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Q
from apps.domain.models.company.models import Company
from apps.domain.models.person.models import Person
from apps.domain.models.work_history.models import WorkHistory
import csv
from faker import Faker

class Command(BaseCommand):
    help = 'Ingest sevenapps data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        path = "./companies.csv"
        companies = []
        with open(path, 'rt') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                # Fix linkedin Names
                row[1] = row[1].replace("\n", "")
                row[1] = row[1].replace("[", "")
                row[1] = row[1].replace("]", "")
                row[1] = row[1].replace('"', "")
                row[1] = row[1].strip()
                row[1] = row[1].split(",")
                row[1] = ",".join(row[1])
                
                # Fix description
                row[2] = row[2] if row[2] != '' else None
                
                # Fix head count
                row[3] = int(row[3]) if row[3] != '' else None
                
                # Fix founding_date
                row[4] = row[4] if row[4] != '' else None
                
                # Fix most_recent_raise
                row[5] = int(row[5]) if row[5] != '' else None
                
                # Fix most_recent_valuation
                row[6] = int(row[6]) if row[6] != '' else None
                
                # Fix investors
                if row[7] == '':
                    row[7] == None
                else:
                    row[7] = row[7].replace("\n", "")
                    row[7] = row[7].replace("[", "")
                    row[7] = row[7].replace("]", "")
                    row[7] = row[7].replace('"', "")
                    row[7] = row[7].strip()
                    row[7] = row[7].split(",")
                    row[7] = ",".join(row[7])
                
                # Fix know_total_funding
                row[8] = int(row[8]) if row[8] != '' else None
                
                companies.append(Company(
                    name=row[0],
                    linkedin_names=row[1],
                    description=row[2],
                    head_count=row[3],
                    founding_date=row[4],
                    most_recent_raise=row[5],
                    most_recent_valuation=row[6],
                    investors=row[7],
                    know_total_funding=row[8],
                ))
           
        Company.objects.bulk_create(companies)

        path = "./people.csv"
        with open(path, 'rt') as f:
            reader = csv.reader(f)
            next(reader)
            current = None
            person = None
            people = []
            work_history = []
            for row in reader:
                if current != row[0]:
                    person, created  = Person.objects.get_or_create(
                        id=row[0]
                    )
                    if created:
                        person.name = fake.name()
                        person.save()
                    
                
                company = Company.objects.filter(Q(name__icontains=row[1]) | Q(linkedin_names__icontains=row[2]) | Q(name__icontains=row[1].lower().replace(" ", "")) | Q(linkedin_names__icontains=row[1].lower().replace(" ", ""))).first()
                if not company:
                    print("ERROR: could not find: ", row)
                    
                row[4] = row[4] if row[4] != '' else None
                row[5] = row[5] if row[5] != '' else None
                work_history.append(WorkHistory(
                    person=person,
                    company=company,
                    title=row[3],
                    group_start_date=row[4],
                    group_end_date=row[5]
                ))
                
                current = row[0]
                
        WorkHistory.objects.bulk_create(work_history)