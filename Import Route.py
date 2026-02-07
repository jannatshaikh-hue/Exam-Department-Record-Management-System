@app.route("/import", methods=["POST"])
def import_csv():
    file = request.files["file"]

    if not file:
        return redirect("/students")

    conn = get_db()
    cur = conn.cursor()

    csv_data = file.stream.read().decode("utf-8").splitlines()
    reader = csv.DictReader(csv_data)

    for row in reader:
        cur.execute("""
        INSERT OR IGNORE INTO students
        (name, roll, year, division, department)
        VALUES (?,?,?,?,?)
        """, (
            row["Name"],
            row["Roll"],
            row["Year"],
            row["Division"],
            row["Department"]
        ))

    conn.commit()
    conn.close()
    return redirect("/students")
