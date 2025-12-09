from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    - Admin (is_staff): full access.
    - Authenticated non-admin: allowed read-only methods and POST (to create orders).
    - Unauthenticated: read-only only.
    """

    def has_permission(self, request, view):
        # Admins can do anything
        if request.user and request.user.is_staff:
            return True

        # Always allow safe requests (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Allow authenticated users to POST (e.g. create an Order)
        if request.method == "POST" and request.user and request.user.is_authenticated:
            return True

        # Otherwise deny (PUT/PATCH/DELETE remain admin-only)
        return False
