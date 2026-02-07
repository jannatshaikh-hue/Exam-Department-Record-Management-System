@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
        INSERT OR IGNORE INTO students
        (name, roll, year, division, department)
        VALUES (?,?,?,?,?)
        """, (
            request.form["name"],
            request.form["roll"],
            request.form["year"],
            request.form["division"],
            request.form["department"]
        ))

        conn.commit()
        conn.close()
        return redirect("/students")

    return render_template("add_student.html")
