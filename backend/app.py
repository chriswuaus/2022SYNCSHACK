from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.get('/units')
def getUnits():
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host = '0.0.0.0', port = 5432)
        cur = conn.cursor()

        cur.execute("""
            SELECT
                id, 
                unit_name AS name, 
                unit_code AS code, 
                unit_level AS level, 
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


@app.post('/units')
def postUnits():

    result = 'error'
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host = '0.0.0.0', port = 5432)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO units (id, unit_name, unit_code, unit_level, available_semesters)
            VALUES(gen_random_uuid(), %s, %s, %s, %s) 
            """, 
            (request.args["name"], request.args["code"], request.args["level"], request.args["semesters"]))

        result = jsonify('success')

    except (Exception, psycopg2.Error) as error:
        result = jsonify({'error': str(error)})
        
    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()

        return result
        

if __name__ == '__main__':
	app.run(debug=True)
