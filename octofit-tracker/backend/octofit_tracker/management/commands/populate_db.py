from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # MongoDBコレクションを直接drop
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.activity.drop()
        db.workout.drop()
        db.leaderboard.drop()
        db.user.drop()
        db.team.drop()

        # チーム作成
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # ユーザー作成
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
        ]

        # アクティビティ作成
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=timezone.now().date())

        # ワークアウト作成
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Flexibility and strength')
        w1.suggested_for.set([users[0], users[1]])
        w2.suggested_for.set([users[2], users[3]])

        # リーダーボード作成
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
