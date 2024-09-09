from django.http import HttpResponseForbidden
from functools import wraps

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user has a Profile and if their role matches the required one
            if hasattr(request.user, 'profile') and request.user.profile.role == role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to perform this action.")
        return _wrapped_view
    return decorator
