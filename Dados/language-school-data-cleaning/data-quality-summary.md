# 📊 Data Quality Summary

## 1. Context
- **Dataset:** Language school data
- **Data Source:** Artificially generated data  
- **Time Period Covered:** 2009-2027  
- **Purpose of Analysis:** Data cleaning practice with Pandas  
- **Critical Fields:**  student_id, class_id, teacher_id, course, student_status, student_email, enrollment_date

---

## 2. Data Quality Dimensions

### 🔹 Completeness
- **Rule:** Required fields must be filled.  
- **Score:** 67.2%  
- **Issues Found:** Lack of standardization across the columns, special critical fields.   
- **Impact:** Such values would skew or make an proper analysis difficult to be performed. 

### 🔹 Accuracy
- **Rule:** Data must correctly represent real-world values.  
- **Score:** 97,8%
- **Issues Found:** 48 unreal values were found in the monthly_fee column, 30 in the enrollment_date, 84 in the student_email and 78 in the age column. 
- **Impact:** Such values represent unreal values and consequently they cause misunderstandings  and failure in obtaining real and trustworthy insights from analysis or dashboards.   

### 🔹 Consistency
- **Rule:** Data must be coherent across columns and systems.  
- **Score:**  
- **Issues Found:**  
- **Impact:**  

### 🔹 Validity
- **Rule:** Data must follow business rules and valid formats.  
- **Score:**  
- **Issues Found:**  
- **Impact:**  

### 🔹 Uniqueness
- **Rule:** No duplicate records should exist.  
- **Score:**  
- **Issues Found:**  
- **Impact:**  

### 🔹 Timeliness
- **Rule:** Data must be updated according to business needs.  
- **Score:**  
- **Issues Found:**  
- **Impact:**  

---

## 3. Overall Scorecard

| Dimension    | Score |
|--------------|-------|
| Completeness |       |
| Accuracy     |       |
| Consistency  |       |
| Validity     |       |
| Uniqueness   |       |
| Timeliness   |       |

**Final Score:**  
**Confidence Level:**  

---

## 4. Key Issues Identified
-  Multiple inconsistencies found concerning teacher-class-course;
-  Unique student_id addressed to several different students;
-  Lack of standardization in the critical fields;

---

## 5. Action Plan
-  
-  
-  

---

## 6. Additional Notes
-  
