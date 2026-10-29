# Interview Lab
## AI-Powered Mock Interview Evaluation System

An AI-powered interview preparation platform that helps candidates practise technical interviews, evaluate their answers, identify missing concepts, and improve their interview performance through personalised feedback.

The system is designed to combine resume-based question selection, voice-based interviewing, automated answer evaluation, and performance reporting in a single application.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Problem Statement](#-problem-statement)
* [Objectives](#-objectives)
* [Key Features](#-key-features)
* [System Architecture](#-system-architecture)
* [Technology Stack](#-technology-stack)
* [Answer Evaluation Methodology](#-answer-evaluation-methodology)
* [Dataset](#-dataset)
* [Evaluation Results](#-evaluation-results)
* [Application Workflow](#-application-workflow)
* [Project Structure](#-project-structure)
* [Installation and Setup](#-installation-and-setup)
* [Configuration](#-configuration)
* [Testing](#-testing)
* [Limitations](#-limitations)
* [Future Enhancements](#-future-enhancements)
* [Contributors](#-contributors)

---

## 📖 Overview

Preparing for technical interviews requires repeated practice, technical knowledge, and an understanding of one's strengths and weaknesses.

Traditional mock interviews often require a human interviewer and may not provide consistent, immediate feedback.

The **AI-Powered Mock Interview Evaluation System** aims to make interview preparation more accessible by automating important parts of the interview process.

Candidates can configure an interview based on their preferred technical domain and difficulty level. The system can then present interview questions, process candidate responses, evaluate their technical content, and provide feedback.

The intended application workflow includes resume processing, voice-based answers, automated evaluation, and a final performance report.

## ❗ Problem Statement

Students and job seekers often face difficulties preparing for technical interviews because:

* Access to experienced interviewers may be limited.
* Repeated mock interviews can be time-consuming.
* Candidates may not know which technical concepts they have missed.
* Feedback may not be available immediately.
* Generic interview questions may not reflect a candidate's projects and skills.

This project aims to address these challenges through an automated interview-practice platform that provides structured questions, answer evaluation, and actionable feedback.

---

## 🎯 Objectives

The primary objectives are:

1. Provide an interactive platform for technical interview practice.
2. Support interview preparation across multiple technical domains.
3. Allow candidates to select their preferred interview difficulty.
4. Extract relevant information from resumes where resume parsing is implemented.
5. Support voice-based responses through an integrated speech-to-text component.
6. Evaluate candidate answers against reference answers and expected concepts.
7. Identify missing concepts and potential misconceptions.
8. Generate question-wise feedback and an interview performance summary.
9. Help candidates identify topics that require further preparation.

---

## ✨ Key Features

### 1. Resume-Based Interview Preparation

The system is designed to accept a candidate's resume and extract relevant information, including:

* Technical skills
* Projects
* Education
* Experience
* Technologies used

This information can help select or generate interview questions relevant to the candidate's background.

### 2. Multiple Interview Domains

The question dataset covers four technical domains:

* Artificial Intelligence
* Machine Learning
* Web Development
* Data Science

### 3. Difficulty Selection

Candidates can choose questions according to their preparation level:

* Easy
* Medium
* Hard

### 4. Question Generation and Selection

The system can select questions from the existing dataset according to the chosen domain and difficulty.

An optional Large Language Model (LLM) integration can be used to generate additional resume-specific questions when configured.

Dataset-based question selection provides a fallback when an external LLM service is unavailable.

### 5. Voice-Based Interviewing

The intended voice-interview workflow allows candidates to record their answers through a microphone.

A speech-to-text component converts recorded audio into a transcript that can be passed to the answer evaluator.

Actual recording and transcription functionality depends on the configured implementation and supported browser or service.

### 6. Automated Answer Evaluation

The existing Python evaluation component analyses candidate responses using techniques such as:

* Text similarity
* Concept coverage
* Missing-concept identification
* Heuristic misconception checks

The evaluator produces a technical score and a corresponding performance category.

### 7. Individual Answer Feedback

The system can display feedback associated with each evaluated answer, including:

* Technical score
* Performance category
* Concepts covered
* Missing concepts
* Detected warnings, where supported
* Areas for improvement

### 8. Final Interview Report

The intended reporting functionality aggregates interview results to summarise:

* Overall performance
* Question-wise scores
* Topic-wise performance
* Strong areas
* Topics requiring improvement
* Frequently missing concepts
* Recommended preparation topics

Report accuracy depends on the evaluation results collected during the interview session.

---

## 🏗️ System Architecture

The application is designed around three main layers.

### Frontend

Provides the user interface for:

* Resume upload
* Interview configuration
* Question presentation
* Voice recording
* Feedback display
* Final performance reporting

### Backend

The backend is intended to use FastAPI to coordinate application operations, including request handling, resume processing, question retrieval, transcription requests, and answer evaluation.

### Evaluation Component

The Python answer evaluator compares candidate responses with reference answers and expected concepts to estimate technical answer quality.

### Architecture Diagram

```text
                    Candidate
                        |
                        v
                 Frontend Website
                        |
                        v
                  FastAPI Backend
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
     Resume         Question       Session
     Processing     Selection      Management
          |             |
          +-------------+
                        |
                        v
                 Interview Question
                        |
                        v
                  Voice Recording
                        |
                        v
                  Speech-to-Text
                        |
                        v
                  Answer Transcript
                        |
                        v
                  AnswerEvaluator
                        |
                        v
                 Individual Feedback
                        |
                        v
                 Final Interview Report
```

*This diagram represents the intended logical architecture. The actual implementation may differ depending on which components have been integrated and tested.*

---

## 🛠️ Technology Stack

The following technologies are part of the project's discussed design. Confirm the final repository before treating every item as an implemented dependency.

| Technology            | Purpose                                                       |
| --------------------- | ------------------------------------------------------------- |
| Python                | Answer evaluation and backend processing                      |
| FastAPI               | Backend API framework                                         |
| React                 | Frontend framework, if used in the final application          |
| Vite                  | Frontend development and build tool, if configured            |
| HTML, CSS, JavaScript | Web interface development                                     |
| TF-IDF                | Statistical text representation                               |
| Cosine Similarity     | Comparison of text vectors                                    |
| NLP techniques        | Text preprocessing and concept matching                       |
| Sentence Transformers | Optional semantic-embedding approach                          |
| Speech-to-Text        | Converts recorded speech into text                            |
| LLM API               | Optional resume-specific question generation                  |
| Question Dataset      | Stores interview questions and related evaluation information |

**Note:** TF-IDF and cosine similarity are traditional text-processing techniques, not deep learning models. Deep learning may be used by optional pretrained speech-recognition, embedding, or language-generation components, depending on the final integration.

---

## 🧠 Answer Evaluation Methodology

The answer evaluator is implemented in:

`evaluate_answer.py`

The main evaluator class is:

`AnswerEvaluator`

Its purpose is to estimate the technical quality of a candidate's answer by comparing the response with a reference answer and expected concepts.

### 1. Text Preprocessing

Text preprocessing helps normalise candidate responses before comparison.

Depending on the implementation, this can include lowercasing, stemming, synonym normalisation, and extracting meaningful phrases.

This helps reduce differences caused by wording and grammar.

### 2. TF-IDF Representation

TF-IDF stands for **Term Frequency–Inverse Document Frequency**.

It represents text numerically according to the frequency and relative importance of its terms.

A common formulation is:

$$
TFIDF(t,d)=TF(t,d)\times IDF(t)
$$

Where:

* \(t\) represents a term.
* \(d\) represents a document.
* \(TF\) measures term frequency.
* \(IDF\) reduces the weight of terms common across documents.

### 3. Cosine Similarity

Cosine similarity measures the similarity between two numerical vectors.

$$
\operatorname{CosineSimilarity}(A,B)=
\frac{A\cdot B}{\|A\|\|B\|}
$$

It can be used to compare the vector representation of a reference answer with that of a candidate's response.

However, text similarity alone cannot guarantee technical correctness.

### 4. Concept Coverage

Concept coverage measures how many expected concepts are identified in the candidate's answer.

A simplified formulation is:

$$
\text{Concept Coverage}=
\frac{\text{Expected Concepts Covered}}
{\text{Total Expected Concepts}}
$$

For example, if an answer contains three of four expected concepts, its concept coverage is 75%.

### 5. Missing Concepts

The evaluator identifies expected concepts that were not detected in the response.

This information can be used to explain what the candidate should include in a stronger answer.

### 6. Misconception Checks

The evaluator includes limited heuristic checks for certain misleading or contradictory responses.

These checks help address cases where an answer contains relevant keywords but communicates an incorrect relationship.

They are not a substitute for complete semantic reasoning.

### 7. Final Score and Feedback

The evaluator combines its supported evaluation signals to produce a score, performance category, and related feedback.

The exact scoring formula and weights are defined by the current implementation in `evaluate_answer.py`.

---

## 📊 Dataset

The existing dataset previously reported for this project contains:

* **300 interview questions**
* **1,200 synthetic candidate answers**

The questions cover four technical domains and three difficulty levels.

### Question Distribution

| Domain                  |    Easy |  Medium |    Hard |   Total |
| ----------------------- | ------: | ------: | ------: | ------: |
| Artificial Intelligence |      25 |      25 |      25 |      75 |
| Machine Learning        |      25 |      25 |      25 |      75 |
| Web Development         |      25 |      25 |      25 |      75 |
| Data Science            |      25 |      25 |      25 |      75 |
| **Total**               | **100** | **100** | **100** | **300** |

The dataset supports question selection and evaluation testing.

### Synthetic Candidate Answers

Synthetic answers are artificially generated or constructed responses used to test the evaluator under different conditions.

They can represent:

* Correct answers
* Partially correct answers
* Answers missing important concepts
* Incorrect answers
* Irrelevant answers
* Answers containing misleading statements

Synthetic data makes controlled testing easier, but it may not fully represent the variety of real candidate responses.

---

## 📈 Evaluation Results

The following results were previously reported for the answer evaluator on 1,200 synthetic candidate answers.

| Metric                                | Reported Result |
| ------------------------------------- | --------------: |
| Mean Absolute Error (MAE)             |            9.75 |
| Root Mean Squared Error (RMSE)        |           14.96 |
| Spearman Correlation                  |          0.8445 |
| Four-Category Classification Accuracy |          62.83% |
| Targeted Test Cases Passed            |           10/10 |

These figures describe the previously reported evaluator benchmark, not the performance of every component of the complete web application.

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted scores and reference scores.

Lower MAE generally indicates better score agreement.

### Root Mean Squared Error (RMSE)

RMSE measures the square root of the average squared prediction error.

It penalises large errors more heavily than MAE.

### Spearman Correlation

Spearman correlation measures how closely the predicted rankings follow the reference rankings.

The reported value of 0.8445 indicates a strong ranking relationship on the benchmark, but it does not mean that 84.45% of answers were correct.

### Classification Accuracy

The reported classification accuracy of 62.83% measures the proportion of benchmark examples assigned the correct quality category.

Intermediate categories were more challenging to classify than clearly poor or excellent answers.

### Important Evaluation Note

The benchmark uses synthetic answers. Its results should not be treated as guaranteed performance on real interview candidates.

Further validation using real, human-labelled responses would provide stronger evidence of generalisation.

Rerun the benchmark after any significant evaluator changes before publishing the results as current.

---

## 🔄 Application Workflow

The intended application workflow is:

1. The candidate opens the application.
2. The candidate uploads a resume.
3. The application extracts relevant resume information.
4. The candidate selects a domain and difficulty level.
5. The application selects or generates suitable questions.
6. The application presents one question at a time.
7. The candidate records an answer using a microphone.
8. The speech-to-text component converts the audio into text.
9. The transcript is sent to the answer evaluator.
10. The evaluator produces a score and feedback.
11. The candidate proceeds through the remaining questions.
12. The application aggregates the interview results.
13. The final report identifies strengths, missing concepts, and preparation recommendations.

This workflow describes the intended functionality. Individual stages should be verified against the running application before claiming the complete workflow is operational.

---

## 📁 Project Structure

The exact structure depends on the current repository. The following is an illustrative layout:

```text
AI-Interview-Evaluation-System/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── data/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── main.py
│   ├── ...
│   └── ...
│
├── evaluate_answer.py
├── test_evaluator_cases.py
├── run_benchmark.py
├── EVALUATION_REPORT.md
├── benchmark_results.csv
├── requirements.txt
└── README.md
```

*This is a suggested structure, not a claim that every listed file or folder exists in the current repository. Update it to match the actual project.*

---

## ⚙️ Installation and Setup

The exact installation commands depend on the existing repository structure and dependency files.

### Prerequisites

Install the tools required by your actual project:

* Python
* Node.js and npm, if the frontend uses React/Vite
* Git, if cloning the repository
* Any additional dependencies required by the speech-to-text or question-generation integrations

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Interview-Evaluation-System
```

Replace the placeholder with your repository's actual URL.

### 2. Set Up the Python Environment

From the directory containing the backend or Python evaluation code:

```bash
python -m venv venv
```

Activate the environment on Windows Command Prompt:

```bat
venv\Scripts\activate
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies if a `requirements.txt` file is present:

```bash
pip install -r requirements.txt
```

If your project has a separate backend dependency file, install dependencies from that file instead.

### 3. Run the Backend

If the actual FastAPI entry point is `main.py` and the application object is named `app`, a typical command is:

```bash
uvicorn main:app --reload
```

If the entry point or application object has a different name, adjust the command accordingly.

### 4. Run the Frontend

If the frontend uses React/Vite, open a terminal in its directory:

```bash
npm install
npm run dev
```

Open the local URL printed by Vite in the terminal.

### 5. Run the Evaluator Tests

If these files exist in the repository and their dependencies are installed:

```bash
python evaluate_answer.py
python test_evaluator_cases.py
python run_benchmark.py
```

Use the actual project instructions if the commands differ.

---

## 🔐 Configuration

Some optional integrations may require environment variables.

For example, a frontend connected to a local backend may use:

```env
VITE_API_BASE_URL=http://localhost:8000
```

An LLM integration or external speech-to-text provider may require additional server-side environment variables.

Use the exact variable names expected by your implementation.

**Security guidelines:**

* Never commit API keys or passwords to GitHub.
* Store secrets in environment variables or an appropriate secrets manager.
* Do not expose private API keys in frontend code.
* Keep uploaded resumes and interview transcripts protected.
* Do not log sensitive candidate information unnecessarily.

---

## 🧪 Testing

The evaluator has previously been tested with ten targeted cases covering scenarios such as:

* Technically correct paraphrases
* Incorrect answers containing relevant keywords
* Partial concept coverage
* Fluent but irrelevant answers
* Short but correct responses
* Major misconceptions
* Empty responses
* Missing important concepts
* Synonymous technical expressions

The previously reported result was **10 out of 10 targeted tests passed**.

For the complete application, additional tests should verify:

* Resume upload and parsing
* Domain and difficulty filtering
* Question generation and fallback behaviour
* Microphone recording
* Speech transcription
* Evaluator integration
* Question-wise feedback
* Session state management
* Final report generation
* Error handling when APIs or external services are unavailable

Only report these integration tests as passing after they have actually been executed.

---

## ⚠️ Limitations

The project has several limitations that should be considered.

1. **Synthetic evaluation data:** The benchmark does not fully represent real interview responses.
2. **Text similarity limitations:** Similarity does not guarantee that a response is technically correct.
3. **Intermediate category classification:** Distinguishing Good from Average answers remains challenging.
4. **Limited misconception detection:** Heuristic rules cannot identify every incorrect technical statement.
5. **Speech recognition errors:** Audio quality, accents, and technical terminology may affect transcription.
6. **Question coverage:** A finite dataset cannot cover every possible interview question.
7. **Resume parsing variability:** Different document formats may affect extraction quality.
8. **External dependencies:** LLM and speech-to-text features may depend on API availability or configuration.
9. **Evaluation fairness:** Automated scores may not capture every valid explanation or alternative approach.

The system should be considered an interview-practice aid rather than a definitive replacement for human technical assessment.

---

## 🚀 Future Enhancements

Potential future improvements include:

* Evaluating answers with a larger human-labelled dataset.
* Improving semantic answer evaluation.
* Adding more technical domains and question categories.
* Supporting more resume formats.
* Improving speech recognition for technical vocabulary.
* Expanding misconception detection.
* Adding more detailed topic-wise performance analytics.
* Supporting downloadable interview reports.
* Improving question personalisation with validated LLM-generated questions.
* Adding user accounts and interview-history tracking.
* Evaluating fairness and consistency across different speaking styles.

---

## 👥 Contributors

Add the names and responsibilities of your actual team members here.

| Team Member   | Responsibility                                   |
| ------------- | ------------------------------------------------ |
| Team Member 1 | Answer evaluation and model development          |
| Team Member 2 | Frontend development                             |
| Team Member 3 | Backend development and integration              |
| Team Member 4 | Testing, documentation, and project coordination |

Replace these placeholders with your team's actual names and responsibilities.

---

## 📌 Conclusion

The AI-Powered Mock Interview Evaluation System aims to provide a structured and accessible platform for technical interview preparation.

By combining resume processing, question selection or generation, voice-based responses, automated answer evaluation, and performance reporting, the project aims to help candidates understand their strengths and identify areas requiring improvement.

The existing answer evaluator has demonstrated promising ranking behaviour on its synthetic benchmark, while further validation on real candidate responses and end-to-end testing remain important for improving reliability.

**The overall goal is to help candidates practise consistently, receive actionable feedback, and prepare more effectively for technical interviews.**
