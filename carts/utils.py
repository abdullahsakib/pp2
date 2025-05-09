# def get_session_key(request):
#     cart = request.session.session_key  # Get the cart ID from the session
#     if not cart:
#         cart = request.session.create()  # Create a new session key if it doesn't exist
#     return cart

def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key
