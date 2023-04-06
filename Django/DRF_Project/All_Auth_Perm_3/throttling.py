from rest_framework.throttling import UserRateThrottle


class MyUserThrottle(UserRateThrottle):
    scope = "hussain"