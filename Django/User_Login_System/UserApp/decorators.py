from django.shortcuts import redirect


def unauthorised_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("user_profile")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func