from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.get('/units')
def getUnits():
    print("unit get")
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id, 
                unit_name AS name, 
                unit_code AS code, 
                unit_level AS level, 
                credit_points AS cp,
                unit_description AS description,
                academic_unit,
                available_semesters
            FROM units
            """)

        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        result = []
        for row in rows:
            current = {colnames[i]: row[i] for i in range(len(colnames))}
            result.append(current)

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)

@app.get('/units/code/<unit_code>')
def getUnitByCode(unit_code):
    print("unit get")
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id, 
                unit_name AS name, 
                unit_code AS code, 
                unit_level AS level, 
                credit_points AS cp,
                unit_description AS description,
                academic_unit,
                available_semesters
            FROM units
            WHERE unit_code = %s
            """, (unit_code,))

        colnames = [desc[0] for desc in cur.description]
        row = cur.fetchone()
        result = {colnames[i]: row[i] for i in range(len(colnames))}

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)

@app.post('/units')
def postUnits():
    print("post unit")
    result = 'error'
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO units (id, unit_name, unit_code, unit_level, available_semesters, credit_points, academic_unit, unit_description)
            VALUES(gen_random_uuid(), %s, %s, %s, %s, %s, %s, %s) 
            """,
                    (request.args["name"], request.args["code"], request.args["level"], request.args["semesters"], request.args["cp"], request.args["academic_unit"], request.args["description"]))

        result = jsonify('success')
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        result = jsonify({'error': str(error)})

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return result


@app.get('/unit-groups/<group_id>/units')
def getUnitGroup(group_id):

    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                unit_id AS id, 
                unit_name AS name, 
                unit_code AS code, 
                unit_level AS level, 
                available_semesters
            FROM units
            RIGHT OUTER JOIN unit_groups ON unit_groups.unit_id = unit_id
            WHERE unit_groups.group_id = %s
            """, (group_id,))

        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        result = []
        for row in rows:
            current = {colnames[i]: row[i] for i in range(len(colnames))}
            result.append(current)

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)


@app.post('/unit-groups/<group_id>/units/<unit_id>')
def postUnitGroup(group_id, unit_id):

    result = 'error'
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO unit_groups (id, group_id, unit_id)
            VALUES(gen_random_uuid(), %s, %s) 
            """,
                    (group_id, unit_id))

        result = jsonify('success')
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        result = jsonify({'error': str(error)})

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return result


@app.get('/groups')
def getGroups():
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id, 
                group_name AS name
            FROM groups
            """)

        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        result = []
        for row in rows:
            current = {colnames[i]: row[i] for i in range(len(colnames))}
            result.append(current)

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)

@app.get('/groups/group/<name>')
def getGroupsByName(name):
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id, 
                group_name AS name
            FROM groups
            WHERE group_name = %s
            """, (name,))

        colnames = [desc[0] for desc in cur.description]
        row = cur.fetchone()
        result = {colnames[i]: row[i] for i in range(len(colnames))}

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)


@app.post('/groups')
def postGroups():

    result = 'error'
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO groups (id, group_name)
            VALUES(gen_random_uuid(), %s) 
            """,
                    (request.args["name"],))

        result = jsonify('success')
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        result = jsonify({'error': str(error)})

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return result


@app.get('/units/<unit_id>/prerequisites')
def getPrerequisites(unit_id):
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT prerequisite_list
            FROM unit_prerequisites
            WHERE unit_prerequisites.unit_id = %s
            """, (unit_id,))

        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        result = []
        for row in rows:
            current = {colnames[i]: row[i] for i in range(len(colnames))}
            result.append(current)

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)


@app.post('/units/<unit_id>/prerequisites')
def postPrerequisites(unit_id):

    result = 'error'
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO unit_prerequisites (id, unit_id, prerequisite_list)
            VALUES(gen_random_uuid(), %s, %s) 
            """,
                    (unit_id, request.args["prerequisite_list"]))

        result = jsonify('success')
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        result = jsonify({'error': str(error)})

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return result


@app.get('/units/<unit_id>/prohibitions')
def getProhibitions(unit_id):
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT prohibition_list
            FROM unit_prohibitions
            WHERE unit_prohibitions.unit_id = %s
            """, (unit_id,))

        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        result = []
        for row in rows:
            current = {colnames[i]: row[i] for i in range(len(colnames))}
            result.append(current)

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)


@app.post('/units/<unit_id>/prohibitions')
def postProhibitions(unit_id):

    result = 'error'
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO unit_prohibitions (id, unit_id, prohibition_list)
            VALUES(gen_random_uuid(), %s, %s) 
            """,
                    (unit_id, request.args["prohibition_list"]))

        result = jsonify('success')
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        result = jsonify({'error': str(error)})

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return result


@app.get('/units/<unit_id>/corequisites')
def getCorequisites(unit_id):
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT corequisite_list
            FROM unit_corequisites
            WHERE unit_corequisites.unit_id = %s
            """, (unit_id,))

        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        result = []
        for row in rows:
            current = {colnames[i]: row[i] for i in range(len(colnames))}
            result.append(current)

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)


@app.post('/units/<unit_id>/corequisites')
def postCorequisites(unit_id):

    result = 'error'
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO unit_corequisites (id, unit_id, corequisite_list)
            VALUES(gen_random_uuid(), %s, %s) 
            """,
                    (unit_id, request.args["corequisite_list"]))

        result = jsonify('success')
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        result = jsonify({'error': str(error)})

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return result

@app.get('/units/<unit_id>/assumed_knowledge')
def getAssumedKnowledge(unit_id):
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT assumed_knowledge_list
            FROM unit_assumed_knowledge
            WHERE unit_assumed_knowledge.unit_id = %s
            """, (unit_id,))

        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        result = []
        for row in rows:
            current = {colnames[i]: row[i] for i in range(len(colnames))}
            result.append(current)

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)


@app.post('/units/<unit_id>/assumed_knowledge')
def postAssumedKnowledge(unit_id):

    result = 'error'
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO unit_assumed_knowledge (id, unit_id, assumed_knowledge_list)
            VALUES(gen_random_uuid(), %s, %s) 
            """,
                    (unit_id, request.args["assumed_knowledge_list"]))

        result = jsonify('success')
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        result = jsonify({'error': str(error)})

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return result


@app.get('/units/<unit_id>/reviews')
def getUnitReviews(unit_id):
    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id, 
                rating,
                comment
            FROM unit_reviews
            WHERE unit_id = %s
            """, (unit_id,))

        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()

        result = []
        for row in rows:
            current = {colnames[i]: row[i] for i in range(len(colnames))}
            result.append(current)

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)


@app.post('/units/<unit_id>/reviews')
def postUnitReviews(unit_id):

    try:
        conn = psycopg2.connect(
            dbname="postgres", user="postgres", password="postgres", host='0.0.0.0', port=5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO unit_reviews (id, unit_id, rating, comment)
            VALUES (gen_random_uuid(), %s, %s, %s)
            """, (unit_id, request.args["rating"], request.args["comment"]))
        conn.commit()

        result = 'success'

    except (Exception, psycopg2.Error) as error:
        result = {'error': str(error)}

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
