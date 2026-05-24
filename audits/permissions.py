from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Permissão customizada para que o usuário só veja seus próprios objetos.
	"""

	def has_object_permission(self, request, view, obj):
		if hasattr(obj, 'company'):
			return obj.company.user == request.user
		elif hasattr(obj, 'user'):
			return obj.user == request.user
		return False


class IsCompanyOwner(permissions.BasePermission):
	"""
	Permissão para que o usuário só acesse companies e audits que lhe pertencem.
	"""

	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return request.user and request.user.is_authenticated
		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		if hasattr(obj, 'user'):
			return obj.user == request.user
		elif hasattr(obj, 'company'):
			return obj.company.user == request.user
		return False
