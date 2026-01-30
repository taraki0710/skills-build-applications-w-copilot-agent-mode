from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='TestTeam', description='desc')
        self.assertEqual(str(team), 'TestTeam')
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@example.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'U')
    def test_activity_create(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(name='U2', email='u2@example.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Run', duration=10, date='2026-01-01')
        self.assertEqual(str(activity), 'U2 - Run (2026-01-01)')
    def test_workout_create(self):
        workout = Workout.objects.create(name='W', description='desc')
        self.assertEqual(str(workout), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T3', description='d3')
        leaderboard = Leaderboard.objects.create(team=team, total_points=42)
        self.assertIn('T3', str(leaderboard))
