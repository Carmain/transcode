from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    return obj.owner == request.user

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
      if request.user:
        return account == request.user
      return False
