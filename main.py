patients={}

def add_patient():
    patient_id=input("Enter patient-id: ")
    name=input("Enter patient name: ")
    age=input("Enter patient age: ")
    illness=input("Enter patient illness: ")
    patients[patient_id]={'Name': name, 'Age': age, 'Illness': illness}
    print(f"Patient-id:{patient_id} added.")

def update_patient():
    patient_id=input("Enter patient-id (for update): ")
    if patient_id in patients:
        name=input("Enter new patient name (or blank to skip): ")
        age=input("Enter new patient age (or blank to skip): ")
        illness=input("Enter new patient illness (or blank to skip): ")
        
        if 'Name':
            patients[patient_id]['Name'] = name
        elif 'Age':
            patients[patient_id]['Age'] = age
        elif 'Illness':
            patients[patient_id]['Illness'] = illness
        
        print(f"Patient-id:{patient_id} updated.")

    else:
        print(f"Patient-id not found.")

def get_patient():
    patient_id=input("Enter patient-id (for info): ")
    print(patients.get(patient_id,"Patient-id not found."))

schedules={}

def add_schedule():
    doctor_id=input("Enter doctor-id: ")
    name=input("Enter doctor name: ")
    time_slot=input("Enter doctor time-slot: ")
    schedules[doctor_id]={'Name': name, 'Time-slot': time_slot}
    print(f"Doctor-id:{doctor_id} added.")

def get_schedule():
    doctor_id=input("Enter doctor-id (for info): ")
    print(schedules.get(doctor_id,"Doctor-id not found."))

def calculate_bill():
    consultation_fee=float(input("Enter consultation fee: "))
    treatement_fee=float(input("Enter treatement fee: "))
    service_fee=float(input("Enter service fee: "))
    total=sum([consultation_fee,treatement_fee,service_fee])
    print(f"Total: Rs.{int(total) if total.is_integer() else total}")

inventory={}

def update_inventory():
    item=input("Enter item name: ")
    quantity=int(input(f"Enter {item} quantity: "))
    inventory[item]= inventory.get(item, 0) + quantity
    print(f"Inventory updated. item:{item}, total quantity:{inventory[item]}.")

def check_inventory():
    item=input("Enter item name (for check): ")
    print(inventory.get(item,"Item-name not found."))

def emergency_alert():
    patient_name=input("Enter patient name (for alert): ")
    print(f"Emergency Alert! for patient {patient_name}.")

visits={}

def record_visit():
    patient_name=input("Enter patient name (for visit): ")
    visits[patient_name]=visits.get(patient_name,0) + 1
    print(f"Patient {patient_name} visited.")

def generate_report():
    patient_name=input("Enter patient name (for visit): ")
    if patient_name in visits:
        print(f"Patient Visited Report: ")
        print(f"Patient name: {patient_name}, total visits: {visits[patient_name]}.")
    else:
        print(f"Patient name not found.")

def send_reminder():
    patient_name=input("Enter patient name (for reminder): ")
    print(f"Reminder Alert! for patient: {patient_name}. Kindly visit the doctor chamber.")

roles={'doctor': ['view_patient','update_patient'], 'nurse': ['view_patient'], 'admin': ['all_access']}

def check_access():
    role=input("Enter your role (doctor/nurse/admin): ").lower()
    action=input("Enter your action (view_patient/update_patient): ").lower()
    if 'all_access' in roles.get(role,[]) or action in roles.get(role,[]):
        print(f"Access granted to {role} for {action}.")
    else:
        print(f"Access denied to {role} for {action}.")

def send_prescription_to_pharmacy():
    patient_name=input("Enter patient name (for sending prescription to pharmacy): ")
    prescription_details=input("Enter prescription details: ")
    print(f"Patient: {patient_name}. Prescription details: {prescription_details}.")

symptoms_db={
    'fever': ['Common Cold', 'Flu', 'COVID-19', 'Malaria', 'Dengue'],
    'cough': ['Bronchitis', 'Pneumonia', 'Asthma', 'Allergies', 'Tuberculosis'],
    'headache': ['Migraine', 'Tension Headache', 'Cluster Headache', 'Sinusitis', 'Hypertension'],
    'sore_throat': ['Strep Throat', 'Viral Pharyngitis', 'Allergies', 'Mononucleosis'],
    'nausea': ['Gastroenteritis', 'Food Poisoning', 'Motion Sickness', 'Pregnancy'],
    'fatigue': ['Anemia', 'Sleep Apnea', 'Chronic Fatigue Syndrome', 'Depression'],
    'shortness_of_breath': ['Asthma', 'Chronic Obstructive Pulmonary Disease (COPD)', 'Heart Failure', 'Pneumonia'],
    'chest_pain': ['Angina', 'Heart Attack', 'Pulmonary Embolism', 'Costochondritis'],
    'abdominal_pain': ['Appendicitis', 'Gallstones', 'Pancreatitis', 'Irritable Bowel Syndrome (IBS)'],
    'joint_pain': ['Arthritis', 'Gout', 'Bursitis', 'Lupus']
}

for pb,symptom in enumerate (symptoms_db):
    print(f"Problem: {symptom}.")
    
    
def suggest_diagnosis():
    problem=input("Enter patient problem: ").lower()
    if problem in symptoms_db:
        print(symptoms_db.get(problem, "Problem not found."))

def main():
    while True:
        print("\nHospital Management System")
        print("1. Add patient")
        print("2. Update patient")
        print("3. Get patient")
        print("4. Add schedule")
        print("5. Get schedule")
        print("6. Calculate bill")
        print("7. Update inventory")
        print("8. Check inventory")
        print("9. Emergency alert")
        print("10. Record visit")
        print("11. Generate report")
        print("12. Send reminder")
        print("13. Check access")
        print("14. Send prescription to pharmacy")
        print("15. Suggest diagnos")
        print("16. Exit")

        user=input("Enter your input(1-16): ")

        if (user=='1'):
            add_patient()
        elif (user=='2'):
            update_patient()
        elif (user=='3'):
            get_patient()
        elif (user=='4'):
            add_schedule()
        elif (user=='5'):
            get_schedule()
        elif (user=='6'):
            calculate_bill()
        elif (user=='7'):
            update_inventory()
        elif (user=='8'):
            check_inventory()
        elif (user=='9'):
            emergency_alert()
        elif (user=='10'):
            record_visit()
        elif (user=='11'):
            generate_report()
        elif (user=='12'):
            send_reminder()
        elif (user=='13'):
            check_access()
        elif (user=='14'):
            send_prescription_to_pharmacy()
        elif (user=='15'):
            suggest_diagnosis()
        elif (user=='16'):
            print("Exiting...")
            break
        else:
            print("Try again, Please enter between (1-16).")

main()
        
        


