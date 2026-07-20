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
    },

    # ==================== NEW TOPICS ====================
    {
        "id": "faq_scholarships_bursaries",
        "category": "fees_payments",
        "question": "Are there scholarships or bursaries available?",
        "keywords": ["scholarship", "bursary", "financial aid", "merit scholarship", "need based aid"],
        "answer": """<b>🏆 SCHOLARSHIPS & BURSARIES:</b><br><br>
The university offers several financial support options for deserving students:<br><br>
• <b>Vice-Chancellor's Merit Scholarship:</b> Awarded annually to the top 5 students per faculty based on CGPA (minimum 4.50/5.00). Covers up to 50% of tuition.<br>
• <b>Need-Based Bursary:</b> Available to students from low-income households. Applicants must submit a means test form and supporting documents to Student Affairs.<br>
• <b>Departmental Excellence Awards:</b> Each department awards a one-time grant of ₦100,000 to the best-graduating student annually.<br>
• <b>External/Government Scholarships:</b> Students are encouraged to apply for TETFUND, State Government, and other external scholarship bodies. The Student Affairs Office maintains an updated list of open scholarship applications.<br><br>
<b>How to Apply:</b> Visit the Student Affairs Office (Block B, 2nd Floor) or download the scholarship form from the student portal under 'Financial Aid'.<br>
<i>Note: Scholarship slots are limited and competitive. Applications are reviewed each new academic session.</i>""",
        "follow_ups": ["What are the payment deadlines and options?", "What are the payment procedures?", "What other fees/charges are there?"]
    },
    {
        "id": "faq_siwes_internship",
        "category": "student_faqs",
        "question": "How does the SIWES / internship program work?",
        "keywords": ["siwes", "internship", "industrial training", "it placement", "student work experience"],
        "answer": """<b>🏭 SIWES / INDUSTRIAL TRAINING (IT) PROGRAM:</b><br><br>
The Students' Industrial Work Experience Scheme (SIWES) is a mandatory component for Science and Engineering students:<br><br>
• <b>Who It Applies To:</b> All students in Science, Engineering, and Technology (SET) programs are required to complete SIWES.<br>
• <b>Duration:</b> Typically 6 months (for 5-year programs) or 3 months (for 4-year programs), usually in the 3rd or 4th year.<br>
• <b>Process:</b><br>
  1. Register for SIWES through the Industrial Training Coordinating Unit (ITCU) before the semester deadline.<br>
  2. Secure an approved placement with a recognized company or government agency.<br>
  3. Collect your SIWES letter of introduction from the ITCU.<br>
  4. Maintain a daily logbook, which must be signed by your industry supervisor.<br>
  5. Submit your completed logbook and a technical report to the ITCU at the end of the placement.<br>
• <b>Assessment:</b> Students are graded on their logbook, employer's evaluation report, and a final presentation to their department.<br>
• <b>Contact:</b> ITCU Office — Block D, Ground Floor | itcu@university.edu | +1 (555) 555-0201""",
        "follow_ups": ["What are the graduation requirements?", "What is the attendance policy?", "I need help with a problem / office contacts"]
    },
    {
        "id": "faq_health_services",
        "category": "student_faqs",
        "question": "What health services are available on campus?",
        "keywords": ["health services", "clinic", "university clinic", "sick bay", "medical centre", "campus health"],
        "answer": """<b>🏥 STUDENT HEALTH SERVICES / UNIVERSITY CLINIC:</b><br><br>
The University Health Centre provides basic and specialist medical care to all registered students:<br><br>
• <b>Location:</b> Health Centre Building, behind the Sports Complex.<br>
• <b>Operating Hours:</b> Monday – Friday: 8:00 AM – 8:00 PM | Saturday: 9:00 AM – 2:00 PM | 24-hour emergency line available.<br>
• <b>Services Offered:</b><br>
  – General consultations and outpatient treatment.<br>
  – Dispensary (free basic medications for enrolled students).<br>
  – Family planning and sexual health advisory.<br>
  – Mental health counselling and psychological support.<br>
  – Referral letters to teaching hospitals for specialist care.<br>
• <b>Medical Insurance:</b> All students pay a compulsory Medical Insurance levy of ₦40,000/year which covers basic consultations and outpatient medication at the Health Centre.<br>
• <b>Emergency:</b> Call the 24-hour emergency line at +1 (555) 555-0911 for urgent medical situations on campus.<br>
• <b>Sick Leave:</b> Medical certificates from the University Health Centre are the only accepted documents for academic absenteeism excusals.""",
        "follow_ups": ["What other fees/charges are there?", "What is the attendance policy?", "I need help with a problem / office contacts"]
    },
    {
        "id": "faq_lost_id_card",
        "category": "student_faqs",
        "question": "What do I do if I lose my student ID card?",
        "keywords": ["lost id card", "missing student card", "replace id card", "id card replacement", "lost student card"],
        "answer": """<b>🪪 LOST / DAMAGED STUDENT ID CARD PROCEDURE:</b><br><br>
If your student ID card is lost, stolen, or damaged, follow these steps immediately:<br><br>
1. <b>Report the Loss:</b> Visit the Campus Security Office (Main Gate) and complete a Loss Report Form. Retain a copy of the stamped form.<br>
2. <b>Visit the ICT/Student Records Unit:</b> Proceed to the ICT Support Centre (Block B, 2nd Floor) with the following:<br>
   – Stamped Security Loss Report Form<br>
   – A completed ID Card Replacement Request Form (available at the front desk)<br>
   – Proof of payment of the ID replacement fee<br>
3. <b>Replacement Fee:</b> ₦5,000 (non-refundable). Payment is made via the student portal under 'Miscellaneous Payments'.<br>
4. <b>Processing Time:</b> 3 – 5 working days.<br>
5. <b>Temporary Pass:</b> A temporary campus access pass will be issued to you while your new card is being processed.<br><br>
<i>⚠️ Note: Your student ID card must be worn visibly on campus at all times. Operating without an ID card after 5 working days of loss reporting is a disciplinary offense.</i>""",
        "follow_ups": ["What is the dress code?", "What are the examination rules?", "I need help with a problem / office contacts"]
    },
    {
        "id": "adm_requirements_cyber_compeng",
        "category": "admissions",
        "question": "What are the admission requirements for Cybersecurity or Computer Engineering?",
        "keywords": ["cybersecurity requirements", "computer engineering requirements", "cyber security admission", "compeng admission"],
        "answer": """<b>🔒 CYBERSECURITY & COMPUTER ENGINEERING ADMISSION REQUIREMENTS:</b><br><br>
<b>Cybersecurity (Faculty of Science):</b><br>
• <b>O'Level:</b> Minimum 5 credits at WAEC/NECO/NABTEB — must include Mathematics, English Language, and Physics.<br>
• <b>JAMB/UTME Score:</b> Minimum cut-off score of 200.<br>
• <b>JAMB Subject Combination:</b> Mathematics, Physics, Chemistry/Biology/Economics/Geography.<br>
• <b>Post-UTME:</b> Candidates must pass the university's aptitude test and technical interview.<br><br>
<b>Computer Engineering (Faculty of Engineering):</b><br>
• <b>O'Level:</b> Minimum 5 credits — must include Mathematics, English Language, Physics, and Chemistry.<br>
• <b>JAMB/UTME Score:</b> Minimum cut-off score of 200.<br>
• <b>JAMB Subject Combination:</b> Mathematics, Physics, Chemistry.<br>
• <b>Direct Entry:</b> ND (Upper Credit) or A-Level passes in Mathematics and Physics are accepted for 200-level entry.<br>
• <b>Post-UTME:</b> Candidates must pass the university's entrance examination.<br><br>
<i>Both programs are accredited by NUC and have a duration of 4–5 years.</i>""",
        "follow_ups": ["What are the requirements for Computer Science?", "How do I apply?", "What are the fees for science courses?"]
    },
    {
        "id": "adm_mba_postgraduate",
        "category": "admissions",
        "question": "What are the MBA or postgraduate admission requirements?",
        "keywords": ["mba admission", "postgraduate admission", "masters requirements", "msc admission", "pgd admission"],
        "answer": """<b>🎓 MBA / POSTGRADUATE ADMISSION REQUIREMENTS:</b><br><br>
<b>General Requirements (All Postgraduate Programs):</b><br>
• A first degree (B.Sc, B.Eng, B.A, etc.) from a recognized university with a minimum CGPA of <b>2.50/5.00</b> (Second Class Lower).<br>
• Five O'Level credits (WAEC/NECO) including Mathematics and English Language.<br>
• NYSC Discharge Certificate or Exemption Letter.<br>
• Two academic/professional reference letters.<br><br>
<b>MBA Specific Requirements:</b><br>
• A bachelor's degree in any discipline (Second Class Lower minimum).<br>
• Minimum of 2 years relevant post-graduation work experience.<br>
• A statement of purpose (SOP) detailing your leadership goals and career ambitions.<br>
• Valid GMAT/GRE score (recommended, not strictly mandatory).<br><br>
<b>M.Sc Programs (Science/Engineering):</b><br>
• First degree in a relevant discipline with Second Class Lower (2.50 CGPA) minimum.<br>
• A completed research proposal submitted with the application.<br><br>
<b>How to Apply:</b> Submit your application online via the Postgraduate School portal at pg.university.edu. Application fee: ₦10,000.<br>
<b>Contact:</b> School of Postgraduate Studies — Block A, 3rd Floor | pg@university.edu""",
        "follow_ups": ["What are the postgraduate/MBA fees?", "How do I apply?", "What documents do I need?"]
    },
    {
        "id": "faq_portal_login_issues",
        "category": "student_faqs",
        "question": "I can't log in to the student portal — what do I do?",
        "keywords": ["portal login issues", "student portal login", "cant login portal", "portal password reset", "portal not working"],
        "answer": """<b>💻 STUDENT PORTAL LOGIN TROUBLESHOOTING:</b><br><br>
If you are unable to log in to the student portal, try the following steps:<br><br>
1. <b>Check Credentials:</b> Your default username is your <b>Student Matriculation Number</b> and your default password is your <b>date of birth</b> in DDMMYYYY format (e.g., 15091999).<br>
2. <b>Reset Password:</b> Click <b>'Forgot Password'</b> on the login page. A reset link will be sent to your registered university email address.<br>
3. <b>Clear Browser Cache:</b> Try clearing your browser cache and cookies, or use a different browser (Chrome or Firefox recommended).<br>
4. <b>Check Internet Connection:</b> Ensure you have a stable internet connection. The portal is also accessible on the campus Wi-Fi network.<br>
5. <b>Account Not Activated:</b> New students must activate their portal account using the activation code on their admission letter. Visit the ICT Centre if you do not have an activation code.<br>
6. <b>Still Unable to Login?</b> Contact the ICT Support Centre directly:<br>
   – Walk-in: Block B, 2nd Floor<br>
   – Email: ict@university.edu<br>
   – Phone: +1 (555) 555-0199<br>
   – Hours: Monday – Friday, 9:00 AM – 5:00 PM""",
        "follow_ups": ["I need help with a problem / office contacts", "How can I contact the university?", "What are the office hours?"]
    },
    {
        "id": "faq_wifi_campus_internet",
        "category": "student_faqs",
        "question": "How do I connect to campus Wi-Fi?",
        "keywords": ["wifi", "campus internet", "campus wifi", "connect internet", "wi-fi access"],
        "answer": """<b>📶 CAMPUS WI-FI / INTERNET ACCESS:</b><br><br>
The university provides free high-speed Wi-Fi throughout all academic, residential, and administrative buildings:<br><br>
• <b>Network Name (SSID):</b> <b>UniConnect_Student</b><br>
• <b>How to Connect:</b><br>
  1. Select <b>UniConnect_Student</b> from your device's Wi-Fi settings.<br>
  2. Open your browser — you will be redirected to the captive portal login page.<br>
  3. Log in using your <b>Student Matriculation Number</b> and <b>portal password</b>.<br>
  4. Accept the acceptable use policy to gain access.<br>
• <b>Coverage Areas:</b> All lecture halls, libraries, hostels, the health centre, cafeteria, and administrative blocks.<br>
• <b>Data Policy:</b> Each student is allocated a daily bandwidth of <b>5 GB</b>. Unlimited access is available in the e-Library zone.<br>
• <b>Prohibited Uses:</b> Streaming pirated content, torrenting, hacking, or any illegal activity on the university network is strictly prohibited and will result in account suspension.<br>
• <b>Technical Issues:</b> Contact the ICT Support Centre at ict@university.edu or call +1 (555) 555-0199.""",
        "follow_ups": ["I can't log in to the student portal — what do I do?", "I need help with a problem / office contacts", "What other fees/charges are there?"]
    },
    {
        "id": "faq_clubs_associations",
        "category": "student_faqs",
        "question": "What student clubs and associations are available?",
        "keywords": ["student clubs", "student associations", "extracurricular", "student union", "societies"],
        "answer": """<b>🎭 STUDENT CLUBS & ASSOCIATIONS:</b><br><br>
The university has a vibrant student life with over 40 registered clubs and associations:<br><br>
• <b>Academic Associations:</b><br>
  – Computer Science Students Association (CSSA)<br>
  – Engineering Students Society (ESS)<br>
  – Nursing Students Association (NSA)<br>
  – Business and Management Students Association (BMSA)<br>
• <b>Technology & Innovation:</b><br>
  – Robotics & AI Club<br>
  – Google Developer Student Club (GDSC)<br>
  – Cybersecurity & Ethical Hacking Society<br>
• <b>Arts, Culture & Media:</b><br>
  – Drama & Performing Arts Club<br>
  – Debate & Public Speaking Society<br>
  – University Press & Media Unit<br>
• <b>Sports Clubs:</b> Football, Basketball, Athletics, Table Tennis, Swimming, and more.<br>
• <b>Community Service:</b><br>
  – Red Cross Student Unit<br>
  – Environmental Sustainability Club<br>
  – UniCares Volunteer Network<br><br>
<b>How to Join:</b> Attend the Clubs & Societies Fair held at the start of each academic session, or visit the Student Affairs Office (Block B, 2nd Floor) to register for a club.<br>
<b>Start a New Club:</b> Submit a constitution and list of 20 founding members to the Student Affairs Office for approval.""",
        "follow_ups": ["How do I apply for accommodation?", "I need help with a problem / office contacts", "What are the graduation requirements?"]
    },
    {
        "id": "faq_study_abroad",
        "category": "student_faqs",
        "question": "Are there study abroad or exchange programs?",
        "keywords": ["study abroad", "exchange program", "international student exchange", "semester abroad", "overseas study"],
        "answer": """<b>✈️ STUDY ABROAD & STUDENT EXCHANGE PROGRAMS:</b><br><br>
The university has active partnerships with institutions in Europe, North America, and Asia:<br><br>
• <b>Eligible Students:</b> Students in their 2nd or 3rd year with a minimum CGPA of <b>3.50/5.00</b> and no outstanding disciplinary records.<br>
• <b>Program Duration:</b> One semester (typically 4–6 months) at a partner university abroad.<br>
• <b>Partner Universities Include:</b> Universities in the UK, Germany, Canada, and South Africa (contact International Relations Office for the current list).<br>
• <b>What Is Covered:</b> Tuition at the partner institution is waived under bilateral agreements. Students are responsible for visa fees, flight costs, and personal upkeep.<br>
• <b>Credit Transfer:</b> Grades earned abroad are converted and credited to your local academic record upon return.<br>
• <b>Application Process:</b><br>
  1. Obtain the study abroad application form from the International Relations Office.<br>
  2. Submit a personal statement, two references, and your academic transcript.<br>
  3. Attend an interview with the International Relations Committee.<br>
  4. If selected, receive your nomination letter and apply to the partner institution directly.<br>
• <b>Contact:</b> International Relations Office — Block A, 2nd Floor | intl@university.edu | +1 (555) 555-0205""",
        "follow_ups": ["What are the graduation requirements?", "Can I defer my admission?", "I need help with a problem / office contacts"]
    },
    {
        "id": "faq_transcript_request",
        "category": "student_faqs",
        "question": "How do I request my academic transcript?",
        "keywords": ["transcript request", "official transcript", "academic transcript", "request transcript", "get transcript"],
        "answer": """<b>📄 ACADEMIC TRANSCRIPT REQUEST PROCEDURE:</b><br><br>
An official transcript is a certified record of all your academic results. Here's how to request one:<br><br>
<b>For Current Students:</b><br>
1. Log in to the Student Portal and navigate to <b>'Registrar Services'</b> → <b>'Transcript Request'</b>.<br>
2. Fill in the Transcript Request Form and specify the purpose (e.g., further studies, employment).<br>
3. Pay the transcript processing fee:<br>
   – <b>Soft copy (PDF):</b> ₦5,000 per copy.<br>
   – <b>Hard copy (sealed & stamped):</b> ₦10,000 per copy.<br>
   – <b>International courier (hard copy):</b> ₦25,000 (inclusive of DHL/courier charges).<br>
4. Upload proof of payment on the portal.<br>
5. Your transcript will be processed and ready within <b>5 – 10 working days</b>.<br><br>
<b>For Alumni:</b> Visit the Registrar's Office in person or send a formal email request to registrar@university.edu with your full name, matriculation number, and year of graduation.<br><br>
<b>Contact:</b> Registrar's Office — Block A, 1st Floor | registrar@university.edu | +1 (555) 555-0188""",
        "follow_ups": ["What is the escalation process?", "How can I contact the university?", "How do I collect my certificate?"]
    },
    {
        "id": "faq_certificate_collection",
        "category": "student_faqs",
        "question": "How do I collect my degree certificate after graduation?",
        "keywords": ["certificate collection", "collect degree", "graduation certificate", "degree certificate", "collect result"],
        "answer": """<b>🎓 DEGREE CERTIFICATE COLLECTION PROCEDURE:</b><br><br>
After successfully completing all graduation requirements, your certificate will be issued as follows:<br><br>
• <b>Convocation Ceremony:</b> Certificates are officially presented at the annual Convocation Ceremony. All graduating students are expected to attend in full academic gown.<br>
• <b>When to Collect:</b> Certificates are available for collection starting 2 weeks after the Convocation Ceremony date.<br>
• <b>How to Collect:</b><br>
  1. Confirm your name on the graduation clearance list via the student portal.<br>
  2. Obtain a clearance form from the Registrar's Office (must be signed by Bursary, Library, Hostel, and your HOD confirming no outstanding obligations).<br>
  3. Present a valid photo ID and your student portal printout at the Registrar's Office.<br>
  4. Sign the certificate receipt register to collect your original certificate.<br>
• <b>Third-Party Collection:</b> If you cannot collect in person, provide a notarized authorization letter and a photocopy of your ID for a designated representative.<br>
• <b>Certificate Replacement (Lost):</b> ₦50,000 replacement fee applies. A police report of loss is required.<br>
• <b>Contact:</b> Registrar's Office — Block A, 1st Floor | registrar@university.edu""",
        "follow_ups": ["How do I request my academic transcript?", "What are the graduation requirements?", "I need help with a problem / office contacts"]
    },
    {
        "id": "pol_supplementary_exams",
        "category": "policies",
        "question": "What is the policy on supplementary exams or retakes?",
        "keywords": ["supplementary exam", "retake exam", "carry over", "carryover", "failed course", "rewrite exam"],
        "answer": """<b>📝 SUPPLEMENTARY EXAMINATION & RETAKE POLICY:</b><br><br>
• <b>Who Qualifies:</b> Students who score below the minimum pass mark (40%) in a course are required to retake that course.<br>
• <b>Supplementary Examination:</b> A supplementary (sup) exam is offered for students who fail a course with a score between <b>30% and 39%</b> only. Students with scores below 30% must retake the full course the following session.<br>
• <b>Supplementary Exam Window:</b> Held within 4 weeks after the release of main semester results. Students must register and pay a supplementary exam fee of <b>₦15,000 per course</b>.<br>
• <b>Maximum Score on Supplementary:</b> A student who passes a supplementary exam is awarded a maximum grade of <b>C (50%)</b>, regardless of the score obtained in the supplementary exam.<br>
• <b>Maximum Retake Attempts:</b> A student may not attempt a course more than <b>3 times</b>. Failure to pass after 3 attempts leads to a referral to the Faculty Academic Board.<br>
• <b>Carryover Limit:</b> Students carrying over more than 50% of a level's course units will be required to <b>repeat the level</b> entirely.<br>
• <b>Registration:</b> Apply for supplementary exams via the Student Portal under 'Examinations' → 'Supplementary Registration'.""",
        "follow_ups": ["What are the examination rules?", "What is the attendance policy?", "What are the academic probation/suspension rules?"]
    },
    {
        "id": "pol_cgpa_grading",
        "category": "policies",
        "question": "How is the CGPA calculated and what is the grading scale?",
        "keywords": ["cgpa calculation", "gpa calculation", "grading scale", "grade point", "how cgpa is calculated", "grading system"],
        "answer": """<b>📊 CGPA CALCULATION & GRADING SCALE:</b><br><br>
The university operates on a <b>5-point grading scale</b> in line with NUC guidelines:<br><br>
<b>Grading Scale:</b><br>
• <b>A (70% – 100%):</b> 5.00 Grade Points — Excellent<br>
• <b>B (60% – 69%):</b> 4.00 Grade Points — Very Good<br>
• <b>C (50% – 59%):</b> 3.00 Grade Points — Good<br>
• <b>D (45% – 49%):</b> 2.00 Grade Points — Pass<br>
• <b>E (40% – 44%):</b> 1.00 Grade Point — Marginal Pass<br>
• <b>F (0% – 39%):</b> 0.00 Grade Points — Fail<br><br>
<b>GPA Calculation (per semester):</b><br>
GPA = Σ (Credit Units × Grade Points) ÷ Total Credit Units registered<br><br>
<b>CGPA Calculation:</b><br>
CGPA = Σ (All weighted grade points from all semesters) ÷ Total cumulative credit units<br><br>
<b>Degree Classification:</b><br>
• <b>First Class:</b> CGPA 4.50 – 5.00<br>
• <b>Second Class Upper:</b> CGPA 3.50 – 4.49<br>
• <b>Second Class Lower:</b> CGPA 2.50 – 3.49<br>
• <b>Third Class:</b> CGPA 1.50 – 2.49<br>
• <b>Pass:</b> CGPA 1.00 – 1.49<br>
• <b>Fail:</b> CGPA below 1.00<br><br>
<i>Your current CGPA is always visible on your Student Portal dashboard under 'Academic Records'.</i>""",
        "follow_ups": ["When are results released?", "What are the academic probation/suspension rules?", "What are the graduation requirements?"]
    },
    {
        "id": "pol_academic_probation",
        "category": "policies",
        "question": "What are the academic probation and suspension rules?",
        "keywords": ["academic probation", "academic suspension", "probation rules", "suspension rules", "low cgpa consequences"],
        "answer": """<b>⚠️ ACADEMIC PROBATION & SUSPENSION POLICY:</b><br><br>
The university enforces strict academic standing requirements to ensure student progress:<br><br>
<b>Academic Probation:</b><br>
• A student is placed on <b>Academic Probation</b> if their semester GPA falls below <b>1.00</b> or their CGPA drops below <b>1.50</b>.<br>
• Students on probation are notified in writing by the Registrar within 2 weeks of result publication.<br>
• A student on probation is assigned a <b>Faculty Academic Adviser</b> who must approve their course registration for the next semester.<br>
• Students on probation may be limited to a reduced course load (maximum of 15 credit units per semester).<br><br>
<b>Academic Suspension:</b><br>
• A student placed on probation who <b>fails to improve</b> their GPA in the following semester is recommended for <b>Academic Suspension</b>.<br>
• Suspension duration: <b>One full academic session</b> (2 semesters). During this period, the student may not attend lectures or write exams.<br>
• A suspended student must write a formal appeal letter to the Faculty Academic Board before being allowed to return.<br><br>
<b>Withdrawal / Rustication:</b><br>
• A student suspended twice or who accumulates excessive failed courses may be permanently <b>withdrawn</b> from the university.<br>
• This decision is made solely by the Senate Academic Committee.<br><br>
<i>Students facing academic difficulties are strongly encouraged to consult their departmental Academic Adviser as early as possible.</i>""",
        "follow_ups": ["How is the CGPA calculated and what is the grading scale?", "What is the policy on supplementary exams or retakes?", "What are the graduation requirements?"]
    }
]
