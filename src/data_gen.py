import csv
import time, datetime
import random


def create_new_csv():
    # create policy
    policy_head = ["policy_no", "policy_type", "policy_coverage", "issue_date", "effective_date", "expiry_date", "reinstatement_effective_date", 
                   "first_premium_due_date", "premium_payment_frequency", "premium_payment_account_type", "waiver_of_premiums",
                   "insured_id", "policy_owner_fname", "policy_owner_mname", "policy_owner_lname", "policy_payer", "policy_beneficiary"]
    
    path = "csv_files/policy.csv"
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(policy_head)

    # create insured
    insured_head = ["ipolicynsured_id", "insured_fname", "insured_mname", "insured_lname", "insured_dob", "insured_age", 
                    "insured_address", "insured_home_phone", "insured_cell_phone", "insured_email", "insured_family_doctor",
                    "is_insured_smoke", "diagnosis_id", "illness_history_id", "marriage_status"]
    
    path = "csv_files/insured.csv"
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(insured_head)

    # create family
    family_head = ["policynsured_id", "insured_name", "relative_name", "relative_dob", "relationship"]
    
    path = "csv_files/family.csv"
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(family_head)
    

    # create medical_history
    medical_history_head = ["medical_history_id", "patient_name", "symptoms_began_date", "diagnosis_date", "treatment_date", 
                            "prescription_date", "had_same_condition_before", "smoke_status"]
    
    path = "csv_files/medical_history.csv"
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(medical_history_head)

    # create diagnosis
    diagnosis_head = ["diagnosis_id", "patient_name", "diagnosis_date", "primary_diagnosis", "primary_symptoms", "secondary_diagnosis",
                      "secondary_symptoms", "objective_findings", "other_factors"]
    
    path = "csv_files/diagnosis.csv"
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(diagnosis_head)

    # create claim
    claim_head = ["claim_no", "policy_no", "claim_occurence_date", "claim_type", "is_fraud_claim"]

    path = "csv_files/claim.csv"
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(claim_head)

    # create claim detail
    claim_detail_head = ["claim_no", "occdate_before_polexpdate", "certissued_US_CAN", "is_suicide", "insuredid_match", "is_fraud_claim"]
    
    path = "csv_files/claim_det.csv"
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(claim_detail_head)

