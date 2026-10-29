# -*- coding: utf-8 -*-
"""
Resume Parser Module for AI Mock Interview Evaluation System
Extracts skills, projects, education, experience, and contact info from PDF and DOCX files.
Isolates untrusted user content and provides graceful error handling.
"""

import os
import re
from typing import Dict, Any, List, Optional
import pypdf
import docx

# Curated technical skills dictionary organized by domains
TECHNICAL_SKILLS_TAXONOMY = {
    # AI & Core CS
    "bfs", "dfs", "a*", "dijkstra", "graph traversal", "heuristics", "expert systems",
    "knowledge representation", "propositional logic", "first order logic", "turing test",
    "search algorithms", "minimax", "alpha-beta pruning", "reinforcement learning",
    # Machine Learning
    "machine learning", "deep learning", "neural networks", "cnn", "rnn", "lstm",
    "transformer", "bert", "gpt", "llm", "random forest", "decision tree", "svm",
    "gradient boosting", "xgboost", "lightgbm", "linear regression", "logistic regression",
    "kmeans", "pca", "hyperparameter tuning", "cross validation", "overfitting", "underfitting",
    "scikit-learn", "tensorflow", "pytorch", "keras", "huggingface", "opencv",
    # Data Science & Statistics
    "data science", "statistics", "probability", "hypothesis testing", "p-value",
    "ab testing", "pandas", "numpy", "scipy", "matplotlib", "seaborn", "sql",
    "data cleaning", "imputation", "outlier detection", "feature engineering",
    "data visualization", "tableau", "power bi", "polars",
    # Web Development
    "web development", "javascript", "typescript", "python", "html", "css",
    "react", "next.js", "vue", "angular", "node.js", "express", "fastapi",
    "flask", "django", "rest api", "graphql", "websockets", "postgresql",
    "mysql", "mongodb", "redis", "docker", "kubernetes", "aws", "gcp", "azure",
    "git", "ci/cd", "tailwind", "responsive design", "microservices"
}

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts raw text from a PDF file using pypdf."""
    text_content = []
    try:
        reader = pypdf.PdfReader(file_path)
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text_content.append(page_text)
        return "\n".join(text_content).strip()
    except Exception as e:
        raise ValueError(f"Failed to read PDF file: {str(e)}")

def extract_text_from_docx(file_path: str) -> str:
    """Extracts raw text from a DOCX file using python-docx."""
    try:
        doc = docx.Document(file_path)
        text_content = [para.text for para in doc.paragraphs if para.text.strip()]
        for table in doc.tables:
            for row in table.rows:
                row_text = " | ".join(cell.text.strip() for cell in row.cells if cell.text.strip())
                if row_text:
                    text_content.append(row_text)
        return "\n".join(text_content).strip()
    except Exception as e:
        raise ValueError(f"Failed to read DOCX file: {str(e)}")

def extract_contact_info(text: str) -> Dict[str, Optional[str]]:
    """Extracts candidate contact metadata (email, phone, potential name)."""
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', text)
    email = email_match.group(0) if email_match else None

    phone_match = re.search(r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
    phone = phone_match.group(0) if phone_match else None

    # Estimate candidate name from the first non-empty lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    estimated_name = None
    for line in lines[:5]:
        # Filter out lines that look like emails, URLs, or addresses
        if "@" in line or "http" in line or len(line) > 50 or re.search(r'\d', line):
            continue
        words = line.split()
        if 1 <= len(words) <= 4 and all(w[0].isupper() for w in words if w.isalpha()):
            estimated_name = line
            break

    return {
        "name": estimated_name or "Candidate",
        "email": email,
        "phone": phone
    }

def extract_skills(text: str) -> List[str]:
    """Extracts technical skills by scanning against the technical skills taxonomy."""
    text_lower = text.lower()
    found_skills = set()

    for skill in TECHNICAL_SKILLS_TAXONOMY:
        # Match as whole word / phrase
        pattern = r'(?<![a-zA-Z0-9])' + re.escape(skill) + r'(?![a-zA-Z0-9])'
        if re.search(pattern, text_lower):
            found_skills.add(skill.title() if len(skill) > 3 else skill.upper())

    # Common programming languages capitalization
    clean_skills = []
    for s in sorted(found_skills):
        if s.lower() in ["sql", "html", "css", "api", "cnn", "rnn", "lstm", "bert", "gpt", "llm", "svm", "pca"]:
            clean_skills.append(s.upper())
        elif s.lower() == "javascript":
            clean_skills.append("JavaScript")
        elif s.lower() == "typescript":
            clean_skills.append("TypeScript")
        elif s.lower() == "next.js":
            clean_skills.append("Next.js")
        elif s.lower() == "node.js":
            clean_skills.append("Node.js")
        elif s.lower() == "fastapi":
            clean_skills.append("FastAPI")
        elif s.lower() == "scikit-learn":
            clean_skills.append("Scikit-Learn")
        else:
            clean_skills.append(s.title())

    return clean_skills

def extract_sections(text: str) -> Dict[str, List[str]]:
    """Heuristically extracts education, experience, and project snippets from resume text."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    sections = {
        "education": [],
        "experience": [],
        "projects": []
    }

    current_section = None
    section_headers = {
        "education": ["education", "academic background", "qualifications", "academics"],
        "experience": ["experience", "employment", "work history", "professional experience", "internship", "internships"],
        "projects": ["projects", "personal projects", "academic projects", "key projects", "notable projects"]
    }

    for line in lines:
        line_lower = line.lower().strip(":#- ")
        matched_header = None
        for sec, headers in section_headers.items():
            if any(line_lower == h or line_lower.startswith(h + " ") or line_lower.endswith(" " + h) for h in headers):
                matched_header = sec
                break

        if matched_header:
            current_section = matched_header
            continue

        if current_section:
            # Check if this line looks like another unknown header
            if len(line) < 30 and line.isupper() and not any(w in line.lower() for w in ["university", "college", "company", "inc", "ltd"]):
                current_section = None
                continue
            sections[current_section].append(line)

    # Clean and cap section lines
    cleaned_sections = {}
    for sec, items in sections.items():
        joined = " ".join(items)
        # Split into bullet items or sentences
        parts = [p.strip() for p in re.split(r'•|–|- |\n|\.\s+', joined) if len(p.strip()) > 15]
        cleaned_sections[sec] = parts[:6]

    return cleaned_sections

