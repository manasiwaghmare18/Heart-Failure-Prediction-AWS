# Data Documentation - Heart Failure Prediction Project

## Dataset Overview

**Dataset Name:** Heart Failure Clinical Records  
**Total Records:** 299 patients  
**Total Features:** 13 (12 input features + 1 target variable)  
**Missing Values:** 0 (Complete dataset)  
**Data Format:** CSV  
**Source:** UCI Machine Learning Repository  
**Class Distribution:** 67.89% No Event, 32.11% Event  

---

## Feature Dictionary & Clinical Significance

### 1. age
**Type:** Numeric (Integer)  
**Unit:** Years  
**Range:** 40-95 years  
**Mean:** 60.87 | **Std Dev:** 11.89  

**Description:**  
The age of the patient at the time of clinical assessment.

**Clinical Significance:**  
Age is a well-established non-modifiable risk factor for heart failure. Older patients demonstrate progressively higher risk of adverse events. This feature captures age-related physiological decline in cardiac function.

**Data Quality:**  
- No missing values
- All values within physiologically reasonable ranges
- Normal distribution with slight right skew

---

### 2. anaemia
**Type:** Binary (0/1)  
**Values:** 0 = No anemia, 1 = Anemia present  
**Distribution:** No Anemia: 165 (55.2%) | Anemia: 134 (44.8%)  

**Description:**  
Binary indicator of whether the patient has a decrease in red blood cells (erythrocytes) or hemoglobin levels below normal thresholds.

**Clinical Significance:**  
Anemia worsens heart failure symptoms by reducing oxygen-carrying capacity of blood. It increases cardiac workload and is associated with poorer prognosis. Presence of anemia is a significant prognostic indicator in heart failure patients.

**Data Quality:**  
- Well-balanced distribution
- Clear binary classification
- No missing values

---

### 3. creatinine_phosphokinase
**Type:** Numeric (Integer)  
**Unit:** mcg/L (micrograms per liter)  
**Range:** 23-7861 mcg/L  
**Mean:** 581.84 | **Median:** 250 | **Std Dev:** 970.29  

**Description:**  
Serum level of CPK (creatinine phosphokinase) enzyme in the blood. CPK catalyzes phosphorylation of creatine and is found in cardiac muscle, skeletal muscle, and brain.

**Clinical Significance:**  
Elevated CPK levels can indicate muscle damage, including cardiac myocardial injury. In heart failure context, elevated CPK may suggest ongoing myocardial damage or recent cardiac events. The wide range suggests heterogeneous cardiac damage severity.

**Data Quality:**  
- Significant outliers present (max 7861 vs median 250)
- Likely represents legitimate clinical variability
- Right-skewed distribution
- No missing values

**Note:** Extreme values retained as they represent important clinical information about severe myocardial damage.

---

### 4. diabetes
**Type:** Binary (0/1)  
**Values:** 0 = No diabetes, 1 = Diabetes present  
**Distribution:** No Diabetes: 163 (54.5%) | Diabetes: 136 (45.5%)  

**Description:**  
Binary indicator of whether the patient has been diagnosed with diabetes mellitus (Type 1 or Type 2).

**Clinical Significance:**  
Diabetes is a major independent risk factor for heart failure development. Hyperglycemia causes myocardial dysfunction through multiple mechanisms including inflammation, oxidative stress, and altered calcium handling. Diabetes is prevalent in heart failure populations.

**Data Quality:**  
- Well-balanced distribution
- Clear binary classification
- No missing values
- Reflects clinical prevalence of diabetes in heart failure populations

---

### 5. ejection_fraction
**Type:** Numeric (Integer)  
**Unit:** % (Percentage)  
**Range:** 14-80%  
**Mean:** 38.08% | **Median:** 38% | **Std Dev:** 11.83%  

**Description:**  
Percentage of blood leaving the left ventricle with each heartbeat. Measured during echocardiography and represents the heart's pumping efficiency.

**Clinical Significance:**  
**MOST IMPORTANT PREDICTOR IN THIS DATASET**  
- Normal EF: >55% indicates healthy cardiac function
- Reduced EF: <40% indicates systolic heart failure
- Lower ejection fraction strongly inversely correlates with heart failure risk
- EF <30% indicates severe dysfunction requiring intensive management
- Most critical parameter for heart failure classification and prognosis

**Clinical Interpretation:**
- EF 50-80%: Normal
- EF 41-49%: Borderline reduced
- EF 31-40%: Mildly reduced
- EF 21-30%: Moderately reduced
- EF ≤20%: Severely reduced

**Data Quality:**  
- No missing values
- All values physiologically plausible
- Mean of 38% suggests predominantly reduced EF population
- Clear discriminatory power for prediction

---

