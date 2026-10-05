# Synthetic Clusters + CI Lab


**Points: 8**
Train a simple classifier on two synthetic 2D point clouds and wire the result into GitHub Actions.

---

1. Copy these files locally and create a **private** repository named `Lab-1_<your-student-number>` (e.g. `Lab-1_s12345`) in the `PROJ-D-2024` organization. Only the repository owner should have access.

2. a) Rename `train.py` to `<your-student-number>.py`.  
   b) In the script, implement a function that automatically generates **two** datasets in 2D space. Each dataset should be a cloud of nearby points, and the two clouds should be far enough apart to be visually separable. Each cloud should contain **50–100** points.  
   c) Using the generated data, train a model in the same script that predicts which cloud a given point belongs to.

3. Fill in `requirements.txt`.

4. Complete `.github/workflows/ci.yml` so that the step:

   ```yaml
   run: cat accuracy.txt
   ```

   prints:

   ```
   Model trained with accuracy: <result-in-percent>%
   ```

---