def parse_resume_file(file_path: str) -> Dict[str, Any]:
    """
    Main entry point for parsing an uploaded resume file (PDF or DOCX).
    Returns a clean, structured dictionary representing the candidate's profile.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Resume file not found at: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        raw_text = extract_text_from_pdf(file_path)
    elif ext in ['.docx', '.doc']:
        raw_text = extract_text_from_docx(file_path)
    elif ext == '.txt':
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            raw_text = f.read()
    else:
        raise ValueError(f"Unsupported file format '{ext}'. Please upload a PDF or DOCX resume.")

    if not raw_text or len(raw_text.strip()) < 50:
        raise ValueError("Uploaded resume appears to be empty or contains insufficient text.")

    contact = extract_contact_info(raw_text)
    skills = extract_skills(raw_text)
    sections = extract_sections(raw_text)

    # Identify primary suggested domain from skills
    skill_lower_set = {s.lower() for s in skills}
    domain_scores = {
        "Artificial Intelligence": sum(1 for s in ["bfs", "dfs", "a*", "search algorithms", "expert systems", "reinforcement learning", "heuristics"] if s in skill_lower_set),
        "Machine Learning": sum(1 for s in ["machine learning", "deep learning", "cnn", "rnn", "transformer", "scikit-learn", "tensorflow", "pytorch", "xgboost"] if s in skill_lower_set),
        "Data Science": sum(1 for s in ["pandas", "numpy", "statistics", "data science", "sql", "ab testing", "feature engineering", "matplotlib"] if s in skill_lower_set),
        "Web Development": sum(1 for s in ["react", "next.js", "javascript", "typescript", "fastapi", "node.js", "html", "css", "docker", "rest api"] if s in skill_lower_set)
    }
    suggested_domain = max(domain_scores, key=domain_scores.get) if any(domain_scores.values()) else "Artificial Intelligence"

    return {
        "success": True,
        "filename": os.path.basename(file_path),
        "candidate_name": contact["name"],
        "email": contact["email"],
        "phone": contact["phone"],
        "extracted_skills": skills,
        "skills_count": len(skills),
        "education": sections["education"],
        "experience": sections["experience"],
        "projects": sections["projects"],
        "suggested_domain": suggested_domain,
        "raw_text_length": len(raw_text),
        "summary": (
            f"Extracted {len(skills)} technical skills. "
            f"Identified {len(sections['projects'])} project items and {len(sections['education'])} education items. "
            f"Recommended domain: {suggested_domain}."
        )
    }

if __name__ == "__main__":
    print("Resume Parser Module ready.")
