


from services.export_service import export_plants_csv

from services.watering_service import (
    view_watering_history,
    record_watering,
    delete_watering_log,
    get_all_plants,
    plants_due_for_watering
)


from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    send_file
)

from services.plant_service import (
    add_plant,
    view_all_plants,
    get_plant_by_id,
    update_plant,
    search_plants,
    filter_by_type,
    filter_by_location,
    filter_by_frequency
)

from services.auth_service import (
    login_user,
    register_user
)

from services.dashboard_service import (
    get_total_plants,
    get_total_watering_logs,
    get_total_health_logs,
    plants_by_type,
    plants_by_location,
    watering_frequency_statistics
)

from services.watering_service import (
    view_watering_history,
    record_watering,
    delete_watering_log,
    get_all_plants
)
from services._health_service import (
    record_health,
    view_health_history,
    delete_health_log
)

from services.plant_service import view_all_plants





app = Flask(__name__)

app.secret_key = "greenguardian_secret_key"


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# LOGIN
# ==========================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = login_user(username, password)

        if user:

            session["user_id"] = user[0]
            session["username"] = user[1]


            return redirect(url_for("dashboard"))

        else:

            flash("Invalid Username or Password")

    return render_template("login.html")


# ==========================================
# REGISTER
# ==========================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if register_user(username, password):

            flash("Registration Successful! Please Login.")

            return redirect(url_for("login"))

        else:

            flash("Username already exists!")

    return render_template("register.html")


# ==========================================
# DASHBOARD
# ==========================================

@app.route("/dashboard")
def dashboard():

    if "username" not in session:

        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        total_plants=get_total_plants(session["user_id"]),
        watering_logs=get_total_watering_logs(session["user_id"]),
        health_logs=get_total_health_logs(session["user_id"])
    )


@app.route("/statistics")
def statistics():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "statistics.html",
        type_stats=plants_by_type(session["user_id"]),
        location_stats=plants_by_location(session["user_id"]),
        frequency_stats=watering_frequency_statistics(session["user_id"])
    )

@app.route("/plants")
def plants():

    if "username" not in session:
        return redirect(url_for("login"))

    search = request.args.get("search")
    plant_type = request.args.get("type")
    location = request.args.get("location")
    frequency = request.args.get("frequency")

    if search:
        plants = search_plants(session["user_id"],search)

    elif plant_type:
        plants = filter_by_type(session["user_id"],plant_type)

    elif location:
        plants = filter_by_location(session["user_id"],location)

    elif frequency:
        plants = filter_by_frequency(session["user_id"],int(frequency))

    else:
        plants = view_all_plants(session["user_id"])

    return render_template(
        "plants.html",
        plants=plants
    )

@app.route("/add-plant", methods=["GET", "POST"])
def add_plant_page():

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        plant_name = request.form["plant_name"]
        plant_type = request.form["plant_type"]
        location = request.form["location"]
        watering_frequency = request.form["watering_frequency"]

        add_plant(
            plant_name,
            session["user_id"],
            plant_type,
            location,
            watering_frequency
        )

        flash("🌱 Plant added successfully!")

        return redirect(url_for("plants"))

    return render_template("add_plant.html")


@app.route("/edit-plant/<int:plant_id>", methods=["GET", "POST"])
def edit_plant(plant_id):

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        plant_name = request.form["plant_name"]
        plant_type = request.form["plant_type"]
        location = request.form["location"]
        watering_frequency = request.form["watering_frequency"]

        update_plant(
            session["user_id"],
            plant_id,
            plant_name,
            plant_type,
            location,
            watering_frequency
        )

        flash("Plant updated successfully!")

        return redirect(url_for("plants"))

    plant = get_plant_by_id(session["user_id"],plant_id)

    return render_template(
        "edit_plant.html",
        plant=plant
    )



@app.route("/delete-plant/<int:plant_id>")
def delete_plant_route(plant_id):

    if "username" not in session:
        return redirect(url_for("login"))

    from services.plant_service import delete_plant

    delete_plant(session["user_id"],plant_id)

    flash("Plant deleted successfully!")

    return redirect(url_for("plants"))



# ==========================================
# WATERING MANAGEMENT
# ==========================================

@app.route("/watering")
def watering():

    if "username" not in session:
        return redirect(url_for("login"))

    records = view_watering_history(session["user_id"])

    return render_template(
        "watering.html",
        records=records
    )


@app.route("/add-watering", methods=["GET", "POST"])
def add_watering():

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        plant_id = request.form["plant_id"]
        notes = request.form["notes"]

        record_watering(
            session["user_id"],
            plant_id,
            notes
        )

        flash("💧 Watering record added successfully!")

        return redirect(url_for("watering"))

    plants = view_all_plants(session["user_id"])

    return render_template(
        "add_watering.html",
        plants=plants
    )


@app.route("/delete-watering/<int:log_id>")
def delete_watering(log_id):

    if "username" not in session:
        return redirect(url_for("login"))

    delete_watering_log(session["user_id"],log_id)

    flash("Watering record deleted!")

    return redirect(url_for("watering"))


@app.route("/watering-reminder")
def watering_reminder():

    if "username" not in session:
        return redirect(url_for("login"))

    plants = plants_due_for_watering(session["user_id"])

    return render_template(
        "watering_reminder.html",
        plants=plants
    )



# ==========================================
# HEALTH MANAGEMENT
# ==========================================

@app.route("/health")
def health():

    if "username" not in session:
        return redirect(url_for("login"))

    records = view_health_history(session["user_id"])

    return render_template(
        "health.html",
        records=records
    )


@app.route("/add-health", methods=["GET", "POST"])
def add_health():

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        plant_id = request.form["plant_id"]
        status = request.form["status"]
        notes = request.form["notes"]

        record_health(
            session["user_id"],
            plant_id,
            status,
            notes
        )

        flash("Health record added successfully!")

        return redirect(url_for("health"))

    plants = view_all_plants(session["user_id"])

    return render_template(
        "add_health.html",
        plants=plants
    )


@app.route("/delete-health/<int:health_log_id>")
def delete_health(health_log_id):

    if "username" not in session:
        return redirect(url_for("login"))

    delete_health_log(session["user_id"],health_log_id)

    flash("Health record deleted successfully!")

    return redirect(url_for("health"))





@app.route("/export-csv")
def export_csv():

    if "username" not in session:
        return redirect(url_for("login"))

    file_path = export_plants_csv(session["user_id"])

    return send_file(
        file_path,
        as_attachment=True
    )

@app.route("/export")
def export():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("export.html")


# ==========================================
# LOGOUT
# ==========================================

@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.")

    return redirect(url_for("login"))


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)