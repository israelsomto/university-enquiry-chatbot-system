# -*- coding: utf-8 -*-

CATEGORIES = {
    "admissions": {
        "name": "Admissions",
        "icon": '<i data-lucide="file-text" class="cat-title-icon"></i>',
        "description": "Requirements, courses, application process, and deadlines."
    },
    "general_info": {
        "name": "General Info",
        "icon": '<i data-lucide="landmark" class="cat-title-icon"></i>',
        "description": "Faculties, departments, location, contact, and academic calendar."
    },
    "student_faqs": {
        "name": "Student FAQs",
        "icon": '<i data-lucide="help-circle" class="cat-title-icon"></i>',
        "description": "Course registration, changing courses, hostels, and deferment."
    },
    "fees_payments": {
        "name": "Fees & Payments",
        "icon": '<i data-lucide="credit-card" class="cat-title-icon"></i>',
        "description": "Tuition fees, acceptance fees, payment deadlines, and procedures."
    },
    "policies": {
        "name": "Policies",
        "icon": '<i data-lucide="scroll" class="cat-title-icon"></i>',
        "description": "Attendance, examination rules, dress code, and graduation requirements."
    },
    "contact": {
        "name": "Contact & Help",
        "icon": '<i data-lucide="phone" class="cat-title-icon"></i>',
        "description": "Get in touch with university offices and find support."
    }
}

SYNONYMS = {
    "cost": "fee",
    "price": "fee",
    "prices": "fee",
    "fees": "fee",
    "charges": "fee",
    "charge": "fee",
    "amount": "fee",
    "payment": "fee",
    "payments": "fee",
    "tuition": "fee",
    "tuitions": "fee",
    
    "apply": "apply",
    "applying": "apply",
    "application": "apply",
    "applications": "apply",
    "enroll": "apply",
    "enrollment": "apply",
    "enrolling": "apply",
    
    "register": "registration",
    "registration": "registration",
    "registering": "registration",
    
    "requirements": "requirement",
    "requirement": "requirement",
    "required": "requirement",
    "qualification": "requirement",
    "qualifications": "requirement",
    "eligibility": "requirement",
    "eligible": "requirement",
    "criteria": "requirement",
    
    "nursing": "nursing",
    "nurse": "nursing",
    
    "hostel": "hostel",
    "hostels": "hostel",
    "accommodation": "hostel",
    "accommodations": "hostel",
    "room": "hostel",
    "rooms": "hostel",
    "dorm": "hostel",
    "dorms": "hostel",
    "housing": "hostel",
    
    "start": "start",
    "starts": "start",
    "begin": "start",
    "begins": "start",
    "commence": "start",
    "commences": "start",
    "resume": "start",
    "resumes": "start",
    
    "close": "close",
    "closes": "close",
    "end": "close",
    "ends": "close",
    "deadline": "close",
    "deadlines": "close",
    "stop": "close",
    
    "location": "location",
    "address": "location",
    "where": "location",
    "place": "location",
    "situated": "location",
    "located": "location",
    
    "contact": "contact",
    "phone": "contact",
    "call": "contact",
    "email": "contact",
    "reach": "contact",
    "number": "contact",
    "tel": "contact",
    
    "help": "help",
    "complain": "help",
    "complaints": "help",
    "support": "help",
    "issue": "help",
    "issues": "help",
    "problem": "help",
    "problems": "help",
    "trouble": "help",
    "advisor": "help",
    
    "exam": "exam",
    "exams": "exam",
    "examination": "exam",
    "examinations": "exam",
    "test": "exam",
    "tests": "exam",
    
    "timetable": "timetable",
    "schedule": "timetable",
    "calender": "timetable",
    "calendar": "timetable",
    
    "defer": "defer",
    "deferment": "defer",
    "deferring": "defer",
    "postpone": "defer",
    
    "change": "change",
    "swap": "change",
    "transfer": "change",
    "switch": "change"
}

STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "arent",
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by",
    "cant", "cannot", "could", "couldnt", "did", "didnt", "do", "does", "doesnt", "doing", "dont",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadnt", "has", "hasnt", "have",
    "havent", "having", "he", "hed", "hell", "hes", "her", "here", "heres", "hers", "herself", "him",
    "himself", "his", "how", "hows", "i", "id", "ill", "im", "ive", "if", "in", "into", "is", "isnt",
    "it", "its", "itself", "lets", "me", "more", "most", "mustnt", "my", "myself", "no", "nor", "not",
    "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out",
    "over", "own", "same", "shant", "she", "shed", "shell", "shes", "should", "shouldnt", "so",
    "some", "such", "than", "that", "thats", "the", "their", "theirs", "them", "themselves",
    "then", "there", "theres", "these", "they", "theyd", "theyll", "theyre", "theyve", "this",
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasnt", "we", "wed",
    "well", "were", "weve", "werent", "what", "whats", "when", "whens", "where", "wheres", "which",
    "while", "who", "whos", "whom", "why", "whys", "with", "wont", "would", "wouldnt", "you",
    "youd", "youll", "youre", "youve", "your", "yours", "yourself", "yourselves"
}