### 6. high_blood_pressure
**Type:** Binary (0/1)  
**Values:** 0 = Normal BP, 1 = Hypertension present  
**Distribution:** Normal: 104 (34.8%) | Hypertension: 195 (65.2%)  

**Description:**  
Binary indicator of whether the patient has been diagnosed with hypertension (high blood pressure).

**Clinical Significance:**  
Hypertension is the leading cause of heart failure in developed nations. Chronic elevated blood pressure causes left ventricular hypertrophy and diastolic dysfunction. Highly prevalent in this cohort (65.2%), reflecting typical heart failure population characteristics.

**Data Quality:**  
- Imbalanced distribution (65.2% vs 34.8%) reflects clinical prevalence
- No missing values
- Clear binary classification

---

### 7. platelets
**Type:** Numeric (Integer)  
**Unit:** kiloplatelets/mL (thousand platelets per milliliter)  
**Range:** 25-850 kiloplatelets/mL  
**Mean:** 262.36 | **Median:** 262 | **Std Dev:** 97.77  

**Description:**  
The concentration of blood platelets (thrombocytes) per milliliter of blood.

**Clinical Significance:**  
Platelet counts reflect bone marrow function and clotting ability. Low platelet counts may indicate:
- Bone marrow dysfunction
- Splenomegaly from cardiac cirrhosis
- Medication side effects

High platelet counts may indicate:
- Inflammatory response
- Acute stress response
- Reactive thrombocytosis

**Reference Range:** 150-400 kiloplatelets/mL (normal)

**Data Quality:**  
- Most values within normal range
- Few extreme values (25, 850) likely represent clinical outliers
- No missing values
- Relatively normal distribution

---

### 8. serum_creatinine
**Type:** Numeric (Float)  
**Unit:** mg/dL (milligrams per deciliter)  
**Range:** 0.7-9.4 mg/dL  
**Mean:** 1.39 | **Median:** 1.1 | **Std Dev:** 1.54  

**Description:**  
The concentration of creatinine in blood serum. Creatinine is a waste product of muscle metabolism filtered by the kidneys.

**Clinical Significance:**  
**SECOND MOST IMPORTANT PREDICTOR**  
- Primary indicator of kidney function/renal dysfunction
- Normal range: 0.7-1.3 mg/dL
- Elevated creatinine indicates decreased glomerular filtration rate (GFR)
- Cardiorenal syndrome: combination of heart and kidney dysfunction
- Strong prognostic indicator in heart failure
- Elevated levels correlate with worse outcomes and mortality risk

**Clinical Interpretation:**
- <1.0 mg/dL: Normal kidney function
- 1.0-1.5 mg/dL: Mild kidney dysfunction
- 1.5-2.5 mg/dL: Moderate kidney dysfunction
- >2.5 mg/dL: Severe kidney dysfunction

**Data Quality:**  
- Mean of 1.39 suggests mild-to-moderate kidney dysfunction common in cohort
- Right-skewed distribution with outliers up to 9.4 mg/dL
- No missing values
- Outliers likely represent severe renal impairment cases

---

### 9. serum_sodium
**Type:** Numeric (Integer)  
**Unit:** mEq/L (milliequivalents per liter)  
**Range:** 113-148 mEq/L  
**Mean:** 136.63 | **Median:** 137 | **Std Dev:** 4.41  

**Description:**  
The concentration of sodium ions in blood serum.

**Clinical Significance:**  
**THIRD IMPORTANT PREDICTOR**  
- Normal range: 135-145 mEq/L
- Hyponatremia (low sodium <135 mEq/L): Associated with worse prognosis
- Hypernatremia (high sodium >145 mEq/L): Relatively rare in heart failure
- In heart failure: neurohormonal activation increases ADH, leading to sodium dilution
- Strong independent predictor of mortality in heart failure
- Values <130 mEq/L indicate severe disease

**Clinical Interpretation:**
- >145: Hypernatremia (rare, concerning)
- 135-145: Normal
- 130-135: Mild hyponatremia (concerning)
- <130: Severe hyponatremia (very concerning)

**Data Quality:**  
- Tight distribution (range 113-148)
- Mean of 136.63 suggests slightly low sodium in cohort
- No missing values
- Standard deviation of only 4.41 shows relative stability
- Lower values represent higher-risk patients

---

### 10. sex
**Type:** Binary (0/1)  
**Values:** 0 = Male, 1 = Female  
**Distribution:** Male: 194 (64.9%) | Female: 105 (35.1%)  

**Description:**  
The biological sex of the patient.

**Clinical Significance:**  
Gender differences in heart failure:
- **Males:** Traditionally higher prevalence of systolic HF, higher mortality rates
- **Females:** Often present with preserved ejection fraction (HFpEF), better short-term outcomes but under-represented in studies
- Different hormonal, structural, and inflammatory responses
- Sex-based differences in medication effectiveness
- Current cohort predominantly male (64.9%)

