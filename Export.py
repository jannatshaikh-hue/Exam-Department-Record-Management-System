from flask import Response

@app.route("/export")
def export_csv():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT name, roll, year, division, department FROM students")
    rows = cur.fetchall()
    conn.close()

    def generate():
        yield "Name,Roll,Year,Division,Department\n"
        for r in rows:
            yield f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]}\n"

    return Response(
        generate(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=students.csv"}
    )