KNOWLEDGE_BASE = [
    # ==================== ADMISSIONS ====================
    {
        "id": "adm_requirements_cs",
        "category": "admissions",
        "question": "What are the requirements for Computer Science?",
        "keywords": ["computer science requirements", "requirements for computer science", "cs requirements", "study computer science"],
        "answer": """<b>🎓 COMPUTER SCIENCE ADMISSION REQUIREMENTS:</b><br><br>
• <b>Grade Requirement:</b> Minimum 50% in 12th grade (Senior Secondary School Certificate).<br>
• <b>Compulsory Subjects:</b> Credits in Mathematics and English Language are mandatory.<br>
• <b>JAMB/UTME Score:</b> Minimum score of 180 is required.<br>
• <b>Evaluations:</b> Candidates must pass the university's entrance examination and interview.""",
        "follow_ups": ["How do I apply?", "How much is the tuition?", "What courses are available in the Faculty of Science?"]
    },
    {
        "id": "adm_qualifications",
        "category": "admissions",
        "question": "Can I apply with my qualifications?",
        "keywords": ["qualifications", "apply with my qualifications", "waec neco a levels diploma", "admission qualifications"],
        "answer": """<b>📋 ADMISSION QUALIFICATIONS:</b><br><br>
• <b>WAEC/NECO:</b> Minimum of 5 credits including Mathematics & English Language.<br>
• <b>A-Level:</b> Minimum of 2 A-Level passes in relevant subjects.<br>
• <b>Diploma:</b> Minimum of an Upper Credit from a recognized institution.<br>
• <b>Transfer Students:</b> Minimum CGPA of 3.0 on a 5.0 scale from your current university.""",
        "follow_ups": ["How do I apply?", "What documents do I need?", "What are the requirements for Computer Science?"]
    },
    {
        "id": "adm_nursing",
        "category": "admissions",
        "question": "Do you offer Nursing?",
        "keywords": ["nursing", "b sc nursing", "nursing program", "study nursing"],
        "answer": """<b>🩺 B.SC NURSING PROGRAM:</b><br><br>
• <b>Availability:</b> Yes! We offer a Bachelor of Science (B.Sc) in Nursing.<br>
• <b>Duration:</b> 5 years.<br>
• <b>Clinical Training:</b> Practical experience is conducted at accredited teaching hospitals.<br>
• <b>Licensure:</b> The curriculum includes thorough preparation for professional licensure examinations.""",
        "follow_ups": ["What are the requirements for Computer Science?", "How much is the tuition?", "What courses are available in the Faculty of Science?"]
    },
    {
        "id": "adm_science_courses",
        "category": "admissions",
        "question": "What courses are available in the Faculty of Science?",
        "keywords": ["faculty of science", "science courses", "science departments", "science programs"],
        "answer": """<b>🔬 FACULTY OF SCIENCE DEPARTMENTS:</b><br><br>
We offer the following undergraduate programs in the Faculty of Science:<br><br>
• Computer Science & Software Engineering<br>
• Cyber Security & Information Technology<br>
• Data Science & Statistics<br>
• Mathematics & Physics<br>
• Chemistry & Biochemistry<br>
• Biology, Microbiology, & Biotechnology<br>
• B.Sc Nursing""",
        "follow_ups": ["What are the requirements for Computer Science?", "Do you offer Nursing?", "How much is the tuition?"]
    },
    {
        "id": "adm_apply",
        "category": "admissions",
        "question": "How do I apply?",
        "keywords": ["how do i apply", "application process", "apply steps", "how to register", "admission process"],
        "answer": """<b>📝 APPLICATION PROCESS STEPS:</b><br><br>
1. <b>Visit website:</b> Go to our admissions portal (admissions.university.edu).<br>
2. <b>Create account:</b> Sign up using a valid email address and phone number.<br>
3. <b>Fill form:</b> Complete the online application profile and select your course.<br>
4. <b>Upload documents:</b> Upload scanned copies of required credentials.<br>
5. <b>Application fee:</b> Pay the non-refundable fee of <b>₦5,000</b> online.<br>
6. <b>Submit:</b> Finalize your application and print the confirmation page.""",
        "follow_ups": ["What documents do I need?", "When does admission close?", "What are the requirements for Computer Science?"]
    },
    {
        "id": "adm_documents",
        "category": "admissions",
        "question": "What documents do I need?",
        "keywords": ["documents needed", "required documents", "credentials to upload", "application documents"],
        "answer": """<b>📁 REQUIRED APPLICATION DOCUMENTS:</b><br><br>
Please upload clear, scanned copies of the following documents during application:<br>
• Official academic transcripts (for transfer or direct-entry students).<br>
• Government-issued ID proof (Birth certificate, National ID, or Passport).<br>
• Recent passport photograph (white background).<br>
• Two letters of recommendation (academic/professional).<br>
• Statement of Purpose explaining your academic goals.<br>
• WAEC, NECO, or equivalent High School certificate.<br>
• JAMB/UTME result slip (if applicable).""",
        "follow_ups": ["How do I apply?", "When does admission close?", "What are the requirements for Computer Science?"]
    },
    {
        "id": "adm_deadline",
        "category": "admissions",
        "question": "When does admission close?",
        "keywords": ["admission close", "application deadline", "deadlines", "last date to apply", "when is admission closing"],
        "answer": """<b>📅 APPLICATION DEADLINES (2026):</b><br><br>
• <b>Early Admission:</b> Closes on March 31, 2026.<br>
• <b>Regular Admission:</b> Closes on June 30, 2026.<br>
• <b>Late Admission:</b> Closes on July 15, 2026 (subject to vacancy and late fee).""",
        "follow_ups": ["How do I apply?", "What are the requirements for Computer Science?", "How much is the tuition?"]
    },
    {
        "id": "adm_tuition_fees",
        "category": "admissions",
        "question": "How much is the tuition?",
        "keywords": ["tuition fees", "school fees", "how much is tuition", "admission tuition", "tuition cost"],
        "answer": """<b>💰 TUITION FEES SUMMARY (PER ANNUM):</b><br><br>
• <b>General Undergraduate Range:</b> ₦700,000 - ₦1,500,000<br>
• <b>Engineering Courses:</b> ₦1,200,000 - ₦1,400,000<br>
• <b>Science Courses:</b> ₦700,000 - ₦900,000<br>
• <b>Business Courses:</b> ₦600,000 - ₦720,000<br>
• <b>Nursing Program:</b> ₦1,200,000<br><br>
<i>Note: Tuition fees can be paid in installments. Meritorious scholarships are also available.</i>""",
        "follow_ups": ["What are the acceptance fees?", "What are the fees for science courses?", "What other fees/charges are there?"]
    },
    {
        "id": "adm_acceptance_fees",
        "category": "admissions",
        "question": "What are the acceptance fees?",
        "keywords": ["acceptance fee", "acceptance fees", "how much is acceptance fee", "admission acceptance fee"],
        "answer": """<b>💳 ACCEPTANCE FEE INFORMATION:</b><br><br>
• <b>Fee Amount:</b> ₦100,000 (one-time, non-refundable).<br>
• <b>Payment Deadline:</b> Must be paid within 2 weeks of receiving the provisional offer of admission.<br>
• <b>Purpose:</b> Secures your admission slot before final registration.""",
        "follow_ups": ["How do I apply?", "How much is the tuition?", "What are the payment procedures?"]
    },

    # ==================== GENERAL INFO ====================
    {
        "id": "gen_location",
        "category": "general_info",
        "question": "Where is the campus location?",
        "keywords": ["location", "campus location", "where is the university", "university address", "direction"],
        "answer": """<b>📍 CAMPUS ADDRESS & LOCATION:</b><br><br>
123 University Avenue,<br>
Academic City, AC 12345,<br>
Nigeria.<br><br>
The campus is easily accessible via public transit and has designated student parking facilities.""",
        "follow_ups": ["How can I contact the university?", "Where is the admissions office?", "What are the office hours?"]
    },
    {
        "id": "gen_faculties",
        "category": "general_info",
        "question": "What faculties and departments do you have?",
        "keywords": ["faculties", "departments", "academic faculties", "list of departments"],
        "answer": """<b>🏛️ UNIVERSITY FACULTIES & DEPARTMENTS:</b><br><br>
• <b>Faculty of Science:</b> Computer Science, IT, Cyber Security, Software Engineering, Data Science, Math, Physics, Chemistry, Biology, Biotech, Statistics, Nursing.<br>
• <b>Faculty of Engineering:</b> Computer, Electrical, Mechanical, Civil, Chemical Engineering.<br>
• <b>Faculty of Business:</b> Accounting, Economics, Business Administration, Marketing, Finance, Human Resources.<br>
• <b>Faculty of Arts & Social Sciences:</b> English, History, Political Science, Sociology, Psychology, Mass Communication.""",
        "follow_ups": ["Where is the admissions office?", "How can I contact the university?", "When does the semester start?"]
    },
    {
        "id": "gen_admissions_office",
        "category": "general_info",
        "question": "Where is the admissions office?",
        "keywords": ["admissions office location", "where is admissions office", "admissions office block"],
        "answer": """<b>🏢 ADMISSIONS OFFICE LOCATION:</b><br><br>
• <b>Location:</b> Main Administration Building, Block A, Ground Floor.<br>
• <b>Office Hours:</b> Monday to Friday, 9:00 AM - 5:00 PM.<br>
• <b>Walk-ins:</b> Welcome during office hours. No prior appointment is required.""",
        "follow_ups": ["How can I contact the university?", "What are the office hours?", "How do I apply?"]
    },
    {
        "id": "gen_contact",
        "category": "general_info",
        "question": "How can I contact the university?",
        "keywords": ["contact university", "phone number", "email address", "admissions contact", "registrar contact"],
        "answer": """<b>📞 UNIVERSITY CONTACT DIRECTORY:</b><br><br>
• <b>Main Admin Office:</b> +1 (555) 123-4567 | info@university.edu<br>
• <b>Admissions Office:</b> +1 (555) 987-6543 | admissions@university.edu<br>
• <b>Registrar's Office:</b> +1 (555) 555-0188 | registrar@university.edu<br>
• <b>Location:</b> Block A, Main Building, Ground Floor (Admissions) & 1st Floor (Registrar).""",
        "follow_ups": ["Where is the admissions office?", "What are the office hours?", "I need help with a problem / office contacts"]
    },
    {
        "id": "gen_office_hours",
        "category": "general_info",
        "question": "What are the office hours?",
        "keywords": ["office hours", "opening hours", "when is office open", "work hours", "working hours"],
        "answer": """<b>🕒 OFFICE WORK HOURS:</b><br><br>
• <b>Monday - Friday:</b> 9:00 AM - 5:00 PM<br>
• <b>Saturday:</b> 10:00 AM - 2:00 PM (Admissions & Registrar's desk only)<br>
• <b>Sunday:</b> Closed<br>
• <b>Public Holidays:</b> Closed""",
        "follow_ups": ["How can I contact the university?", "Where is the admissions office?", "When does the semester start?"]
    },
    {
        "id": "gen_semester_start",
        "category": "general_info",
        "question": "When does the semester start?",
        "keywords": ["semester start", "when is resumption", "school resumes", "resumption date", "calendar start"],
        "answer": """<b>📅 SEMESTER START DATES (2026/2027):</b><br><br>
• <b>First Semester:</b> Resumes on August 1, 2026.<br>
• <b>Second Semester:</b> Resumes on January 15, 2027.<br>
• <b>Registration Period:</b> March 1 - June 30, 2026.""",
        "follow_ups": ["When are the exams?", "When does course registration end?", "When does admission close?"]
    },
    {
        "id": "gen_exams",
        "category": "general_info",
        "question": "When are exams?",
        "keywords": ["exam date", "when are exams", "examination period", "exam calendar"],
        "answer": """<b>📝 ACADEMIC EXAMINATIONS CALENDAR:</b><br><br>
• <b>First Semester Exams:</b> December 1 - December 15, 2026.<br>
• <b>Second Semester Exams:</b> May 15 - May 30, 2027.<br>
• <b>Timetable Release:</b> Timetable is published on the portal 2 weeks before exams start.""",
        "follow_ups": ["When does the semester start?", "When is the exam timetable released?", "When are results released?"]
    },

    # ==================== STUDENT FAQS ====================
    {
        "id": "faq_registration_deadline",
        "category": "student_faqs",
        "question": "When does course registration end?",
        "keywords": ["course registration end", "registration deadline", "when is registration closing", "registration date"],
        "answer": """<b>📚 COURSE REGISTRATION DEADLINES:</b><br><br>
• <b>Regular Registration:</b> Closes on June 30, 2026.<br>
• <b>Late Registration:</b> July 1 - July 15, 2026 (a late penalty fee of ₦50,000 applies).<br>
• <b>Note:</b> Registration portal opens on March 1, 2026.""",
        "follow_ups": ["What happens if I miss course registration?", "Can I change my course?", "When does the semester start?"]
    },
    {
        "id": "faq_miss_registration",
        "category": "student_faqs",
        "question": "What happens if I miss course registration?",
        "keywords": ["miss registration", "missed course registration", "late registration penalty"],
        "answer": """<b>⚠️ MISSED REGISTRATION CONSEQUNCES:</b><br><br>
• <b>Late Window:</b> If you miss regular registration (by June 30), you can register during the late window (July 1-15) with a late registration fee of <b>₦50,000</b>.<br>
• <b>After July 15:</b> The portal closes completely. No registration is allowed for the semester. You will have to wait for the next semester.<br>
• <b>Support:</b> Contact the Registrar's office (registrar@university.edu) for special medical/compassionate cases.""",
        "follow_ups": ["When does course registration end?", "Can I change my course?", "Can I defer my admission?"]
    },
    {
        "id": "faq_change_course",
        "category": "student_faqs",
        "question": "Can I change my course?",
        "keywords": ["change course", "course transfer", "switch department", "change major"],
        "answer": """<b>🔄 COURSE / DEPARTMENT CHANGE POLICY:</b><br><br>
• <b>Time Window:</b> Permitted only within the first 2 weeks of the academic semester.<br>
• <b>Approvals:</b> Requires written approval from both the sending and receiving Head of Department (HOD).<br>
• <b>Criteria:</b> You must meet the admission requirements of the new department and there must be available capacity.<br>
• <b>Fees:</b> A department change processing fee of <b>₦10,000</b> applies.""",
        "follow_ups": ["When does course registration end?", "What are the requirements for Computer Science?", "Can I defer my admission?"]
    },
    {
        "id": "faq_apply_accommodation",
        "category": "student_faqs",
        "question": "How do I apply for accommodation?",
        "keywords": ["apply for accommodation", "apply hostel", "hostel application", "book room", "student housing"],
        "answer": """<b>🏠 HOSTEL ACCOMMODATION APPLICATION:</b><br><br>
To apply for a room in the university hostels:<br>
1. Log in to the <b>Student Portal</b>.<br>
2. Navigate to the <b>Accommodation</b> tab.<br>
3. Fill the online room request form.<br>
4. Generate the payment invoice and make the hostel payment.<br>
5. Upon verification, your room allocation slip will be generated automatically on the portal.""",
        "follow_ups": ["How much is the hostel fee?", "What are the payment procedures?", "When does course registration end?"]
    },
    {
        "id": "faq_hostel_fee",
        "category": "student_faqs",
        "question": "How much is the hostel fee?",
        "keywords": ["hostel fee", "hostel cost", "hostel fees", "accommodation cost", "room price"],
        "answer": """<b>💰 HOSTEL ACCOMMODATION FEES:</b><br><br>
• <b>Standard Room:</b> ₦500,000 / academic year (shared room with basic amenities).<br>
• <b>Executive Room:</b> ₦800,000 / academic year (private room, air-conditioned, en-suite bathroom).<br>
• <b>Application Window:</b> Opens May 1, 2026, and closes July 15, 2026.<br>
• <b>Note:</b> Fees are paid in full before room allocation is confirmed.""",
        "follow_ups": ["How do I apply for accommodation?", "What other fees/charges are there?", "What are the payment procedures?"]
    },
    {
        "id": "faq_defer_admission",
        "category": "student_faqs",
        "question": "Can I defer my admission?",
        "keywords": ["defer admission", "deferment", "postpone resumption", "defer my admission", "admission deferment"],
        "answer": """<b>📜 ADMISSION DEFERMENT POLICY:</b><br><br>
• <b>Eligibility:</b> Yes, students can defer their admission, primarily for medical, financial, or compassionate grounds.<br>
• <b>Process:</b> Apply before the semester starts. You must submit official medical reports or supporting documentation to the Registrar.<br>
• <b>Duration:</b> Deferment is approved for 1 semester or 1 academic year maximum.<br>
• <b>Fees:</b> Fees paid are not refundable but will be credited to your account for when you resume.""",
        "follow_ups": ["Can I change my course?", "What happens if I miss course registration?", "When does course registration end?"]
    },
    {
        "id": "faq_exam_timetable",
        "category": "student_faqs",
        "question": "When is the exam timetable released?",
        "keywords": ["exam timetable", "exam schedule", "when is exam timetable released"],
        "answer": """<b>📅 EXAM TIMETABLE RELEASE:</b><br><br>
• <b>Release Date:</b> November 15, 2026 (for First Semester exams).<br>
• <b>Where to check:</b> Published on the student portal and pinned on department notice boards.<br>
• <b>Exam Period:</b> First semester exams run from December 1 to December 15, 2026.""",
        "follow_ups": ["When are exams?", "When are results released?", "When does the semester start?"]
    },
    {
        "id": "faq_results_release",
        "category": "student_faqs",
        "question": "When are results released?",
        "keywords": ["results release", "when are results out", "results date", "grade release"],
        "answer": """<b>🎓 SEMESTER RESULTS RELEASE:</b><br><br>
• <b>Release Date:</b> December 30, 2026 (for First Semester exams).<br>
• <b>How to Check:</b> Log in to the Student Portal, click on 'Grades/Results', and select the academic session.<br>
• <b>GPA:</b> Your Semester GPA and Cumulative GPA (CGPA) will be updated automatically.""",
        "follow_ups": ["When are exams?", "When is the exam timetable released?", "When does the semester start?"]
    },

    # ==================== FEES & PAYMENTS ====================
    {
        "id": "fee_cs",
        "category": "fees_payments",
        "question": "How much is the tuition for Computer Science?",
        "keywords": ["tuition for computer science", "computer science tuition", "cs tuition fees", "computer science school fees"],
        "answer": """<b>💻 COMPUTER SCIENCE TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦1,200,000</b> per academic year.<br>
• <b>Includes:</b> Lecture delivery, lab access, practical software licenses, and departmental library fees.<br>
• <b>Payment plans:</b> Eligible for installment payments (up to 3 installments).""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_it",
        "category": "fees_payments",
        "question": "How much is the tuition for Information Technology?",
        "keywords": ["tuition for information technology", "information technology tuition", "it tuition fee"],
        "answer": """<b>ℹ️ INFORMATION TECHNOLOGY TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦1,100,000</b> per academic year.<br>
• <b>Includes:</b> ICT services, networking labs, virtual desktop access, and lectures.""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_cyber",
        "category": "fees_payments",
        "question": "How much is the tuition for Cyber Security?",
        "keywords": ["tuition for cyber security", "cyber security tuition", "cyber security school fees"],
        "answer": """<b>🔒 CYBER SECURITY TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦1,300,000</b> per academic year.<br>
• <b>Includes:</b> Cybersecurity labs, penetration testing tools, licensing, and course tuition.""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_se",
        "category": "fees_payments",
        "question": "How much is the tuition for Software Engineering?",
        "keywords": ["tuition for software engineering", "software engineering tuition", "software engineering school fees"],
        "answer": """<b>⚙️ SOFTWARE ENGINEERING TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦1,400,000</b> per academic year.<br>
• <b>Includes:</b> Full coding bootcamps, project infrastructure, hosting credits, and course tuition.""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_datasci",
        "category": "fees_payments",
        "question": "How much is the tuition for Data Science?",
        "keywords": ["tuition for data science", "data science tuition", "data science school fees"],
        "answer": """<b>📊 DATA SCIENCE TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦1,500,000</b> per academic year.<br>
• <b>Includes:</b> Cloud computing access, big data clusters, Python/R lab licenses, and lectures.""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_nursing",
        "category": "fees_payments",
        "question": "How much is the tuition for Nursing?",
        "keywords": ["tuition for nursing", "nursing tuition", "nursing school fees", "nursing cost"],
        "answer": """<b>🩺 B.SC NURSING TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦1,200,000</b> per academic year.<br>
• <b>Includes:</b> Anatomy lab access, clinical materials, hospital ward placement insurances, and tutorials.""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "Do you offer Nursing?"]
    },
    {
        "id": "fee_accounting",
        "category": "fees_payments",
        "question": "How much is the tuition for Accounting?",
        "keywords": ["tuition for accounting", "accounting tuition", "accounting school fees"],
        "answer": """<b>📈 ACCOUNTING TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦700,000</b> per academic year.<br>
• <b>Includes:</b> Financial database tools (Sage/Quickbooks), professional seminar entries, and lectures.""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_economics",
        "category": "fees_payments",
        "question": "How much is the tuition for Economics?",
        "keywords": ["tuition for economics", "economics tuition", "economics school fees"],
        "answer": """<b>📉 ECONOMICS TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦680,000</b> per academic year.<br>
• <b>Includes:</b> Analytical software licenses (SPSS/Stata), research seminars, and lectures.""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_busadmin",
        "category": "fees_payments",
        "question": "How much is the tuition for Business Administration?",
        "keywords": ["tuition for business administration", "business administration tuition", "business school fees"],
        "answer": """<b>💼 BUSINESS ADMINISTRATION TUITION FEE:</b><br><br>
• <b>Tuition Fee:</b> <b>₦720,000</b> per academic year.<br>
• <b>Includes:</b> Business simulation packages, case studies, leadership modules, and lectures.""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_engineering_courses",
        "category": "fees_payments",
        "question": "How much is the tuition for engineering courses?",
        "keywords": ["engineering tuition fees", "engineering school fees", "cost of engineering"],
        "answer": """<b>⚙️ FACULTY OF ENGINEERING TUITION FEES (PER YEAR):</b><br><br>
• <b>Chemical Engineering:</b> ₦1,400,000<br>
• <b>Computer Engineering:</b> ₦1,350,000<br>
• <b>Electrical Engineering:</b> ₦1,300,000<br>
• <b>Mechanical Engineering:</b> ₦1,250,000<br>
• <b>Civil Engineering:</b> ₦1,200,000""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_science_courses",
        "category": "fees_payments",
        "question": "What are the fees for science courses?",
        "keywords": ["science tuition fees", "science school fees", "cost of science courses"],
        "answer": """<b>🔬 FACULTY OF SCIENCE TUITION FEES (PER YEAR):</b><br><br>
• <b>Data Science:</b> ₦1,500,000<br>
• <b>Software Engineering:</b> ₦1,400,000<br>
• <b>Cyber Security:</b> ₦1,300,000<br>
• <b>Computer Science:</b> ₦1,200,000<br>
• <b>Information Technology:</b> ₦1,100,000<br>
• <b>Biotechnology:</b> ₦1,000,000<br>
• <b>Nursing:</b> ₦1,200,000<br>
• <b>Biochemistry:</b> ₦900,000<br>
• <b>Microbiology:</b> ₦850,000<br>
• <b>Mathematics:</b> ₦800,000<br>
• <b>Physics / Chemistry / Biology:</b> ₦700,000""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_postgraduate",
        "category": "fees_payments",
        "question": "What are the postgraduate/MBA fees?",
        "keywords": ["postgraduate fees", "msc tuition", "mba fees", "postgraduate tuition"],
        "answer": """<b>🎓 POSTGRADUATE TUITION FEES (PER YEAR):</b><br><br>
• <b>MBA (Master of Business Administration):</b> ₦1,500,000<br>
• <b>M.Sc Programs (Faculty of Science/Engineering):</b> ₦1,350,000 - ₦1,500,000<br>
• <b>M.Com (Master of Commerce):</b> ₦850,000<br>
• <b>Postgraduate Diploma (PGD):</b> ₦600,000""",
        "follow_ups": ["What are the payment procedures?", "What are the payment deadlines and options?", "How much is the tuition?"]
    },
    {
        "id": "fee_other_charges",
        "category": "fees_payments",
        "question": "What other fees/charges are there?",
        "keywords": ["other charges", "additional fees", "library fee sports fee ict fee", "extra costs"],
        "answer": """<b>📋 MANDATORY ANNUAL ANCILLARY CHARGES:</b><br><br>
Beyond tuition, the following fees apply annually:<br>
• <b>Library Fee:</b> ₦50,000<br>
• <b>Medical Insurance:</b> ₦40,000<br>
• <b>Sports Fee:</b> ₦30,000<br>
• <b>ICT Fee:</b> ₦25,000<br><br>
<i>Note: Hostel Accommodation is optional and ranges from ₦500,000 to ₦800,000/year depending on room selection.</i>""",
        "follow_ups": ["How much is the hostel fee?", "What are the payment procedures?", "What are the payment deadlines and options?"]
    },
    {
        "id": "fee_procedures",
        "category": "fees_payments",
        "question": "What are the payment procedures?",
        "keywords": ["payment procedure", "how to pay school fees", "generate invoice", "make payments"],
        "answer": """<b>💳 STEP-BY-STEP PAYMENT PROCEDURES:</b><br><br>
All official fee payments are processed securely online:<br>
1. <b>Invoice Generation:</b> Log in to the Student Portal and click on the 'Fees' module. Generate a payment invoice for the current session.<br>
2. <b>Payment Channels:</b><br>
   • <b>Online:</b> Click 'Pay Online' and use a Debit card via Flutterwave/Paystack.<br>
   • <b>Bank Branch:</b> Print the invoice and present the RRR at any commercial bank.<br>
3. <b>Confirmation:</b> Upload the payment receipt/teller on the portal.<br>
4. <b>Verification:</b> The Bursary clears and verifies the receipt within 24-48 hours. A digital receipt will appear on your dashboard.""",
        "follow_ups": ["What are the payment deadlines and options?", "How much is the tuition?", "What are the acceptance fees?"]
    },
    {
        "id": "fee_deadlines",
        "category": "fees_payments",
        "question": "What are the payment deadlines and options?",
        "keywords": ["payment deadline", "fee deadline", "installment payments", "discount for full payment"],
        "answer": """<b>📅 FEE PAYMENT DEADLINES & PLANS:</b><br><br>
• <b>Payment Deadlines:</b><br>
  - <b>1st Installment (60%):</b> Due by August 1, 2026 (Resumption).<br>
  - <b>2nd Installment (20%):</b> Due by October 15, 2026.<br>
  - <b>3rd Installment (20%):</b> Due by January 15, 2027.<br>
• <b>Late Payment Penalty:</b> ₦50,000 applies to payments made after deadlines.<br>
• <b>Payment Incentives:</b> 5% discount on tuition is granted for full upfront payments.<br>
• <b>Scholarships:</b> Merit and need-based financial aid are available through Student Affairs.""",
        "follow_ups": ["What are the payment procedures?", "How much is the tuition?", "What other fees/charges are there?"]
    },

    # ==================== POLICIES ====================
    {
        "id": "pol_attendance",
        "category": "policies",
        "question": "What is the attendance policy?",
        "keywords": ["attendance policy", "attendance percentage", "attendance requirement", "biometric attendance"],
        "answer": """<b>📋 ATTENDANCE REGULATIONS:</b><br><br>
• <b>Minimum Requirement:</b> Students must achieve a minimum of <b>75% attendance</b> in each course to be eligible to sit for exams.<br>
• <b>Monitoring:</b> Attendance is tracked electronically using biometrics in lecture halls.<br>
• <b>Exclusions:</b> Students falling below 75% will be automatically barred from writing exams.<br>
• <b>Absences:</b> Up to 10 days of absence per semester are tolerated. Medical leave must be certified by the University Health Centre within 48 hours.""",
        "follow_ups": ["What are the examination rules?", "What is the dress code?", "What are the graduation requirements?"]
    },
    {
        "id": "pol_exam_rules",
        "category": "policies",
        "question": "What are the examination rules?",
        "keywords": ["examination rules", "exam rules", "exam misconduct", "cheating rules"],
        "answer": """<b>📝 EXAMINATION CODE OF CONDUCT:</b><br><br>
• <b>Arrival:</b> Arrive at the exam venue at least 30 minutes before the scheduled start.<br>
• <b>ID Card:</b> A valid Student ID Card is mandatory for entry.<br>
• <b>Prohibited Items:</b> Mobile phones, smartwatches, and unauthorized papers are strictly prohibited. Finding any of these constitutes malpractice.<br>
• <b>Duration:</b> Standard exams are 2-3 hours long.<br>
• <b>Malpractice:</b> Any form of cheating or speaking during the exam leads to automatic failure, immediate suspension, and escalation to the disciplinary committee.""",
        "follow_ups": ["What is the attendance policy?", "What is the dress code?", "What are the graduation requirements?"]
    },
    {
        "id": "pol_dress_code",
        "category": "policies",
        "question": "What is the dress code?",
        "keywords": ["dress code", "rules on dressing", "formal attire", "lab coats"],
        "answer": """<b>👔 UNIVERSITY DRESS CODE:</b><br><br>
• <b>General Rule:</b> Students are required to dress formally or semi-formally during lecture hours (Monday - Friday, 8 AM - 5 PM).<br>
• <b>Specialized Gear:</b> Lab coats are compulsory for all students in science laboratories.<br>
• <b>Library Dress:</b> Sleeveless tops, short skirts, and slippers are not permitted in the library.<br>
• <b>Identity Card:</b> The student ID card must be worn visibly around the neck at all times on campus.<br>
• <b>Weekends:</b> Decent casual wear is permitted on weekends and after 5 PM.""",
        "follow_ups": ["What is the attendance policy?", "What are the examination rules?", "What is the university code of conduct?"]
    },
    {
        "id": "pol_graduation",
        "category": "policies",
        "question": "What are the graduation requirements?",
        "keywords": ["graduation requirements", "requirements to graduate", "minimum cgpa", "siwes internship"],
        "answer": """<b>🎓 GRADUATION REQUIREMENTS:</b><br><br>
To graduate and receive your degree, you must:<br>
• Complete and pass all compulsory core and elective course credits.<br>
• Achieve a minimum Cumulative GPA (CGPA) of <b>2.50</b> (Second Class Lower division).<br>
• Successfully complete and pass your final year departmental project.<br>
• Successfully complete SIWES / Student Internship placement (for science/engineering).<br>
• Have a clean disciplinary record and no outstanding financial balances or library fines.""",
        "follow_ups": ["What is the attendance policy?", "What is the university code of conduct?", "What are the examination rules?"]
    },
    {
        "id": "pol_conduct",
        "category": "policies",
        "question": "What is the university code of conduct?",
        "keywords": ["code of conduct", "university rules", "regulations", "harassment bullying"],
        "answer": """<b>📜 STUDENT CODE OF CONDUCT:</b><br><br>
• <b>Respect:</b> Treat all academic staff, administrative staff, and fellow students with dignity.<br>
• <b>Integrity:</b> Plagiarism, exam malpractice, and falsification of records are strictly banned.<br>
• <b>Safety:</b> Harassment, cultism, bullying, and drug abuse carry a penalty of immediate expulsion.<br>
• <b>Property:</b> Do not deface or damage university buildings, library resources, or equipment.<br>
• <b>Penalties:</b> Violations are investigated by the Student Disciplinary Committee and can result in suspensions or expulsions.""",
        "follow_ups": ["What is the attendance policy?", "What is the dress code?", "What are the examination rules?"]
    },

    # ==================== CONTACT ====================
    {
        "id": "con_help_problem",
        "category": "contact",
        "question": "I need help with a problem / office contacts",
        "keywords": ["need help with a problem", "problem help", "office locations", "admin contacts"],
        "answer": """<b>🏛️ SUPPORT OFFICE DIRECTORY:</b><br><br>
• <b>Applications & Offers:</b> Admissions Office (Block A, Ground Floor | admissions@university.edu | +1 (555) 987-6543)<br>
• <b>Registration, Transcripts & Graduation:</b> Registrar's Office (Block A, 1st Floor | registrar@university.edu | +1 (555) 555-0188)<br>
• <b>Payments & Refunds:</b> Bursary/Finance Office (Block C, Ground Floor | finance@university.edu | +1 (555) 555-0199)<br>
• <b>Accommodation & Welfare:</b> Student Affairs Office (Block B, 2nd Floor | studentaffairs@university.edu | +1 (555) 555-0177)<br>
• <b>Portal Login & IT Issues:</b> ICT Support Centre (Block B, 2nd Floor | ict@university.edu | +1 (555) 555-0199)""",
        "follow_ups": ["How can I contact the university?", "What is the escalation process?", "Where is the admissions office?"]
    },
    {
        "id": "con_escalation",
        "category": "contact",
        "question": "What is the escalation process?",
        "keywords": ["escalation process", "how to lodge a complaint", "appeal a decision", "complain escalation"],
        "answer": """<b>🔴 OFFICIAL COMPLAINT ESCALATION PROCESS:</b><br><br>
If you have an issue that was not resolved at the front desk, please follow this hierarchy:<br><br>
1. <b>Level 1 (Front Desk):</b> Lodge the complaint with the relevant office (e.g. Bursary, Admissions, ICT) via phone or email.<br>
2. <b>Level 2 (Head of Department):</b> If unresolved in 3 working days, submit a written appeal to your department HOD.<br>
3. <b>Level 3 (Dean of Faculty):</b> If still unresolved after 5 working days, escalate the issue to the Dean of your Faculty.<br>
4. <b>Final Appeal (Registrar/Vice-Chancellor):</b> For critical or disciplinary issues, submit a formal petition to the Registrar's Office.""",
        "follow_ups": ["I need help with a problem / office contacts", "How can I contact the university?", "What are the office hours?"]
    }
]
