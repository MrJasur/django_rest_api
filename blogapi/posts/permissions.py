from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #faqat korish uchun ruxsar beriladi
        if request.method in permissions.SAFE_METHODS:
            return True

        #update only for creator
        return obj.author == request.user