**Data Quality:**  
- Clear binary classification
- Male-dominant distribution reflects historical study biases
- No missing values

---

### 11. smoking
**Type:** Binary (0/1)  
**Values:** 0 = Non-smoker, 1 = Smoker  
**Distribution:** Non-smoker: 203 (67.9%) | Smoker: 96 (32.1%)  

**Description:**  
Binary indicator of current or recent smoking status.

**Clinical Significance:**  
Smoking is a major modifiable cardiovascular risk factor:
- Damages endothelial function
- Increases atherosclerosis risk
- Causes myocardial inflammation
- Reduces oxygen delivery
- Increases arrhythmia risk
- Smoking cessation has proven benefits

**Data Quality:**  
- Clear binary classification
- 32.1% smoking rate typical for heart failure populations
- No missing values
- Reflects modifiable risk factor in cohort

---

### 12. time
**Type:** Numeric (Integer)  
**Unit:** Days  
**Range:** 4-2015 days  
**Mean:** 130.26 | **Median:** 115 | **Std Dev:** 77.61  

**Description:**  
The duration of the follow-up period for each patient, measured in days.

**Clinical Significance:**  
- Represents observation period length
- Longer follow-up allows detection of delayed events
- Variable follow-up creates bias in longitudinal analysis
- Important for survival analysis and time-dependent metrics
- Short follow-ups may miss delayed complications

**Data Quality:**  
- Range of 4-2015 days shows variable follow-up duration
- Mean of 130 days (~4.3 months) is relatively short
- Right-skewed distribution with some long-term follow-ups
- No missing values

---

### 13. DEATH_EVENT (Target Variable)
**Type:** Binary (0/1)  
**Values:** 0 = No heart failure, 1 = Heart failure occurred  
**Distribution:**
- No Event (0): 203 records (67.89%)
- Event (1): 96 records (32.11%)
- **Class Imbalance Ratio:** 2.11:1

**Description:**  
Binary target variable indicating whether a heart failure event (death or significant cardiac event) occurred during the follow-up period.

**Clinical Significance:**  
Represents the primary outcome of interest. Predicting this outcome enables:
- Risk stratification of patients
- Identification of high-risk individuals
- Targeting of intensive interventions
- Prognostic assessment
- Treatment selection

**Class Imbalance:**  
- Slightly imbalanced (67.89% vs 32.11%)
- Manageable for machine learning
- Stratified cross-validation recommended
- Recall metric particularly important

**Data Quality:**  
- Clear binary classification
- No missing values
- Well-defined clinical outcome
- Sufficient positive examples (96) for model training

---

## Statistical Summary Table

| Feature | Type | Mean | Median | Std Dev | Min | Max | Missing |
|---------|------|------|--------|---------|-----|-----|---------|
| age | Numeric | 60.87 | 61 | 11.89 | 40 | 95 | 0 |
| anaemia | Binary | 0.45 | 0 | 0.50 | 0 | 1 | 0 |
| creatinine_phosphokinase | Numeric | 581.84 | 250 | 970.29 | 23 | 7861 | 0 |
| diabetes | Binary | 0.46 | 0 | 0.50 | 0 | 1 | 0 |
| ejection_fraction | Numeric | 38.08 | 38 | 11.83 | 14 | 80 | 0 |
| high_blood_pressure | Binary | 0.65 | 1 | 0.48 | 0 | 1 | 0 |
| platelets | Numeric | 262.36 | 262 | 97.77 | 25 | 850 | 0 |
| serum_creatinine | Numeric | 1.39 | 1.1 | 1.54 | 0.7 | 9.4 | 0 |
| serum_sodium | Numeric | 136.63 | 137 | 4.41 | 113 | 148 | 0 |
| sex | Binary | 0.35 | 0 | 0.48 | 0 | 1 | 0 |
| smoking | Binary | 0.32 | 0 | 0.47 | 0 | 1 | 0 |
| time | Numeric | 130.26 | 115 | 77.61 | 4 | 2015 | 0 |
| DEATH_EVENT | Binary | 0.32 | 0 | 0.47 | 0 | 1 | 0 |

---

## Data Quality Assessment

**Missing Values:** ✓ Perfect (0%)  
**Duplicates:** ✓ None detected  
**Data Type Consistency:** ✓ All correct  
**Outliers:** Present but clinically valid  
**Class Balance:** Acceptable (2.11:1)  
**Data Completeness:** 100%  

---

## Preprocessing Recommendations

1. **Feature Scaling:** StandardScaler (required for KNN, SVM)
2. **Train-Test Split:** 80-20 with stratification
3. **Cross-Validation:** 5-fold stratified cross-validation
4. **Outlier Handling:** Retain (clinically significant)
5. **Class Imbalance:** Monitor recall metric, consider stratification

---
