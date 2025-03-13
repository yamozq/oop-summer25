students = [
    {
        'first_name': 'Kamran',
        'last_name': 'Ibrahimli',
        'index_number': '35315', 
        'nationality': 'Azerbaijani', 
        'starting_date': '2025-03-13',
        'courses': ['Mathematics', 'Computer Science', 'Physics']  

    },
    {
        'first_name': 'Atilla',
        'last_name': 'Quliyev',
        'index_number': '003500',
        'nationality': 'Azerbaijani', 
        'starting_date': '2025-01-11',
        'courses': ['Marketing', 'Law', 'Physics'] 
    },
    {
        'first_name': 'Hleb',
        'last_name': 'Korol',
        'index_number': '52000',
        'nationality': 'Belarus', 
        'starting_date': '2024-09-01',
        'courses': ['Marketing', 'Law', 'Physics'] 
    }
]

for student in students:
    print("Name:", student['first_name'], student['last_name'])
    print("Index:", student['index_number'])
    print("Nationality:", student['nationality']) 
    print("starting_date:", student['nationality'])
    print("courses:", student['courses'])