def create_new_insurance():

    insured_info = ""

    insured_age = random.randint(10, 80)

    # create policy
    print("creating policy object...")

    policy_no = int(time.time()*1000000)

    policy_type_list = ["term10", "term20", "100years"]
    policy_code = random.randint(0,2)
    policy_type = policy_type_list[policy_code]

    policy_coverage = "$" + str(random.randint(100,9999) * 1000)

    issue_year = random.randint(1990, 2023)
    issue_month = random.randint(1, 12)
    issue_day = random.randint(1, 28)

    issue_date = str(datetime.datetime(issue_year, issue_month, issue_day, 1,1,1))
    
    effective_day = issue_day + random.randint(3, 7)
    if effective_day > 28:
        effective_day = 28

    effective_date = str(datetime.datetime(issue_year, issue_month, effective_day, 1,1,1))

    if policy_code == 0:
        expired_year = issue_year + 10
    elif policy_code == 1:
        expired_year = issue_year + 20
    else:
        expired_year = issue_year + (100 - insured_age)
    
    expiry_date = str(datetime.datetime(expired_year, issue_month, effective_day, 1,1,1))

    reinstatement_effective_date = effective_date

    first_premium_due_date = effective_date

    payment_frequency_list = ["monthly", "annually", "full"]

    premium_payment_frequency = payment_frequency_list[random.randint(0,2)]

    payment_type_list = ["Credit Card", "Debit Card", "Cheque", "BankDraft"]

    premium_payment_account_type = payment_type_list[random.randint(0,3)]

    waiver_of_premiums = (random.randint(0,1) == 1)

    insured_id = int(time.time()*1000000)

    policy_owner_fname = get_random_str()
    policy_owner_mname = get_random_str()
    policy_owner_lname = get_random_str()

    policy_payer = get_random_str()

    policy_beneficiary = policy_payer

    my_policy = [policy_no, policy_type, policy_coverage, issue_date, effective_date, expiry_date, reinstatement_effective_date, 
                 first_premium_due_date, premium_payment_frequency, premium_payment_account_type, waiver_of_premiums,
                 insured_id, policy_owner_fname, policy_owner_mname, policy_owner_lname, policy_payer, policy_beneficiary]
    
    path = "csv_files/policy.csv"
    with open(path, "a+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(my_policy)


    # create insured
    print("creating insured object...")
    birth_year = 2024 - insured_age
    birth_month = random.randint(1,12)
    birth_day = random.randint(1,28)

    insured_dob = str(datetime.datetime(birth_year, birth_month, birth_day, 1,1,1))

    insured_address = get_random_str()

    insured_home_phone = random.randint(6471110001, 6479999999)

    insured_cell_phone = random.randint(6471110001, 6479999999)

    insured_email = policy_owner_lname + "." + policy_owner_fname + "@azure.com"

    insured_family_doctor = get_random_str()

    is_insured_smoke = (random.randint(0,1) == 1)

    has_diagnosis = (random.randint(0,1) == 1)
    if has_diagnosis:
        diagnosis_id = int(time.time()*1000000)
    else:
        diagnosis_id = 0
    
    has_medical_history = (random.randint(0,1) == 1)
    if has_medical_history:
        illness_history_id = int(time.time()*1000000)
    else:
        illness_history_id = 0

    if insured_age < 22:
        marriage_status = False
    else:
        marriage_status = (random.randint(0,1) == 1)

    my_insured = [insured_id, policy_owner_fname, policy_owner_mname, policy_owner_lname, insured_dob, insured_age, 
                    insured_address, insured_home_phone, insured_cell_phone, insured_email, insured_family_doctor,
                    is_insured_smoke, diagnosis_id, illness_history_id, marriage_status]

    path = "csv_files/insured.csv"
    with open(path, "a+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(my_insured)


    # create family
    print("creating family object...")
    my_family = []
    if insured_age < 22:
        family_count = 0
    else:
        family_count = random.randint(0,3)
        spouse_done = (random.randint(0,1) == 1)
    for i in range(family_count):
        if marriage_status and not spouse_done:
            relate_name = get_random_str()
            relate_birth_year = random.randint(1950, 2000)
            relate_birth_month = random.randint(1,12)
            relate_birth_day = random.randint(1,28)
            relate_dob = str(datetime.datetime(relate_birth_year, relate_birth_month, relate_birth_day, 1,1,1))
            relationship = "spouse"
            my_family.append([insured_id,policy_owner_fname,relate_name,relate_dob,relationship])
            spouse_done = True
        else:
            relate_name = get_random_str()
            age_range =2024-insured_age-1
            # print(age_range)
            relate_birth_year = random.randint((age_range+20),2023)
            relate_birth_month = random.randint(1,12)
            relate_birth_day = random.randint(1,28)
            relate_dob = str(datetime.datetime(relate_birth_year, relate_birth_month, relate_birth_day, 1,1,1))
            relationship = "child"
            my_family.append([insured_id,policy_owner_fname,relate_name,relate_dob,relationship])
    if family_count > 0:
        path = "csv_files/family.csv"
        with open(path, "a+") as f:
            csv_writer = csv.writer(f)
            for i in my_family:
                csv_writer.writerow(i)
            

    # create medical_history
    print("creating medical_history object...")
    if illness_history_id != 0:
        patient_name = policy_owner_fname

        symptoms_begin_year = birth_year + random.randint(1, insured_age-1)
        symptoms_begin_month = random.randint(1,12)
        symptoms_begin_day = random.randint(1,28)
        symptoms_began_date = str(datetime.datetime(symptoms_begin_year, symptoms_begin_month, symptoms_begin_day, 1,1,1))

        diagnosis_year = symptoms_begin_year + random.randint(1, 3)
        diagnosis_month = random.randint(1,12)
        diagnosis_day = random.randint(1,28)
        diagnosis_date = str(datetime.datetime(diagnosis_year, diagnosis_month, diagnosis_day,1,1,1))

        treatment_month = diagnosis_month + random.randint(0,12-diagnosis_month)
        treatment_date = str(datetime.datetime(diagnosis_year, treatment_month, diagnosis_day,1,1,1))

        prescription_month = treatment_month + random.randint(0,12-treatment_month)
        prescription_date = str(datetime.datetime(diagnosis_year, prescription_month, diagnosis_day,1,1,1))

        have_same_condition_before = (random.randint(0,1) == 1)

        my_medical_history = [illness_history_id, patient_name, symptoms_began_date, diagnosis_date, treatment_date, 
                            prescription_date, have_same_condition_before, is_insured_smoke]
        path = "csv_files/medical_history.csv"
        with open(path, "a+") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(my_medical_history)
        



    # create diagnosis
    print("creating diagnosis object...")
    if diagnosis_id != 0:
        patient_name = policy_owner_fname

        diagnosis_year = birth_year + random.randint(1, insured_age-1)
        diagnosis_month = random.randint(1,12)
        diagnosis_day = random.randint(1,28)

        diagnosis_date = str(datetime.datetime(diagnosis_year, diagnosis_month, diagnosis_day,1,1,1))

        primary_diagnosis = get_random_str()
        primary_symptoms = get_random_str()
        secondary_diagnosis = get_random_str()
        secondary_symptoms = get_random_str()
        objective_findings = get_random_str()
        other_factors = get_random_str()
        my_diagnosis = [diagnosis_id, patient_name, diagnosis_date, primary_diagnosis, primary_symptoms, secondary_diagnosis,
                      secondary_symptoms, objective_findings, other_factors]
        
        path = "csv_files/diagnosis.csv"
        with open(path, "a+") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(my_diagnosis)


    # claim
    print("create claim object...")
    my_claim = []
    my_claim_det = []
    claim_count = random.randint(0, 5)
    claimed = (random.randint(0,1) == 1)
    for i in range(claim_count):
        claim_no = int(time.time()*1000000)

        claim_occurence_year = random.randint(issue_year, expired_year)
        claim_occurence_month = random.randint(1,12)
        claim_occurence_day = random.randint(1,28)
        claim_occurence_date = str(datetime.datetime(claim_occurence_year, claim_occurence_month, claim_occurence_day, 1,1,1))

        claim_type = "LIFE"
        
        if claimed and i==0:
            is_fraud_claim = False
            my_claim_det.append([claim_no, 1, 1, 0, 1, is_fraud_claim])
        else:
            is_fraud_claim = True
            tag_point = random.randint(1,4)
            occdate_before_polexpdate = 0 if round(float(tag_point)/1.00, 2) == 1.00 else 1
            certissued_US_CAN = 0 if round(float(tag_point)/2.00, 2) == 1.00 else 1
            is_suicide = 1 if round(float(tag_point)/3.00, 2) == 1.00 else 0
            insuredid_match = 0 if round(float(tag_point)/4.00) == 1.00 else 1
            my_claim_det.append([claim_no, occdate_before_polexpdate, certissued_US_CAN, is_suicide, insuredid_match, is_fraud_claim])

        my_claim.append([claim_no, policy_no, claim_occurence_date, claim_type, is_fraud_claim])

    if claim_count > 0:
        path = "csv_files/claim.csv"
        with open(path, "a+") as f:
            csv_writer = csv.writer(f)
            for i in my_claim:
                csv_writer.writerow(i)
        
        path = "csv_files/claim_det.csv"
        with open(path, "a+") as f:
            csv_writer = csv.writer(f)
            for i in my_claim_det:
                csv_writer.writerow(i)

    print("done")

def get_random_str():
    result = ""
    number_char = random.randint(3, 15)
    for i in range(number_char):
        result = result + chr(random.randint(65,90))
    return result



if __name__ == "__main__":
    print("start...")
    print("create new csvs")
    create_new_csv()
    for i in range(0,5000):
        print("create no:",i)
        create_new_insurance()
    print("all done.")

