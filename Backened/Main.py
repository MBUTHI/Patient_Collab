Doctors_Avaiable = ["Dr. Smith", "Dr. Johnson", "Dr. Lee", "Dr. Brown"] 
Patients_List = []  
def book_appointment(patient_name, doctor_name):
    if doctor_name in Doctors_Avaiable:
        Patients_List.append((patient_name, doctor_name))
        print(f"Appointment booked for {patient_name} with {doctor_name}.")
    else:
        print(f"Sorry, {doctor_name} is not available. Please choose another doctor.")

print("Welcome to the Hospital Appointment System!")
while True:
    patient_name = input("Enter your name (or type 'exit' to quit): ")
    if patient_name.lower() == 'exit':
        break
    print("Available doctors:")
    for doctor in Doctors_Avaiable:
        print(doctor)
    doctor_name = input("Enter the name of the doctor you want to book an appointment with: ")
    book_appointment(patient_name, doctor_name)