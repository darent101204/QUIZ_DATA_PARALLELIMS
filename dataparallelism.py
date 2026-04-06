import multiprocessing
import os
import time
import random
def analyze_score(score):
    pid = os.getpid()
    print(f"[Process {pid}] START score: {score}")
    time.sleep(0.3)  # simulasi proses
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "E"
    
    status = "LULUS" if score >= 40 else "TIDAK LULUS"
    result = {
        "score": score,
        "grade": grade,
        "status": status
    }
    print(f"[Process {pid}] DONE score: {score}")
    return result

if __name__ == "__main__":
    dataset = [random.randint(30, 100) for _ in range(150)]
    
    print("=== DATA PARALLELISM: ANALISIS NILAI SISWA ===")
    print("Total data:", len(dataset))
    print("Processing...\n")
    
    start = time.time()
    
    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(analyze_score, dataset)
    end = time.time()
    
    print("\n=== HASIL (10 DATA PERTAMA) ===")
    for r in results[:10]:
        print(r)
    
    print("\nTotal processed:", len(results))
    print("Execution time:", round(end - start, 2), "seconds")