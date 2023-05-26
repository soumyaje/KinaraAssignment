from flask import Flask, jsonify, request

app = Flask(__name__)

# To Load student details from a JSON file
def load_student_details():
    with open('student_details.json', 'r') as file:
        student_data = json.load(file)
    return student_data

# Here Implementing the Load Student Detail's API
@app.route('/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    students = load_student_details()

    # Calculating pagination parameters
    total_students = len(students)
    total_pages = (total_students // page_size) + (1 if total_students % page_size > 0 else 0)
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    # Paginating the student details
    paginated_students = students[start_index:end_index]

    # Return the paginated student details as JSON response
    response = {
        'page': page,
        'page_size': page_size,
        'total_students': total_students,
        'total_pages': total_pages,
        'students': paginated_students
    }
    return jsonify(response)

# Implementing the Server-side Filtring API
@app.route('/students/filter', methods=['POST'])
def filter_students():
    filter_criteria = request.json

    students = load_student_details()

    filtered_students = []

    # Applying filters based on the filter criteria
    for student in students:
        if student_matches_criteria(student, filter_criteria):
            filtered_students.append(student)

    # Return the filtered student details as JSON response
    response = {
        'students': filtered_students
    }
    return jsonify(response)

# Helper function is used  to check if a student matches the filter criteria
def student_matches_criteria(student, filter_criteria):
    
    pass

if __name__ == '__main__':
    app.run()
