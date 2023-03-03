from django.shortcuts import render, redirect
from user_auth.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def home(request):
    """
    Simpel function that redirect te
    """
    return render(request, "base.html")


def signup(request):
    """
    In this we provide the html field validation,
    asissing the to the our models fields and than create the user.
    and redirect to the destination.
    """

    # Check if the retrieving data has post method or not.
    if request.method == "POST":
        # asigning the HTML form value to model fields.
        username = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        image = request.FILES.get("image")

        # validate and store the msg to the messages object.
        # that we can fetch in our redirected file.
        if CustomUser.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username."
            )

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")

        # If any errors, redirect to same page with old values
        if messages.get_messages(request):
            return render(
                request,
                "signup.html",
                {
                    "username": username,
                    "fname": fname,
                    "lname": lname,
                    "email": email,
                },
            )

        # create the user and save to the model.
        myuser = CustomUser.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.image = image
        myuser.save()
        messages.success(request, "Account Created succesfully")
        return redirect("signin")
    return render(request, "signup.html")


def signin(request):
    """
    In this fucntion we provide the validation of the user credantials.
    that we can use for login.
    We use the django contrib auth, authanticate function for validating.
    """
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        # authenticate the user with our database.
        user = authenticate(username=username, password=pass1)

        # if user is validate then rediecting to the destination.
        # either redirecting to the sigin page.
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "dashboard.html", {"username": username})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect("signin")

    return render(request, "login.html")


def signout(request):
    """
    Here we provide the logou functionality using the inbuilt function,
    django.contrib.auth logout function.
    And redirect to the siging page.
    """
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect("signin")
