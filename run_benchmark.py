# -*- coding: utf-8 -*-
"""
AI Mock Interview Evaluation System - Reproducible Benchmark Runner
=================================================================
Runs all 1,200 candidate sample answers across 300 technical interview questions
through the AnswerEvaluator, generates comprehensive performance metrics,
and exports granular sample-level predictions to `benchmark_results.csv`.
"""

import sys
import os
import json
import csv
import numpy as np
from scipy.stats import spearmanr
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

sys.path.insert(0, os.path.abspath('.'))
from evaluate_answer import AnswerEvaluator


def run_benchmark(output_csv: str = "benchmark_results.csv"):
    dataset_path = os.path.join("dataset", "interview_dataset.json")
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found at {dataset_path}")

    with open(dataset_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    evaluator = AnswerEvaluator(
        similarity_weight=0.35,
        concept_coverage_weight=0.65,
        concept_match_threshold=0.20,
        use_sentence_transformers=False
    )

    print("=" * 80)
    print("AI Mock Interview Evaluation System - Benchmark Execution")
    print("=" * 80)
    print(f"Loaded {len(dataset)} questions from {dataset_path}.")
    print("Evaluating 1,200 candidate responses...")

    results = []
    tier_labels = ['excellent', 'good', 'average', 'poor']

    for q in dataset:
        qid = q['question_id']
        question = q['question']
        model_answer = q['model_answer']
        expected_concepts = q['expected_concepts']
        domain = q['domain']
        level = q['level']
        topic = q['topic_tag']
        keywords = q.get('keywords', [])

        for sa in q['sample_answers']:
            sid = sa['sample_id']
            ref_tier = sa['quality_level']
            ref_score = float(sa['human_score'])
            cand_text = sa['answer_text']
            expected_missing = sa.get('missing_concepts', [])

            eval_res = evaluator.evaluate(
                question=question,
                model_answer=model_answer,
                expected_concepts=expected_concepts,
                candidate_answer=cand_text,
                keywords=keywords,
                domain=domain,
                level=level,
                topic_tag=topic
            )

            pred_score = eval_res['provisional_score']
            pred_tier = eval_res['predicted_quality_level']
            err = pred_score - ref_score

            results.append({
                'question_id': qid,
                'sample_id': sid,
                'domain': domain,
                'level': level,
                'topic_tag': topic,
                'expected_quality': ref_tier,
                'reference_score': ref_score,
                'predicted_score': pred_score,
                'predicted_quality': pred_tier,
                'absolute_error': round(abs(err), 2),
                'signed_error': round(err, 2),
                'semantic_similarity': eval_res['semantic_similarity'],
                'raw_similarity': eval_res['raw_similarity'],
                'concept_coverage': eval_res['concept_coverage_score'],
                'expected_missing_count': len(expected_missing),
                'detected_missing_count': len(eval_res['possible_missing_concepts']),
                'detected_misconceptions': json.dumps(eval_res['possible_misconceptions'], ensure_ascii=False),
                'warnings': json.dumps(eval_res['warnings'], ensure_ascii=False),
                'explanation': eval_res['explanation'],
                'candidate_text': cand_text
            })

    print(f"Completed evaluation for all {len(results)} sample answers.")

    # Export to benchmark_results.csv
    csv_headers = [
        'question_id', 'sample_id', 'domain', 'level', 'topic_tag',
        'expected_quality', 'reference_score', 'predicted_score', 'predicted_quality',
        'absolute_error', 'signed_error', 'semantic_similarity', 'raw_similarity',
        'concept_coverage', 'expected_missing_count', 'detected_missing_count',
        'detected_misconceptions', 'warnings', 'explanation'
    ]

    with open(output_csv, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_headers, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(results)

    print(f"[EXPORT] Saved {len(results)} evaluated records to {output_csv}.")

    # Calculate overall metrics
    ref_scores = np.array([r['reference_score'] for r in results])
    pred_scores = np.array([r['predicted_score'] for r in results])
    ref_tiers = [r['expected_quality'] for r in results]
    pred_tiers = [r['predicted_quality'] for r in results]

    mae = float(np.mean(np.abs(ref_scores - pred_scores)))
    rmse = float(np.sqrt(np.mean((ref_scores - pred_scores) ** 2)))
    spearman_corr, p_val = spearmanr(ref_scores, pred_scores)
    acc = accuracy_score(ref_tiers, pred_tiers)

    cm = confusion_matrix(ref_tiers, pred_tiers, labels=tier_labels)
    prec, rec, f1, supp = precision_recall_fscore_support(ref_tiers, pred_tiers, labels=tier_labels, zero_division=0)

    print("\n" + "=" * 80)
    print("OVERALL EVALUATION ENGINE BENCHMARK RESULTS")
    print("=" * 80)
    print(f"Total Sample Answers Evaluated : {len(results)}")
    print(f"Mean Absolute Error (MAE)      : {mae:.2f} points")
    print(f"Root Mean Squared Error (RMSE) : {rmse:.2f} points")
    print(f"Spearman Rank Correlation      : {spearman_corr:.4f} (p-value: {p_val:.2e})")
    print(f"Classification Accuracy        : {acc * 100:.2f}%")

    print("\nConfusion Matrix (Rows=Expected Category, Columns=Predicted Category):")
    print(f"{'':14}" + "".join([f"{l:>14}" for l in tier_labels]))
    for idx, row in enumerate(cm):
        print(f"{tier_labels[idx]:14}" + "".join([f"{val:>14}" for val in row]))

    print("\nPer-Category Classification Metrics:")
    for idx, t in enumerate(tier_labels):
        print(f"  {t:<11} | Precision: {prec[idx]:.3f} | Recall: {rec[idx]:.3f} | F1-Score: {f1[idx]:.3f} | Support: {supp[idx]}")

    print("\nPerformance by Technical Domain:")
    for d in ['AI', 'ML', 'Web Development', 'Data Science']:
        d_sub = [r for r in results if r['domain'] == d]
        d_ref = [r['reference_score'] for r in d_sub]
        d_pred = [r['predicted_score'] for r in d_sub]
        d_mae = np.mean(np.abs(np.array(d_ref) - np.array(d_pred)))
        d_corr, _ = spearmanr(d_ref, d_pred)
        d_acc = accuracy_score([r['expected_quality'] for r in d_sub], [r['predicted_quality'] for r in d_sub])
        print(f"  {d:<16} | MAE: {d_mae:5.2f} | Spearman: {d_corr:.4f} | Accuracy: {d_acc * 100:.2f}%")

    print("\nPerformance by Question Difficulty Level:")
    for lvl in ['easy', 'medium', 'hard']:
        l_sub = [r for r in results if r['level'] == lvl]
        l_ref = [r['reference_score'] for r in l_sub]
        l_pred = [r['predicted_score'] for r in l_sub]
        l_mae = np.mean(np.abs(np.array(l_ref) - np.array(l_pred)))
        l_corr, _ = spearmanr(l_ref, l_pred)
        l_acc = accuracy_score([r['expected_quality'] for r in l_sub], [r['predicted_quality'] for r in l_sub])
        print(f"  {lvl:<16} | MAE: {l_mae:5.2f} | Spearman: {l_corr:.4f} | Accuracy: {l_acc * 100:.2f}%")

    print("\nPerformance by Expected Quality Category:")
    for t in tier_labels:
        t_sub = [r for r in results if r['expected_quality'] == t]
        t_ref = [r['reference_score'] for r in t_sub]
        t_pred = [r['predicted_score'] for r in t_sub]
        t_mae = np.mean(np.abs(np.array(t_ref) - np.array(t_pred)))
        print(f"  {t:<11} | Avg Reference: {np.mean(t_ref):5.1f} | Avg Predicted: {np.mean(t_pred):5.1f} | MAE: {t_mae:5.2f}")

    return {
        'mae': mae,
        'rmse': rmse,
        'spearman_corr': spearman_corr,
        'accuracy': acc,
        'confusion_matrix': cm.tolist(),
        'results_count': len(results)
    }

if __name__ == '__main__':
    run_benchmark()
