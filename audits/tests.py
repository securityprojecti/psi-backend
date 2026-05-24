from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from companies.models import Company
from .models import Audit, Control, Answer


class AuditPermissionTests(TestCase):
	"""Testes para verificar as permissões de acesso aos audits."""

	def setUp(self):
		# Criar dois usuários
		self.user1 = User.objects.create_user(username='user1', password='pass123')
		self.user2 = User.objects.create_user(username='user2', password='pass123')

		# Criar companies para cada usuário
		self.company1 = Company.objects.create(name='Company 1', user=self.user1)
		self.company2 = Company.objects.create(name='Company 2', user=self.user2)

		# Criar audits para cada company
		self.audit1 = Audit.objects.create(company=self.company1)
		self.audit2 = Audit.objects.create(company=self.company2)

		# Criar um controle
		self.control = Control.objects.create(
			code='AC-01',
			title='Access Control',
			description='Control access to systems',
			type='Access',
			iso_type='ISO 27001'
		)

		# Cliente REST
		self.client = APIClient()

	def test_user_can_see_own_audits(self):
		"""Usuário só consegue ver seus próprios audits."""
		self.client.force_authenticate(user=self.user1)
		response = self.client.get('/api/v1/audits/')
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data['results']), 1)
		self.assertEqual(response.data['results'][0]['id'], self.audit1.id)

	def test_user_cannot_see_other_audits(self):
		"""Usuário não consegue ver audits de outras pessoas."""
		self.client.force_authenticate(user=self.user1)
		response = self.client.get('/api/v1/audits/')
		
		# Verificar que o audit2 não está na lista
		audit_ids = [audit['id'] for audit in response.data['results']]
		self.assertNotIn(self.audit2.id, audit_ids)

	def test_unauthenticated_user_cannot_see_audits(self):
		"""Usuário não autenticado não consegue ver audits."""
		response = self.client.get('/api/v1/audits/')
		
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AnswerPermissionTests(TestCase):
	"""Testes para verificar as permissões de acesso às answers."""

	def setUp(self):
		# Criar dois usuários
		self.user1 = User.objects.create_user(username='user1', password='pass123')
		self.user2 = User.objects.create_user(username='user2', password='pass123')

		# Criar companies para cada usuário
		self.company1 = Company.objects.create(name='Company 1', user=self.user1)
		self.company2 = Company.objects.create(name='Company 2', user=self.user2)

		# Criar audits para cada company
		self.audit1 = Audit.objects.create(company=self.company1)
		self.audit2 = Audit.objects.create(company=self.company2)

		# Criar um controle
		self.control = Control.objects.create(
			code='AC-01',
			title='Access Control',
			description='Control access to systems',
			type='Access',
			iso_type='ISO 27001'
		)

		# Criar answers para cada audit
		self.answer1 = Answer.objects.create(
			audit=self.audit1,
			control=self.control,
			status='Compliant'
		)
		self.answer2 = Answer.objects.create(
			audit=self.audit2,
			control=self.control,
			status='Non-Compliant'
		)

		# Cliente REST
		self.client = APIClient()

	def test_user_can_see_own_answers(self):
		"""Usuário só consegue ver suas próprias answers."""
		self.client.force_authenticate(user=self.user1)
		response = self.client.get('/api/v1/answers/')
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data['results']), 1)
		self.assertEqual(response.data['results'][0]['id'], self.answer1.id)

	def test_user_cannot_see_other_answers(self):
		"""Usuário não consegue ver answers de outras pessoas."""
		self.client.force_authenticate(user=self.user1)
		response = self.client.get('/api/v1/answers/')
		
		# Verificar que o answer2 não está na lista
		answer_ids = [answer['id'] for answer in response.data['results']]
		self.assertNotIn(self.answer2.id, answer_ids)
